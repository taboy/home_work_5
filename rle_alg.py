with open("file1.txt","r") as data:
    data=data.readline()
number=''
code=''

for y in range(len(data)):
    if data[y].isdigit():
        number+=data[y]
    else:
        code+=data[y]*int(number)
        number=""

print(code)
with open("file3.txt","w")as data:
    data.write(code)