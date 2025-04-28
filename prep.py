#!/usr/bin/python3
import subprocess

# Open the file in read mode
file = open("/etc/default/grub", "r+")

# Read each line one by one
nf = list(line for line in file)

def warn():
	answer = input("WARNING: You are about to make changes to your boot configuration! This is meant for advanced users only! Do you want to continue? [y/N] ")
	if answer.lower()[0] == 'y' :
		return
	elif answer.lower()[0] == 'n' :
		quit(1)
	else:
		print("ERROR: Please provide a valid answer!")
		warn()

for l in nf:
	if "GRUB_CMDLINE_LINUX_DEFAULT" in l:  # Find the line we are looking for
		if "text" in l:
			print("no preliminary work to be done...")
			quit(2)
		else:
			warn()
		print("doing preliminary work, you will be greeted with a terminal session after rebooting, run post.sh to undo these changes upon completion")
		i = nf.index(l)
		s = "GRUB_CMDLINE_LINUX_DEFAULT=\"intel_iommu=on nomodeset\""	# Replace it with our desired settings
		print(s)
		nf[i] = s

"""
for l in nf:
	if "GRUB_CMDLINE_LINUX_DEFAULT" in l:  # .strip() to remove newline characters
		print(l.strip())
"""

# Close the file
file.close()

subprocess.run(["grub-mkconfig", "-o", "/boot/grub/grub.cfg"])

print("preliminary work completed. please restart your computer and re-run the script")
quit(0)
