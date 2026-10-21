#Q1
a = "Aman"
b = 19
c = "Lucknow"
d = "Blue"
print(f" Name: {a} ")
print(f" Age: {b} ")
print(f" City: {c} ")
print(f" Color: {d} ")

#Q2
item_name = "Burger"
price = 149.99
quantity = 3
Subtotal = price * quantity
GST = (Subtotal * 18) / 100
Total = Subtotal + GST
print(f" Item: {item_name} ")
print(f" Price: {price} ")
print(f" Qty: {quantity} ")
print(f" Subtotal: {Subtotal} ")
print(f" GST: {GST} ")
print(f" Total: {Total} ")

#Q3
radius = 7
area = 3.14159 * 7 * 7
circumf = 2 * 3.14159 * 7
print(f" Radius: {radius} ")
print(f" Area: {area} ")
print(f" Circumference: {circumf} ")

#Q4
first_name = "Rahul"
last_name = "Verma"
year = 2024
x = first_name[:4].lower()
y = last_name[3:].lower()
z = str(year)[2:].lower()
print(f" Generated Email {x+y+z}@sitara.edu")

#Q5
a = "Hello, World! Welcome to Python"
print("Original:", a)
print(a.upper())
print(a.lower())
print(len(a))
print(a.count("o"))
print(a[:6])
print(a[-6:])

#Q6
Celsius = 37.5
print(f" {Celsius} C = {Celsius * 9/5 + 32} F")
print(f" {Celsius} C = {Celsius + 273.15} K")

#Q7
Princi = 50000
rate = 8.5
time = 3
Interest = (Princi * rate * time) / 100
Total = Interest + Princi
print("Principal:", Princi)
print("Rate:", rate, "%")
print("Time:", time)
print("Interest:", Interest)
print("Total:", Total)
print("########################## Q7")

#Q8
Pen, Notebook, Eraser = 30, 120, 25                                                                                                                                                                                                                  
print(f"Pen      x3 Rs{Pen}")
print(f"Notebook x2 Rs{Notebook}")
print(f"Eraser   x5 Rs{Eraser}")
print("---------------------")
print(f"TOTAL       Rs{Pen+Notebook+Eraser}")
print("########################## Q8")

#Q9
a = "I like Java and Java is great"
print(a)
print(a.replace("Java", "Python"))
print(a.count("Java"))

#Q10
num = 9876
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
total = a + b + c + d
print("Number:", num)
print("Thousands:", a)
print("Hundreds:", b)
print("Tens:", c)
print("Units:", d)
print("Sum:", total)

#Q11
value = "256"
print(type(value))
print(type(int(value)))
print(type(float(value)))
print(type(bool(value)))
print(type(str(value)))

#Q12
name = "Ravi Shankar"
roll = 2024056
branch = "electrical engineering"
a=name[:2].upper()
b=str(roll)[4:7]
c=(branch)[:1].upper()+(branch)[11:12].upper()
#c=(branch.split()[0][0]+branch.split()[1][0]).upper()
d=list(name.replace(" ",""))
e=len(d)
print(f"Code:{a}{b}-{c}-{e}")

#13
a = "5"
b = 3
c = float(b)
d = str(b) + a
e = int(a) + b
f = bool(a)

print(f"a = {a} | type: str")
print(f"b = {b} | type: int")
print(f"c = {c} | type: float")
print(f"d = {d} | type: str")
print(f"e = {e} | type: int")
print(f"f = {f} | type: bool")

#Q14
data = " NAME:rahul kumar;ROLL:2024007;BRANCH:computer science;CGPA:8.75 "
a=data.strip().split(";")
print(a)
name=a[0].title()
roll=a[1]
branch=a[2].split(":")[1].strip().upper()
cgpa=float(a[3].split(":")[1].strip())
print("+---------------------+")
print(f"| {name}   |")
print(f"| {roll}       |")
print(f"| BRANCH:{branch[:11]} |")
print(f"| CGPA: {cgpa:.1f}          |")
print("+---------------------+")
