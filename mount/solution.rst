Solution
---------

The code written below gives the same output as that given by the mount command on the terminal. The code first opens a file named mounts present in /proc
directory,then reads its contents and then prints the contents(required output).then we closes this file to prevent the program from crashing. The comment linesspecifies the function of each command.

Code
----
#!/usr/bin/env python         
f = open("/proc/mounts")      #this opens the mounts file present inside proc directory 
print f.read()                #reads the text inside the mounts file.
f.close()                     #closes the file after use.

Link
----
The link of the solution is:

