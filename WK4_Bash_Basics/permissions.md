##Ownership of Linux files
### User
A user is the owner of the file. By default, the person who created a file becomes its owner. Hence, a user is also 
sometimes called an owner.

### Group
A user-group can contain multiple users. All users belonging to a group will have the same access permissions to the 
file. Suppose you have a project where a number of people require access to a file. Instead of manually assigning 
permissions to each user, you could add all users to a group, and assign group permission to file such that only this 
group members and no one else can read or modify the files.

### Other
Any other user who has access to a file. This person has neither created the file, nor he belongs to a usergroup who 
could own the file. Practically, it means everybody else. Hence, when you set the permission for others, it is also 
referred as set permissions for the world.

##Permissions
###Read
This permission give you the authority to open and read a file. Read permission on a directory gives you the ability 
to lists its content.

###Write
The write permission gives you the authority to modify the contents of a file. The write permission on a directory 
gives you the authority to add, remove and rename files stored in the directory. Consider a scenario where you have
 to write permission on file but do not have write permission on the directory where the file is stored. You will be
  able to modify the file contents. But you will not be able to rename, move or remove the file from the directory.

###Execute 
In Windows, an executable program usually has an extension ".exe" and which you can easily run. In Unix/Linux, you 
cannot run a program unless the execute permission is set. If the execute permission is not set, you might still be 
able to see/modify the program code(provided read & write permissions are set), but not run it.

## Check ownership and permissions
```$xslt
ls -l
```

##Absolute(Numeric) Mode
```
Number	Permission Type	       Symbol
0	No Permission	        ---
1	Execute	                --x
2	Write	                -w-
3	Execute + Write	        -wx
4	Read	                r--
5	Read + Execute	        r-x
6	Read + Write	        rw-
7	Read + Write + Execute	rwx
```
Let us change the search.sh file to have Read, Write and Execute and leave the rest with Read and Execute
```
chmod 755 search.sh
```
##Symbolic Mode

```
Operator	Description
+	Adds a permission to a file or directory
-	Removes the permission
=	Sets the permission and overrides the permissions set earlier.
```

```
User Denotations
u	user/owner
g	group
o	other
a	all
```
What do these commands mean?
```$xslt
chmod o=rwx report.txt
```
```$xslt
chmod g+x report.txt
```
```$xslt
chmod u-r report.txt
```

##Changing Ownership and Group
For changing the ownership of a file/directory, you can use the following command:
```
chown root report.txt
```
In case you want to change the user as well as group for a file or directory use the command
```$xslt
chown user:group report.txt
```