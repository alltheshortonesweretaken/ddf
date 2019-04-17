# ddf
A friend left me with an HP ML310 with Windows and asked me to re-set
the Administrator password.  Usually, this isn't super hard: I can boot
pogostick Linux just fine and to the Windows SAM update thing to allow
access to the machine again.  On this machine, though, pogostick linux,
Knoppix, and Debian have all failed to assemble the onboard RAID.
No big deal...  I can take each of the 4 disks out, image them, and
assemble the RAID from loopback devices.

This has failed too.  :(

So, here's an attempt at putting some Python together to get the data
out of the RAID set into a nice file.  Stupid RAID is bad, mmkay?
Stupid RAID that is implemented by Windows drivers that can't be found
any more is bad, too.

Anyway...

Documentation for the SNIA Common RAID Disk Data Format v1.2 (DDF) can
be found at
https://www.snia.org/sites/default/files/SNIA-DDFv1.2_with_Errata_A_Applied.pdf

This repository is intended to make dealing with such disks a little bit easier.
