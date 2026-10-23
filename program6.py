f=open('append.txt')
words=[]
for line in f:
    temp=line.split()
    for i in temp:
        words.append(i)
f.close()
words.sort()
outfile=open('appendnew.txt','w')
for i in words:
    outfile.writelines(i)
    outfile.writelines("")
outfile.close()
