#Q1
subjects = ["Math", "Physics"]
a=subjects.append("Chemistry")
b=subjects.append("Biology")
print(subjects)
print(len(subjects))

#Q2
subjects = ["Math", "Physics"]
electives = ["Art", "Music"]
subjects.append(electives)
print(subjects,(len(subjects)))
subjects = ["Math", "Physics"]
subjects.extend(electives)
print(electives,(len(electives)))

#Q3
subjects = ["Math", "Physics", "Chemistry"]
subjects.insert(1,"Biology")
subjects.insert(0,"English")
subjects.insert(100,"Computer")
print(subjects)

#Q4
marks = [85, 90, 78, 90, 88]
marks.remove(90)
marks.remove(78)
print(marks)
print(len(marks))

#Q5
subjects = ["Math", "Physics", "Chemistry", "Biology"]
subjects.pop()
subjects.pop(0)
subjects.pop(1)
print("Biology Math Cemistry")
print(subjects)
print(len(subjects))

#Q6
subjects = ["Math", "Physics", "Chemistry"]
a=subjects.copy()
subjects.clear()
print(subjects)
print(len(subjects))
print(a,len(a))

#Q7
a = ["Math", "Physics"]
b=a
c=a.copy()
b.append("Chemistry")
c.append("Biology")
print(a)
print(b)
print(c)
print(a is b, a is c)

#Q8
marks = [85, 90, 78, 90, 88, 90]
a=marks.count(90)
print(a)
print(marks.count(100))
b=(len(marks))
print((a * 100)//b)

#Q9
marks = [85, 90, 78, 90, 88, 90]
print(marks.index(90))
print(marks.index(90,2))
print(marks.index(90,4))

#Q10
subjects = ["Math", "Physics", "Chemistry"]
a=(subjects[::-1])
print(a)
print(a[::-1])

#Q11
marks = [85, 90, 78, 92, 88]
marks.sort()
print(marks)
marks.reverse()
print(marks)
print(marks.clear())

#Q12
names= ["Priya", "aman", "Rahul", "neha", "Om"]
names.sort()
print(names)
names.sort(key=str.lower)
print(names)
names.sort(key=len)
print(names)

#Q13
marks = [85, 90, 78, 92]
print(sorted(marks, reverse=True))
print(marks)
marks.sort(reverse=True)
print(marks)

#Q14
subjects = ["Math", "Physics"]
subjects.append("Chemistry")
subjects.insert(1,"Biology")
subjects.extend(["English", "History"])
subjects.remove("Physics")
a=subjects.pop(4)
b=subjects.pop(0)
print(subjects)
print(a,b,len(subjects))

#Q15
marks = [85, 90, 78, 92, 88]
a=marks.copy()
a.sort(reverse=True)
print(a)
print(a[0:3], a.index(88))

#Q16
semesters = ("Fall", "Winter", "Spring", "Summer")
print(len(semesters))
print(type(semesters))
print(semesters[:1], semesters[3:])
print("Winter" in semesters, "Monsoon" in semesters)

#Q17
days = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
print(days[:3])
print(days[5:])
print(days[2:5])
print(days[::-1])
print(days[::2])

#Q18
marks = (85, 90, 78, 90, 88, 90)
a=marks.count(90)
print(a)
print(marks.count(100))
b=len(marks)
print(a * 100 // b)

#Q19
marks = (85, 90, 78, 90, 88, 90)
print(marks.index(90))
print(marks.index(90,2))
print(marks.index(90,5))

#Q20
days = ("Mon", "Tue", "Wed")
print(days+("Thu","Fri"))
print(days*2)
print(days+("Sat",))
print(len(days*3))

#Q21
x = ("Fall")
y = ("Fall",)
z = tuple("Fall")
print(type(x), len(x))
print(type(y), len(y))
print(tuple(x), len(x))

#Q22
record = ("Aman", 20, "CSE", 8.7)
name, age, branch, cgpa = record
print(name, age, branch, cgpa)
name,branch = branch,name
print(name,branch)

#Q23
semesters = ("Fall", "Winter", "Spring")
a=list(semesters)
a[1]="Autumn"
a.remove("Spring")
a.append("Summer")
semesters=tuple(a)
print(semesters, len(semesters))

#Q24
students = (("Aman", 88), ("Priya", 92), ("Rahul", 75))
print(students[1][0], students[1][1])
print(students[2][1])
a=students[0:2]+(("Neha", 95),)
print(a)
print(len(a),a[2][1])

#Q25
marks = (85, 90, 78, 92, 88)
print(min(marks),max(marks),sum(marks))
print(sum(marks)/len(marks))
print(sorted(marks))
print(tuple(sorted(marks, reverse=True)))

#Q26
marks=(85,90,78,90,85)
pairs=(("Aman",88),("Priya",92))
a=list(marks)
a.append(95)
print(tuple(a))
print(sorted(marks[:3]))
b=dict(pairs)
print(b)

#Q27
seats = {}
seats[(1, "A")] = "Aman"
seats[(1, "B")] = "Priya"
seats[(2, "A")] = "Rahul"
print(seats)
print(seats[(1, "B")], len(seats))
print(sorted(seats))

#Q28
classes = {"CS101", "CS102", "CS103", "CS101"}
print(len(classes), type(classes))
print("CS102" in classes, "CS104" is not classes)
print(sorted(classes))

#Q29
classes = {"CS101", "CS102"}
print(classes.add("CS103"))
print(classes.add("CS101"))
print(sorted(classes), len(classes))

#Q30
classes = {"CS101"}
letters = set()
classes.update(["CS102","CS103"])
classes.update({"CS104", "CS102"})
print(sorted(classes), len(classes))
letters.update("abc")
print(sorted(letters))

#Q31
classes = {"CS101", "CS102", "CS103"}
classes.remove("CS102")
classes.discard("CS999")
classes.discard("CS103")
print(sorted(classes), len(classes))

#Q32
nums = {1, 2, 3, 4, 5}
x=nums.pop()
print(x)
print(sorted(nums), len(nums))
print("q32")

#Q33
classes = {"CS101", "CS102", "CS103"}
a=classes.copy()
classes.clear()
print(set(classes), len(classes))
print(sorted(a), len(a))

#Q34
a = {"CS101", "CS102"}
alias = a 
duplicate = a.copy()
alias.add("CS103")
duplicate.add("CS999")
print(sorted(a))
print(sorted(duplicate))
print(a is alias, a is duplicate)

#Q35
morning = {"Aman", "Priya"}
evening = {"Priya", "Karan"}
print(sorted(morning.union(evening)))
print(sorted(morning|evening))
print(sorted(morning.union(["Neha", "Aman"])))
print(sorted(morning))

#Q36
morning = {"Aman", "Priya", "Rahul"}
evening = {"Priya", "Rahul", "Karan"}
print(sorted(morning.intersection(evening)))
print(sorted(morning & evening))
print(len(morning & evening))

#Q37
morning = {"Aman", "Priya", "Rahul"}
evening = {"Priya", "Karan"}
print(sorted(morning.difference(evening)))
print(sorted(evening.difference(morning)))
print(sorted(morning-evening), sorted(evening-morning))

#Q38
day1 = {"Aman", "Priya", "Rahul"}
day2 = {"Priya", "Karan"}
print(sorted(day1.symmetric_difference(day2)))
z=sorted(day1^day2)
print(z)
print(len(z))

#Q39
club = {"Aman", "Priya"}
batch = {"Aman", "Priya", "Rahul", "Neha"}
guests = {"Karan"}
print(club.issubset(batch))
print(batch.issuperset(club))
print(club.isdisjoint(guests))
print(club <= batch, batch >= club)

#Q40
a = {"CS101", "CS102"}
b = {"CS102", "CS103"}
print(sorted(a.union(b)), sorted(a))
a.update(b)
print(sorted(a), len(a))

#Q41
enrolled = {"Aman", "Priya", "Rahul"}
attended = {"Priya", "Rahul", "Karan"}
a=sorted(enrolled.intersection(attended))
print(a, len(a))
print(sorted(attended))

#Q42
enrolled = {"Aman", "Priya", "Rahul"}
dropped = {"Priya"}
a=sorted(enrolled.difference(dropped))
print(a, len(a))
print(sorted(enrolled.intersection(dropped)))

#Q43
day1 = {"Aman", "Priya", "Rahul"}
day2 = {"Priya", "Karan"}
a=sorted(day1.symmetric_difference(day2))
print(a, len(a))
print(sorted(day2))

#Q44
rolls = [101, 105, 101, 107, 105, 109, 101]
a=set(rolls)
print(len(a))
print(len(rolls)-len(a))
b=sorted(a)
print(b[:3])

#Q45
math_set = {"Aman", "Priya", "Rahul"}
physics_set = {"Priya", "Rahul", "Karan"}
chem_set = {"Priya", "Neha"}
print(sorted(math_set.intersection(physics_set).intersection(chem_set)))
print(len(math_set.union(physics_set).union(chem_set)))
print(sorted((math_set-physics_set-chem_set)
         |(physics_set-chem_set-math_set)
         |(chem_set-math_set-physics_set)))

#Q46
student = {"name": "Aman", "roll_no": 101, "branch": "CSE"}
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(student.items())

#Q47
student = {"name": "Aman", "branch": "CSE"}
print(student.get("branch"))
print(student.get("cgpa"))
print(student.get("cgpa","Not Available"))
print(student, len(student))

#Q48
student = {"name": "Aman", "cgpa": 8.7}
print(student.setdefault("cgpa",0.0))
print(student.setdefault("hostel","Block A"))
print(student)

#Q49
student = {"name": "Aman", "cgpa": 8.7}
student.update({"cgpa":9.1,"branch":"CSE"})
print(student)
student.update({"hostel":"Block A","cgpa":9.5})
print(student, len(student))

#Q50
student = {"name": "Aman", "roll_no": 101, "branch": "CSE"}
print(student.pop("roll_no"))
print(student.pop("cgpa","No such keys"))
print(student, len(student))

#Q51
student = {"name": "Aman", "roll_no": 101, "branch": "CSE"}
print(student.popitem())
print(student.popitem())
print(student,len(student))

#Q52
student = {"name": "Aman", "roll_no": 101}
a=student.copy()
b=student.clear()
print(student, len(student))
print(a, len(a))

#Q53
marks = {"Math": 90, "Physics": 78}
alias = marks
duplicate = marks.copy()
alias["Chemistry"]=92
duplicate["English"]=85
print(marks)
print(duplicate)
print(marks is alias, marks is duplicate)

#Q54
subjects = ["Math", "Physics", "Chemistry"]
a=dict.fromkeys(subjects,0)
print(a)
b=dict.fromkeys(subjects)
print(b)
print(len(a),list(a.keys()))

#Q55
shared = dict.fromkeys(["Aman", "Priya"], [])
shared["Aman"].append(88)
print(shared)
a={"Aman":[],"Priya":[]}
a["Aman"].append(88)
print(a)
# The difference is that it didn't create list 2 for Priya.

#Q56
student = {"name": "Aman", "roll_no": 101}
k = student.keys()
v = student.values()
print(list(k),list(v))
student["cgpa"] = 8.7
print(list(k), list(v))
print(len(student))

#Q57
student = {"name": "Aman"}
student.update({"roll_no": 101, "branch": "CSE"})
student.setdefault("cgpa",8.7)
student.setdefault("branch","ECE")
removed=student.pop("roll_no")
print(student)
print(removed, len(student))
print(list(student.keys()), list(student.values()))

#Q58 
marks = {"Aman": [88, 92]}
marks["Aman"].append(79)
marks.setdefault("Priya",[]).append(95)
print(marks)
print(len(marks["Aman"]), sum(marks["Aman"]))
print(marks.get("Rahul",[]))

#Q59
records = [{"name": "Aman", "cgpa": 8.7}, {"name": "Priya", "cgpa": 9.1}]
print(records[1]["name"])
records[0].update({"cgpa":8.9,"branch":"CSE"})
print(records[0])
records.append({"name":"Rahul","cgpa":7.5})
print(len(records), records[-1].get("branch","No Set"))

#Q60
subjects = ["Math", "Physics", "Chemistry"]
register=dict.fromkeys(subjects,0)
register.update({"Math":42,"Physics":38})
register["Chemistry"]=45
print(register)
print(sum(register.values()),max(register,key=register.get))
print(sorted(register.items()))
