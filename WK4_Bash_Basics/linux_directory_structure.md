## / – The root directory
Everything, all the files and directories, in Linux are located under ‘root’ represented by ‘/’. If you look at the directory structure, you’ll realize that it is similar to a plant’s root.
![Alt text](images/linux_folder.png?raw=true)

Linux applies Filesystem Hierarchy Standard (FHS).This FHS defines the directory structure and the content/purpose of the directories in Linux distributions. Thanks to this FHS, you’ll find the same directory structure in (almost) all the Linux distributions.
![Alt text](images/linux_directory_structure.png?raw=true)

## /bin – Binaries
The ‘/bin’ directly contains the executable files of many basic shell commands like ls, cp, cd etc. Mostly the programs are in binary format here and accessible by all the users in the Linux system.

## /etc – Configuration files
The /etc directory contains the core configuration files of the system, use primarily by the administrator and services, such as the password file and networking files.

If you need to make changes in system configuration (for example changing the hostname), this is where you’ll find the respective files.

## /usr – User binaries and program data
in ‘/usr’ go all the executable files, libraries, source of most of the system programs. For this reason, most of the files contained therein is read­only (for the normal user)

‘/usr/bin’ contains basic user commands
‘/usr/sbin’ contains additional commands for the administrator
‘/usr/lib’ contains the system libraries
‘/usr/share’ contains documentation or common to all libraries, for example ‘/usr/share/man’ contains the text of the man page

## /home – User personal data
Home directory contains personal directories for the users. The home directory contains the user data and user-specific configuration files. As a user, you’ll put your personal files, notes, programs etc in your home directory.

When you create a user on your Linux system, it’s a general practice to create a home directory for the user. Suppose your Linux system has two users, Alice and Bob. They’ll have a home directory of their own at locations /home/alice and /home/bob.

Do note that Bob won’t have access to /home/alice and vice versa. That makes sense because only the user should have access to his/her home. You may read about file permissions in Linux to know more on this topic.

## /lib – Shared libraries
Libraries are basically codes that can be used by the executable binaries. The /lib directory holds the libraries needed by the binaries in /bin and /sbin directories.

Libraries needed by the binaries in the /usr/bin and /usr/sbin are located in the directory /usr/lib.

## /sbin – System binaries
This is similar to the /bin directory. The only difference is that is contains the binaries that can only be run by root or a sudo user. You can think of the ‘s’ in ‘sbin’ as super or sudo.

## /tmp – Temporary files
As the name suggests, this directory holds temporary files. Many applications use this directory to store temporary files. Even you can use directory to store temporary files.

But do note that the contains of the /tmp directories are deleted when your system restarts. Some Linux system also delete files old files automatically so don’ store anything important here.

## /var – Variable data files
Var, short for variable, is where programs store runtime information like system logging, user tracking, caches, and other files that system programs create and manage.

The files stored here are NOT cleaned automatically and hence it provides a good place for system administrators to look for information about their system behavior. For example, if you want to check the login history in your Linux system, just check the content of the file in /var/log/wtmp.

## /boot – Boot files
The ‘/boot’ directory contains the files of the kernel and boot image, in addition to LILO and Grub. It is often advisable that the directory resides in a partition at the beginning of the disc.

## /proc – Process and kernel files
The ‘/proc’ directory contains the information about currently running processes and kernel parameters. The content of the proc directory is used by a number of tools to get runtime system information.

For example, if you want to check processor information in Linux, you can simply refer to the file /proc/cpuinfo. You want to check memory usage of your Linux system, just look at the content of /proc/meminfo file.

## /opt – Optional software
Traditionally, the /opt directory is used for installing/storing the files of third-party applications that are not available from the distribution’s repository.

The normal practice is to keep the software code in opt and then link the binary file in the /bin directory so that all the users can run it.

## /root – The home directory of the root
There is /root directory as well and it works as the home directory of the root user. So instead of /home/root, the home of root is located at /root. Do not confuse it with the root directory (/).

## /media – Mount point for removable media
When you connect a removable media such as USB disk, SD card or DVD, a directory is automatically created under the /media directory for them. You can access the content of the removable media from this directory.

## /mnt – Mount directory
This is similar to the /media directory but instead of automatically mounting the removable media, mnt is used by system administrators to manually mount a filesystem.

## /srv – Service data
The /srv directory contains data for services provided by the system. For example, if you run a HTTP server, it’s a good practice to store the website data in the /srv directory.

I think this much information is enough for you to understand the Linux directory structure and its usage.

In the end, if you want, you can download and save this image for quick reference to the directory structure in Linux systems.

# Recap
![Alt text](images/linux_system_directoies_poster.png?raw=true)

ref: https://linuxhandbook.com/linux-directory-structure/ 