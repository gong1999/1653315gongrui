from sys import argv
script,textfile=argv
text=open(textfile,"w")
line1="My name is Gong Rui."
line2="I am 18."
line3="I like studying."
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()
