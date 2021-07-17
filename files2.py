f = open("customer.txt","w")
print(f.write("Selin "))
print(f.write("Beste "))
print(f.write("Elcin"))



#close
f.close()

fileToAppend = open("students.txt","a")
fileToAppend.write("Aysegul ")
fileToAppend.write("Ceyda ")
fileToAppend.write("Merve ")

fileToAppend.close()

#clear file
import os
#os.remove("customer.txt")
#if os.path.exists("customer.txt"):
 # os.remove("customer.txt")

#else:
  #print("Not file")

os.rmdir("customer.txt")




