import sys
import os
if len(sys.argv)==1:
    file=input("File to compile? ")
else:
    file=sys.argv[1]
code_file=open(file, "r")
code=code_file.readlines()
code_file.close()
for n in range(0, len(code)):
    code[n]=code[n].strip()
def sep_args(arg):
    i=0
    final=[]
    final.append("")
    for n in arg:
        if not n==" ":
            final[i]=final[i]+n
        else:
            final.append("")
            i=i+1
    return final
i=1
tmp=""
out=""
var_name=[]
for n in code:
    if not n=="":
        args=sep_args(n)
    else:
        args=[""]
    cmd=args[0]
    if cmd=="echo":
        tmp=""
        for n in range(1, len(args)):
            if not var_name.__contains__(args[n]):
                tmp=tmp+args[n]+" "
            else:
                tmp=tmp+"\"+"+args[n]+"+\""
        out=out+"print(\""+tmp+"\")\n"
    elif cmd=="input":
        tmp=""
        for n in range(1, len(args)-1):
            if not var_name.__contains__(args[n]):
                tmp=tmp+args[n]+" "
            else:
                tmp=tmp+"\"+"+args[n]+"+\""
        out=out+args[len(args)-1]+"=input(\""+tmp+"\")\n"
        if not var_name.__contains__(args[len(args)-1]):
            var_name.append(args[len(args)-1])
    elif cmd=="var":
        out=out+args[1]+"="+args[2]
        var_name.append(args[1])
    elif not cmd=="":
        print("Unknown Command: "+cmd+" at line: "+ str(i))
        sys.exit()
    i=i+1
out_name=file+".py"
out_file=open(out_name, "w")
out_file.write(out)
out_file.close()
os.system("pyinstaller -F "+ out_name)
os.system("mv ./dist/"+file+" ./"+file+".out")
os.system("rm -r build dist")
os.system("rm "+file+".spec")
os.system("rm "+out_name)
