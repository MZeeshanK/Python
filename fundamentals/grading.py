max = int(input('Enter the max marks: '))
marks = int(input('Enter the marks: '))

per = (marks/max) * 100

if per >= 85:
  print("Grade is S")
elif per >= 75:
  print("Grade is A")
elif per >= 65:
  print("Grade is B")
elif per >= 55:
  print("Grade is C")
else:
  print("Failed the class")
