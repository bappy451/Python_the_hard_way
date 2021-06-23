import os


#os.rmdir("myfolder")
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
  

txt = open("file.txt","rt")

print("Here's your file.txt")
print(txt.read(5))
print()
print(txt.readline())
print ("Type the filename again:")
txt.close()

file_again = input("> ")

txt_again = open(file_again,'r')

print (txt_again.read())
txt_again.close()


print()
f = open("file.txt", "r")
for x in f:
  print(x)
f.close()