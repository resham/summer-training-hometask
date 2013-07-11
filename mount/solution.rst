Solution
---------

The code written below gives the same output as that given by the mount command on the terminal. The code first opens a file named mounts present in /proc
directory,then reads its contents line by line and then prints the contents(required output)after carrying functions such as strip,insert, delete etc.then we closes this file to prevent the program from crashing. 

Code
----
1.#!/usr/bin/env python         
2.f = open("/proc/mounts")      #this opens the mounts file present inside p      roc directory 
3. b= f.readlines()                #reads the text inside the mounts file.

3.for x in b[1:]:# for loop which ignores the first line of the file and begins from the second line of the file
4.    l = x.split(" ")#splits the file line by line according to spaces
5.    del l[-2]#deletes the second last zero from the file
6.    del l[-1]#deletes the last zero from the file
7.    l.insert(2,"type ")# the string "type" is inserted in index 2
8.    l.insert(1,"on")# the string "on" is inserted in index 1
9.    l.insert(5,"(")# the opening bracket "(" is inserted in the 5th index
10.   l.insert(7,")")# the closing bracket ")" is inserted in the 7th index
11.   str = " ".join(l)# the splitted string is joined using the join() function
12.print str
13.f.close()                     #closes the file after use.

Link
----
The link of the  code solution is:
`Link<https://github.com/resham/summer-training-hometask/blob/master/mount.py>`_
