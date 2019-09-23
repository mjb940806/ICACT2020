import os
import sys #running commands
import glob #handling files

filelist = sorted(glob.glob('s*/*[0-9].c'))

count = 0
f = open ('output.txt')
f2 = open ('result.txt','w')
#recursion start
for filename in filelist: 

    func = filename.split("/")
    funcname = func[1]
    funcname = funcname.replace(".c", "_bad")
    os.system("cbmc "+filename+" --bounds-check --pointer-check --unwind 200 --function "+funcname+">> output.txt")
    data = f.read()
    result = data.split('\n')[-2]
    f2.write(filename+": "+result+"\n")
    if result == "VERIFICATION SUCCESSFUL":
        count = count + 1
#recursion end

f2.write("EXECUTION RATE: "+str(filelist.index(filename)+1)+"/"+str(len(filelist))+"\n")
f2.write("SUCCESS RATE: "+str(count)+"/"+str(len(filelist))+"\n")

f.close()
f2.close()
