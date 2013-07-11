#!/usr/bin/env python         
f = open("/proc/mounts")      #this opens the mounts file present inside proc directory 
print f.read()                #reads the text inside the mounts file.
f.close()                     #closes the file after use.
