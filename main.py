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
def combine_args():
    global tmp
    global args
    global n
    if not var_name.__contains__(args[n]):
        tmp=tmp+args[n]+" "  
    elif not str_name.__contains__(args[n]):
        tmp=tmp+"\"+str("+args[n]+")+\""
    else:
        tmp=tmp+"\"+"+args[n]+"+\""
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
str_name=[]
for n in code:
    if not n=="":
        args=sep_args(n)
    else:
        args=[""]
    cmd=args[0]
    if cmd=="echo":
        tmp=""
        for n in range(1, len(args)):
            combine_args()
        out=out+"print(\""+tmp+"\")\n"
    elif cmd=="input":
        tmp=""
        for n in range(1, len(args)-1):
            combine_args()
        out=out+args[len(args)-1]+"=input(\""+tmp+"\")\n"
        if not str_name.__contains__(args[len(args)-1]):
            str_name.append(args[len(args)-1])
    elif cmd=="var":
        out=out+args[1]+"="+args[2]+"\n"
        var_name.append(args[1])
    elif cmd=="str":
        out=out+args[1]+"="+args[2]+"\n"
        for n in range(1, len(args)-1):
            tmp=tmp+args[n]
        str_name.append("\""+tmp+"\"")
    elif not cmd=="" and not cmd[0]=="#":
        print("Unknown Command: "+cmd+" at line: "+ str(i))
        sys.exit()
    i=i+1
out_name=file+".py"
out_file=open(out_name, "w")
out_file.write(out)
out_file.close()
os.system("pyinstaller -F "+ out_name)
if not os.name=="nt":
    os.system("mv ./dist/"+file+" ./"+file+".out")
    os.system("rm -r build dist")
    os.system("rm "+file+".spec")
    os.system("rm "+out_name)
else:
    os.system("move ./dist/"+file+" ./"+file+".out")
    os.system("rmdir build dist")
    os.system("del /Q "+file+".spec")
    os.system("del /Q "+out_name)
