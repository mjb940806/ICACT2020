import glob
import re
import os
import sys

s = "getenv|printf|strcpy|vfprintf|vsprintf|wcscat|wctomb|bsearch|gmtime|qsort|strerror|vfscanf|vsscanf|wcscpy|wmemcpy|localtime|setbuf|strncat|vfwprintf|vswprintf|wcsncat|wmemmove|fprintf|mbsrrtowcs|snprintf|strncpy|vfwscanf|vswscanf|wcsncpy|wprintf|fscanf|mbstowcs|sprintf|strtok|vprintf|vwprintf|wcsrtombs|wscanf|fwprintf|memcpy|sscanf|swprintf|vscanf|vwscanf|wcstok|fwscanf|memmove|strcat|swscanf|vsnprintf|wcrtomb|wcstombs"
p = re.compile(s)
count = 0
total = 0
filelist = sorted(glob.glob('C/testcases/CWE401_Memory_Leak/s*/*[0-9].c'))

for i in filelist:
    with open(i, 'r') as f:
        total = total + 1
        for x,y in enumerate(f.readlines(),1):
            m = p.search(y)
            if m:
                print(i)
                os.system("rm "+i)
                count = count + 1
                break

print(str(count)+"/"+str(total))
