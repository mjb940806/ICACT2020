import os
import sys # running commands
import glob # handling files

filelist = sorted(glob.glob('result_[0-9]*.txt'))
f2 = open ('result.txt','w')

for filename in filelist: 
	f = open (filename,'r')
	lines = f.readlines()
	last_line = lines[-1]
	f2.write(filename+"*****"+last_line)
	f.close()

f2.close()