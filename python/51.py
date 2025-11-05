f1=open("input.txt","r")
f2=open("output1.txt","w")
count=1

for i in f1:
    if count%2!=0 :
        f2.write(i)
    count+=1