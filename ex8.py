textfile=raw_input("please input the flie's name:")
text=open(textfile,"r")
print"The content of %s:"%textfile
print text.read()
