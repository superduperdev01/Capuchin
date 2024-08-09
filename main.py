import sys
import os
from shutil import which
print("Welcome to Capuchin Programming Language Compiler!")
if len(sys.argv)==1:
    file=input("File to compile? ")
else:
    file=sys.argv[1]
try:
    code_file=open(file, "r")
    code=code_file.readlines()
    code_file.close()
except:
    print("No such file or directory: "+file)
    sys.exit()
for n in range(0, len(code)):
    code[n]=code[n].strip()
if code[0][slice(2)]=="#!":
    path=code[0][::-1][slice(len(code[0])-2)][::-1]
elif len(sys.argv)==3:
    path=sys.argv[2]
else:
    path=input("Capuchin Binary Path? ")
def combine_args(start, end):
    global tmp
    global args
    global n
    global cmd
    tmp=""
    for n in range(start, len(args)-end):
        if not var_name.__contains__(args[n]) and not str_name.__contains__(args[n]):
            tmp=tmp+args[n]+" "  
        elif var_name.__contains__(args[n]):
            tmp=tmp+"\"+str("+args[n]+")+\""
        elif str_name.__contains__(args[n]):
            tmp=tmp+"\"+"+args[n]+"+\""
def add_str(add):
    global str_name
    global var_name
    if not str_name.__contains__(add) and not var_name.__contains__(add):
            str_name.append(add)
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
def make_indent(value):
    indent=""
    for n in range(0, value):
        indent=indent+"    "
    return indent
def set_out(value):
    global out
    global indent
    out=out+make_indent(indent)+value
def import_sys():
    global out
    global use_sys
    if not use_sys:
        use_sys=1
        out="import sys\n"+out
i=1
tmp=""
out=""
var_name=[]
str_name=[]
indent=0
use_sys=0
lists=[]
defs=""
for n in code:
    if not n=="":
        args=sep_args(n)
    else:
        args=[""]
    cmd=args[0]
    last=args[len(args)-1]
    if defs.__contains__(cmd):
        tmp="("
        for n in range(1, len(args)):
            tmp=tmp+args[n]
            if n==len(args)-1:
                tmp=tmp+")"
            else:
                tmp=tmp+", "
        set_out(cmd+tmp+"\n")
    elif cmd=="echo":
        combine_args(1, 0)
        set_out("print(\""+tmp+"\")\n")
    elif cmd=="input":
        combine_args(1, 1)
        add_str(last)
        set_out(args[len(args)-1]+"=input(\""+tmp+"\")\n")
    elif cmd=="var":
        set_out(args[1]+"="+last+"\n")
        var_name.append(args[1])
        if str_name.__contains__(args[1]):
            str_name.remove(args[1])
    elif cmd=="str":
        tmp=""
        set_out(args[1]+"="+args[2]+"\n")
        for n in range(2, len(args)-1):
            tmp=tmp+args[n]
        add_str(args[1]+tmp)
        if var_name.__contains__(args[1]):
            var_name.remove(args[1])
    elif cmd=="if":
        set_out(n+":\n")
        indent=indent+1
    elif cmd=="else":
        set_out("else:\n")
        indent=indent+1
    elif cmd=="elif":
        set_out(n+":\n")
        indent=indent+1
    elif cmd=="}":
        if not indent==0:
            indent=indent-1
        else:
            print("Unexpected Ending Curly Bracket: "+cmd+" at line: "+str(i))
            sys.exit()
    elif cmd=="lower":
        set_out(args[2]+"="+args[1]+".lower()\n")
        add_str(last)
    elif cmd=="upper":
        set_out(args[2]+"="+args[1]+".upper()\n")
        add_str(last)
    elif cmd=="list":
        if args[1]=="add":
            lists.append(last)
            set_out(last+"=[]\n")
        elif args[1]=="del":
            combine_args(3)
            set_out(args[2]+".remove(\""+tmp+"\")\n")
        elif args[1]=="app":
            combine_args(3)
            set_out(args[2]+".append(\""+tmp+"\")\n")
        elif args[1]=="get":
            set_out(last+"="+args[2]+"["+args[3]+"]\n")
            add_str(last)
    elif cmd=="len":
        set_out(last+"=len("+args[1]+")\n")
        if not var_name.__contains__(last):
            var_name.append(last)
    elif cmd=="while":
        set_out("while(1):")
        indent=indent+1
    elif cmd=="exit":
        import_sys()
        set_out("sys.exit()\n")
    elif cmd=="break":
        set_out("break")
    elif cmd=="def":
        tmp=""
        i=0
        set_out("def ")
        for n in args:
            if not n=="def":
                if tmp==", " and i==len(args)-1:
                    tmp="):\n"
                if not n=="-":
                    set_out(n+tmp)
                    if not tmp==", ":
                        defs=defs+n+"\n"
                else:
                    tmp=", "
                    set_out("(")
            i=i+1
        indent=indent+1
    elif cmd=="include":
        os.system(path+" "+args[1]+".cpu -i")
        def_file=open("defs.txt", "r")
        defs=defs+def_file.read()
        def_file.close()
        def_file=open(args[1]+".py", "r")
        out=def_file.read()+out
        def_file.close()
    elif cmd=="printvar":
        set_out("print("+args[1]+")\n")
    elif not cmd=="" and not cmd[0]=="#":
        print("Unknown Command: "+cmd+" at line: "+ str(i))
        def_file=open("defs.txt", "a")
        def_file.write(defs)
        def_file.close()
        sys.exit()
    i=i+1
file=os.path.splitext(file)[0]
out_name=file+".py"
out_file=open(out_name, "w")
out_file.write(out)
out_file.close()
if sys.argv[len(sys.argv)-1]=="-i":
    def_file=open("defs.txt", "w")
    def_file.write(defs)
    def_file.close()
    sys.exit()
if which("pyinstaller") is None:
    print("pyinstaller is required to continue comiling!")
    print("Try running pip install pyinstaller")
    if not os.name=="nt":
        os.system("rm "+out_name)
    else:
        os.system("del /Q "+out_name)
    sys.exit()
os.system("pyinstaller -F "+ out_name)
if not os.listdir().__contains__("dist"):
    sys.exit()
if not os.name=="nt":
    os.system("mv ./dist/"+file+" ./"+file+".elf")
    os.system("rm -r build dist")
    os.system("rm "+file+".spec")
    os.system("rm "+out_name)
    os.system("clear")
    os.system("./"+file+".elf")
else:
    os.system("move ./dist/"+file+" ./"+file+".exe")
    os.system("rmdir build dist")
    os.system("del /Q "+file+".spec")
    os.system("del /Q "+out_name)
    os.system("cls")
    os.system(file+".exe")