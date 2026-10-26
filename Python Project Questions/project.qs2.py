students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

while True:
  print("Choose: \n1. Add student,\n2. View all students,\n3. Show topper,\n4. Exit")

  choice = input("Enter choice: ")

  if choice == "1":
    name = input("Enter student name: ")
    while name in students:
      print("Student already exists.")
      name = input("Enter student name: ")

    marks = []
    i = 0
    while i < 3:
      mark = float(input("Enter mark: "))
      if mark >= 0 and mark <= 100:
        marks.append(mark)
        i = i + 1
      else:
        print("Invalid mark, try again.")
    students[name] = marks
    print("Student added successfully!")

  elif choice == "2":
    names = list(students.keys())
    i = 0
    while i < len(names):
      name = names[i]
      m = students[name]
      avg = (m[0] + m[1] + m[2]) / 3
      if avg >= 85:
        grade = "A"
      elif avg >= 70:
        grade = "B"
      elif avg >= 50:
        grade = "C"
      else:
        grade = "F"
      print(f"{name} {avg:.2f} {grade}")
      i = i + 1

  elif choice == "3":
    names = list(students.keys())
    topper_name = names[0]
    m = students[topper_name]
    highest_avg = (m[0] + m[1] + m[2]) / 3

    i = 1
    while i < len(names):
      name = names[i]
      m = students[name]
      avg = (m[0] + m[1] + m[2]) / 3
      if avg > highest_avg:
        highest_avg = avg
        topper_name = name
      i = i + 1
    print("Topper:", topper_name)

  elif choice == "4":
    print("Goodbye!")
    break

  else:
    print("Invalid choice, try again.")