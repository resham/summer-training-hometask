Solution
---------

The code written below gives the same output as that given by the mount command on the terminal. The code first opens a file named mounts present in /proc
directory,then reads its contents line by line and then prints the contents(required output)after carrying functions such as strip,insert, delete etc.then we closes this file to prevent the program from crashing. 

Code
----
1.#!/usr/bin/env python         
2.f = open("/proc/mounts")      #this opens the mounts file present inside p      roc directory 
3. b= f.readlines()                #reads the text inside the mounts file.

3.for x in b[1:]:
4.    l = x.split(" ")
5.    del l[-2]
6.    del l[-1]
7.    l.insert(2,"type ")
8.    l.insert(1,"on")
9.    l.insert(5,"(")
10.   l.insert(7,")")
11.   str = " ".join(l)
12.print str
13.f.close()                     #closes the file after use.

Link
----
The link of the  code is:
https://github.com/resham/summer-training-hometask/blob/master/mount.py
