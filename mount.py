#!/usr/bin/env python
f = open("/proc/mounts")#opens file /proc/mounts
b = f.readlines()# reads the file line by line
for x in b[1:]:# for loop which ignores the first line of the file and begins from the second line of the file
    l = x.split(" ")#splits the file line by line according to spaces
    del l[-2]#deletes the second last zero from the file
    del l[-1]#deletes the last zero from the file
    l.insert(2,"type ")# the string "type" is inserted in index 2
    l.insert(1,"on")# the string "on" is inserted in index 1
    l.insert(5,"(")# the opening bracket "(" is inserted in the 5th index
    l.insert(7,")")# the closing bracket ")" is inserted in the 7th index
    str = " ".join(l)# the splitted string is joined using the join() function
    print str #the required output is printed; for loop ends
f.close()# file is closed
