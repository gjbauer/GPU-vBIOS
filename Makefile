all: catvbios

catvbios:
	cc -o catvbios catvbios.c

modvbios:
	cc -o modvbios modvbios.c

clean:
	rm catvbios modvbios
