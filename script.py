import os
import sys #running commands
import glob #handling files

filelist = sorted(glob.glob('s*/*[0-9].c'))
if len(filelist) == 0: # if there is no s* folder
    filelist = sorted(glob.glob('*[0-9].c'))

unwind = sys.argv[1]
count = 0
f = open ('output_'+unwind+'.txt','w+t')
f2 = open ('result_'+unwind+'.txt','w')
#recursion start
for filename in filelist:

    func = filename.find("CWE")
    funcname = filename[func:]
    funcname = funcname.replace(".c", "_bad")
    os.system("cbmc "+filename+" --bounds-check --pointer-check --pointer-overflow-check --unwind "+unwind+" --function "+funcname+">> output_"+unwind+".txt")
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
