# List Questions.
print("List Questions:")
#Q1
fruits=["apple","banana","cherry"]
fruits.append("mango")
print(fruits)

#Q2
num=[10,20,30,40,50]
print(num[0],num[4])

#Q3
color=["red","green","blue"]
color.insert(1,"yellow")
print(color)

#Q4
items=[5,3,8,1]
items.sort()
print(items)

#Q5
letters=["a","b","c","d"]
letters.remove("c")
print(letters)

#Q6
num=[1,2,3,4,5,6,7,8]
print(num[2:5])

#Q7
num=[4,8,15,16,23,42]
print(len(num),sum(num),max(num),min(num))

#Q8
data=[1,2,3]
a=data.pop(2)
print(a,data)

#Q9
a=[1,2]
b=[3,4]
c=a+b
print(c)

#Q10
words=["to","be","or","not","to","be"]
print(words.count("be"))
print(words.index("or"))

## Tuple Questions.
print("Tuple Questions: ")

#Q1
point=(3,7)
x,y=(3,7)
print("x =",x,"y =",y)

#Q2
t=(10,20,30,40)
print(t[1], t[3])

#Q3
a=(1,2)
b=(3,4)
c=a+b
print(c)

#Q4
t=(1,2,3)
print(t*2)

#Q5
t=(1,2,3,4,5)
print(t[1:4])

#Q6
t=(5,3,5,1,5)
print(t.count(5),t.index(3))

#Q7
t=(4,9,2,7)
print(len(t),max(t),min(t),sum(t))

#Q8
a="10"
b="20"
a,b=b,a
print(a,b)

#Q9
student=("Aman",21,"CSE")
name,age,branch=("Aman",21,"CSE")
print(f"My name is {name}, i am {age} years old and my branch is {branch}.")

#Q10
t=("a","b","c")
a=list(t)
a.append("d")
b=tuple(t)
print(t,b)

# Set Questions.
print("Set Questions: ")

#Q1
s={1,2,3}
s.add(4)
print(sorted(s))

#Q2
nums=[1,2,2,3,3,3,4]
a=set(nums)
print(len(a))

#Q3
a={1,2,3,4}
b={3,4,5,6}
x=a.union(b)
print(sorted(x))

#Q4
s={"a","b","c"}
print("b" in s, "z" in s)

#Q5
a={1,2,3,4}
b={3,4,5,6}
x=a.intersection(b)
print(sorted(x))

#Q6
a={1,2,3,4}
b={3,4,5,6}
x=a.difference(b)
print(sorted(x))

#Q7
a={1,2,3,4}
b={3,4,5,6}
x=a.symmetric_difference(b)
print(sorted(x))

#Q8
s={1,2,3,4}
s.remove(3)
s.discard(10)
print(sorted(s))

#Q9
a={1,2}
b={1,2,3,4}
x=a.issubset(b)
y=b.issuperset(a)
print(x,y)

#Q10
s={5,10,15}
s.update([15,20,25])
print(sorted(s),len(s))

# Dictionary Questions.
print("Dictionary Questions:")

#Q1
student={"name":"riya","age":20}
print(student["name"])

#Q2
student={"name":"riya","age":20}
student["marks"]=88
print(student)

#Q3
d={"a":1,"b":2}
d["b"]=20
print(d)

#Q4
d={"a":1,"b":2}
print("a" in d, "c" in d)

#Q5
prices={"pen":10,"book":40}
print(prices.get("bag",0))

#Q6
d={"x":1,"y":2,"z":3}
a=d.pop("y")
print(a,d)

#Q7
d={"a":1,"b":2,"c":3}
print(list(d.keys()))
print(list(d.values()))

#Q8
d1={"a":1,"b":2}
d2={"b":3,"c":4}
d1.update(d2)
print(d1)

#Q9
marks={"Math":78,"Science":92,"English":85}
print(max(marks))

#Q10
keys=["a","b","c"]
values=[1,2,3]
print(dict(zip(keys,values))) # zip()= You use zip() here to combine the two separate lists—keys and values—into pairs of (key, value) tuples, which dict() then converts into a dictionary {'a': 1, 'b': 2, 'c': 3}

# Condition Questions.
print("Condition Questions: ")

#Q1
num=7
if num//2==0:
    print("Even")
else:
    print("Odd")

#Q2
age=16
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible")

#Q3
temp=35
if temp>30:
    print("Hot outside")
elif temp<=30 and temp>=20:
    print("Warm")
else:
    print("Cold")

#Q4
num=-5
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#Q5
a=15
b=22
c=9
print(max(a,b,c))

#Q6
marks=82
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif num>=50:
    print("C")
else:
    print("F")

#Q7
year=2024
if year/4==0 and year/100 !=0 or year/400==0:
    print("Leap year")
else:
    print("Not a leap year")

#Q8
usrnm="admin"
pswrd="1234"
if usrnm=="admin" and pswrd=="1234":
    print("Login sucessful")
else:
    print("Login Failed")

#Q9
units=250
if units<=100:
    print("Bill:",100*5)
elif units>=101 and units<=200:
    print("Bill:",100*5+(units-100)*7)
elif units>200:
    print("Bill:",100*5+100*7+(units-200)*10)


#Q10
a=5
b=5
c=8
if a+b>c or a<b+c:
    print("Valid")
else:
    print("Invalid")

if a==b==c:
    print("Equilateral triangle")
elif a==b!=c or a!=b==c:
        print("Isosceles triangle")
else:
    print("Scalene Triangle")



#While Loop:
print("While Loop Questions: ")

#Q1
# a=1
# while a<=5:
#     print(a)
#     a+=1

# #Q2
# a=1
# total=0
# while a<=10:
#     total+=a
#     a+=1
# print("Sum:",total)

# #Q3
# i=5
# while i>=1:
#     print(i)
#     i-=1
# print("Liftoff!")

# #Q4
# a=10
# b=7
# while a>=10:
#     a+=1
# print(a*b)

##############
# i=int(input("enter number: "))
# while(i<=38):
#     i=int(input("enter number: "))
#     print(i)
# print("Done with loop")
# #############
# count=5
# while count>0:
#     count=count-1
# print(count)

#Q5
print("n=12345")


n=12345
count=0
while n>0:
    count+=1
    n//=10
print(f"Digits:{count}")
    
############
# count=1
# while count<=3:
#     print("No")
#     count+=1
# print("Hello World")


#Q6
n=4321
sum=0
while n>0:
    a=n%10
    n//=10
    sum+=a
print(sum)

#Q7
a=0
while a<10:
    a+=1
    if a%2==0:
        continue
    print(a)
#Q8
a=51
while True:
    if a%7==0:
        print(a)
        break
    a+=1

#Q9
n=1234
reverse=0
while n>0:
    last=n%10
    reverse=(reverse*10)+last
    n=n//10
print(reverse)

print("#########################")

#Q10
fib=[0,1]
while len(fib)<6:
    num=fib[-1]+fib[-2]
    fib.append(num)
print(fib)

# factorial
n=int(input("Enter a number: "))
factorial=1
i=1
while i <=n:
    factorial*=i
    i+=1
    continue
print(n,factorial)

limit=int(input("Enter for sum: "))
total=0
current=1
while current<=limit:
    total+=current
    current+=1

print(limit, total)

print("geometric progression:>")
# geometric progression
count=int(input("power of 2 to be generated: "))
powers=[]
exponent=0
while exponent<count:
    powers.append(2**exponent)
    exponent+=1
print(powers)