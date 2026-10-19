#Q:1
print("Hello, World!")
print("I am learning Python! ")

#Q:2
a="Arsad Ali"
b=18
c="Now I Live in Lucknow."
print(f"My name is {a}, I am {b} years old and {c} ")

#Q:3
print(25+17)
print(100-36)
print(5*12)
print(45/9)

#Q:4
print("Step 1")
#print("Step2")
print("Step 3")

#Q:5
a=5
b=10
print("Before:",a,b)
a,b=b,a
print("After:",a,b)

#Q6
x,y,z="Apple","Banana","Cheery"
a=b=c="Mango"
print(x,y,z)
print(a,b,c)

#Q7
a=10
b=3.14
c="Hello"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Q8
a=10
print(a,type(a))
print(float(a),type(float(a)))
print(float(a),type(str(a)))

#Q9
greeting="Hello, World!"
print(greeting.upper())
print(greeting.lower())
print(len(greeting))

#Q10
name="Priya"
marks=92
print(f"{name} scored {marks} marks.")

#Q11
item="Notebook"
price=45.50
qty=4
print("Item:",item,"\nPrice:",price,"\nQty:",qty)
print(f"Total:{4*45.50:.2f}")

#Q12
a="Programing"
print(a[:4]) # will print Prog
print(a[-10:-6]) # will print Prog
print(a[6:]) # will print ming
print(a[-4:]) # will print ming
print(a[3:7]) # will print gram
print(a[-7:-3]) # will print gram
print(a[::-1])

#Q13
text="Hello, Python World!"
print("Hello, Python World!")
print(text.replace("Python","Coding"))
print(text.split())

#Q14
a=17;b=5
print(f" Add:{a+b}\n Sub:{a-b}\n Mul:{a*b}\n Div:{a/b}\n IntDiv:{a//b}\n Mod:{a%b}\n Power:{a**b}")

#Q15   
m1=int("85")
m2=int("92")
m3=int("78")
print("Marks: 85, 92, 78")
a=m1+m2+m3
print("Total is:",a)
print("Average is:",a/3)

#Q16
print(bool(0))
print(bool(42))
print(bool(""))
print(bool("Hello"))
print(bool())

#Q17
name="rahul kumar"
roll=2024001
branch="computer science"
year=2024
print(f"=== STUDENT ID ===")
print("Name:",name.upper())
print("Roll:", roll)
print("Branch:", branch.title())
print("Year:", year)
print("===================")

#Q18
celsius=37.5
print("Celsus    :",celsius)
print("Fahrenheit:",(celsius*9)/5+32)

#Q19
name="Aman"
age="20"
print("My name is",name,"and I am",age,"years old")
print("My name is "+name+" and I am "+age+" years old")
print(f"My name is {name} and I am {age} years old")

#Q20
principal=10000
rate=7.5
time=2
interest=(principal*rate*time)/100
print("Principal:",principal)
print(f"Rate     :{rate}%")
print("Time     :",time,"years")
print(f"Interest : {interest:.2f}")
print(f"Total    : {principal+interest:.2f}")

### Completed ###