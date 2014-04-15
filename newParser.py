import os
import sys
import filecmp

def main(argv):
    if(os.path.isdir("./screens")):
        os.system("rm -r ./screens")
        os.mkdir("./screens")
    else:
        os.mkdir("./screens")
    if(len(argv)==0):
        print "something wrong"
    else:
        screenCounter=0
        traces=[]
        for root,dirnames,filenames in os.walk(argv[0]):
            for dirname in dirnames:
                currentTrace=[]
                #print dirname
                for r,ds,fs in os.walk(os.path.join(root, dirname)):
                    i=1
                    while("uidump"+str(i)+".xml" in fs):
                        f="uidump"+str(i)+".xml"
                        #print f
                        match=False
                        matchFileName=""
                        for r2,ds2,fs2 in os.walk("./screens"):
                            for f2 in fs2:
                                file1=open(os.path.join(r, f),'r')
                                file2=open(os.path.join(r2,f2),'r')
                                string1=file1.read()
                                string2=file2.read()
                                if(string1==string2):
                                    match=True
                                    matchFileName=f2
                                    file1.close()
                                    file2.close()
                                    break
                                file1.close()
                                file2.close()
                        if(match):
                            #print "match"
                            currentTrace.append(matchFileName)
                        else:
                            screenCounter=screenCounter+1
                            file1=open(os.path.join(r, f),'r')
                            file2=open(os.path.expandvars("./screens/screen"+str(screenCounter)),'w')
                            file2.write(file1.read())
                            currentTrace.append("screen"+str(screenCounter))
                        i=i+1
                #print currentTrace
                traces.append((dirname,currentTrace))
        print traces

if __name__ == "__main__":
    main(sys.argv[1:])
