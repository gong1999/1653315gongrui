from sys import argv
script,textfile=argv#input script,filename
text=open(textfile,"a")#open file
line1="My name is Gong Rui."
line2="I am 18."
line3="I like studying."
text.write(line1)#write file
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()#close file

textfile=raw_input("please input the flie's name which is going to be copied:")#input the flie's name which is going to be copied
text=open(textfile,"r")#open file
content=text.read()#read file
textfile=raw_input("please input the flie's name:")#input the flie's name
text=open(textfile,"w+")#open file
text.write(content)#write file
text.seek(0,0)#move the cursor
print"The content of %s:"%textfile
print text.read()#read the file
text.close()#close file
