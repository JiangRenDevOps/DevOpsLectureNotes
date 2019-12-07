# Check Linux Kernel version
unmae -a

uname -srm

# Check Linux Distribution
cat /etc/os-release


# CPU
less /proc/cpuinfo

# To count the number of processing units use grep with wc
cat /proc/cpuinfo | grep processor | wc -l

# To get the actual number of cores, check the core id for unique values
cat /proc/cpuinfo | grep 'core id'

lscpu

# Memory
cat /proc/meminfo

top

htop

free -m

vmstat -s

# Disk
df -h

fdisk -l

# IO
iostat

atop


#Network
ifconfig

# List DNS servers for internet domain name resolution.
/etc/resolv.conf
# Lists hosts to be resolved locally (not by DNS).
/etc/hosts
# Specify network configuration and devices. eg. Static IP and info, DHCP, etc.
less /etc/network/interfaces

# http://www.yolinux.com/TUTORIALS/LinuxTutorialNetworking.html