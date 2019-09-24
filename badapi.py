import glob
import re
import os
import sys

s = "getenv|printf|strcpy|vfprintf|vsprintf|wcscat|wctomb|bsearch|gmtime|qsort|strerror|vfscanf|vsscanf|wcscpy|wmemcpy|localtime|setbuf|strncat|vfwprintf|vswprintf|wcsncat|wmemmove|fprintf|mbsrrtowcs|snprintf|strncpy|vfwscanf|vswscanf|wcsncpy|wprintf|fscanf|mbstowcs|sprintf|strtok|vprintf|vwprintf|wcsrtombs|wscanf|fwprintf|memcpy|sscanf|swprintf|vscanf|vwscanf|wcstok|fwscanf|memmove|strcat|swscanf|vsnprintf|wcrtomb|wcstombs"
p = re.compile(s)
folderlist = ['121','122','124','126','127','190','191','369','415','416','476','681']
for folder in folderlist:
	filelist = sorted(glob.glob('C/testcases/CWE'+folder+'_*/s*/*[0-9].c'))
	count = 0
	total = 0
	for i in filelist:
	    with open(i, 'r') as f:
	        total = total + 1
	        for x,y in enumerate(f.readlines(),1):
	            m = p.search(y)
	            if m:
	                os.system("rm "+i)
	                count = count + 1
	                break
	print("CWE"+folder+": removed "+str(count)+" of "+str(total)+" files")
