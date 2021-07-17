students = ["Aysegul","Selin","Beste","Elcin","Ceyda","Merve","Arzu"]

fileToAppend = open("students2","a")

for student in students:
  fileToAppend.write(student)
  fileToAppend.write("\n")

fileToAppend.close()
