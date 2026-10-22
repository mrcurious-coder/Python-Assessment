#Q1
a=['Milk', 'Bread', 'Eggs', 'Butter']
print(a)
print(len(a))

#Q2
movies = ["Avengers", "Inception", "Interstellar", "Dangal", "3 Idiots"]
print(movies[0])
print(movies[4])
print(movies[2])

#Q3
menu = ["Chai", "Samosa", "Biryani", "Dosa", "Paneer", "Naan"]
print(menu[0:3])
print(menu[4:])
print(menu[1:5])

#Q4
print("Q4")
colors = ["Red", "Gren", "Blue"]
colors[1]=colors[1][:2]+"e"+colors[1][2:] # gren=gren(gr_)+"e"+en  , output is green.
print(colors)

#Q5
friends = ["Aman", "Priya", "Rohan"]
friends.append("Neha")
print(friends)

#Q6
class_lt = ["Aman", "Priya", "Rohan","Neha","Kavya"]
class_lt.remove("Aman")
print(class_lt)

#Q7
shopping = ["Milk", "Bread", "Eggs"]
a=input("Enter any name: Milk, Bread, Eggs: ")
print(a,"is there in shopping: ",a in shopping)
print(f"Is Butter there in the list: {"Butter" in shopping}")

#Q8
days=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days)
print(len(days))
print(type(days))

#Q9
print("Q9 starts here")
a = ("Hello")
b = ("Hello",)
print(type(a))
print(type(b))

#Q10
print("Q10 starts here")
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(weekdays[:1])
print(weekdays[4:5])
print(weekdays[1:4])
print("Sat" in weekdays)

#Q11
a=[]
a.append("Tum Hi Ho")
a.append("Kesariya")
a.append("Kal Ho Na Ho")
a.remove("Kesariya")
a.insert(0,"Kesariya")
print(a)

#Q12
subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
subjects[1:3]=("Economics","Statistics")
print(subjects)

#Q13
team_a = ["Virat", "Rohit", "Dhoni"]
team_b = ["Bumrah", "Jadeja"]
team_a.extend(team_b)
team_a.insert(1,"Hardik")
print(team_a)
print(len(team_a))

#Q14
items = ["Pen", "Book", "Eraser", "Ruler", "Pencil"]
x=items.pop(2)
print("Removed:",x)
print(items)

#Q15
lst=['Aman', 20, True, 8.5]
print(lst)
for i in lst:
    print(type(i))

#Q16
numbers=[1, 2, 3, 4, 5]
print("Original:",numbers)
print("Reversed:",numbers[::-1])

#Q17
colors = ("Red", "Green", "Blue")
a = list(colors)
a[1] ="Yellow"
colors=tuple(a)
print(colors)
print(type(colors))

#Q18
fruits = ("Apple", "Banana")
fruits += ("Mango",)
print(fruits)
print(len(fruits))

#Q19
a=["Math", "Science", "English"]
b=("Math", "Science", "English")
print(a)
print(b)
print(type(a))
print(type(b))
a[0]="Art"
a[0]="Art"
print(a)
print(b)

#Q20
a=("Priya", 2024005, "CSE")
b=[85, 92, 78, 88]
print("Name:", a[0])
print("Branch:", a[2])
print("First Marks:", b[0])
b[2]=82
print(b)