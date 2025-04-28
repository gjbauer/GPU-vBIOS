#!/bin/sh
echo 1 > /sys/devices/pci0000:00/0000:00:02.0/rom
cat /sys/devices/pci0000:00/0000:00:02.0/rom > vbios.dump
echo 0 > /sys/devices/pci0000:00/0000:00:02.0/rom
