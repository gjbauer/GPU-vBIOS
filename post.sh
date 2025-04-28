#!/bin/sh
sudo mv /etc/grub/grub.old /etc/grub/grub
grub-mkconfig -o /boot/grub/grub.cfg
echo "Successfully restored previous configuration!"
