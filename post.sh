#!/bin/sh
mv /etc/grub/grub.old /etc/grub/grub
grub-mkconfig -o /boot/grub/grub.cfg
systemctl set-default graphical.target
echo "Successfully restored previous configuration!"
