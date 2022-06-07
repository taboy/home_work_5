
with open("file.txt","w")as data:
    data.write("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW")
with open("file.txt","r") as data:
    data=data.readline()



count=1
string=''
for y in range(len(data)-1):
    if data[y]==data[y+1]:
        count+=1
    else:
        string+=str(count)+data[y]
        count=1
print(string)
with open("file1.txt","w")as data:
    data.write(string)



