Solution
---------

The code written below gives the same output as that given by the mount command on the terminal. The code first opens a file named mounts present in /proc
directory,then reads its contents and then prints the contents(required output).then we closes this file to prevent the program from crashing. The comment linesspecifies the function of each command.

Code
----
1. #!/usr/bin/env python         
2.f = open("/proc/mounts")      #this opens the mounts file present inside proc directory 
3.print f.read()                #reads the text inside the mounts file.
4.f.close()                     #closes the file after use.

Link
----
The link of the  code solution is:
https://github.com/resham/summer-training-hometask/blob/master/mount.py
