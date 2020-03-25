name=["faisal","safaan","virat","sohail","abd","bad","cat","dog"]
rollno=[1,2,3,4,5,6,7,8]
marks=[79,95,47,88,33,65,88,92]
stud=[["A+ grade"],["A grade"],["B grade"],["fail grade"]]
def addstudent(name,rollno,marks):
    
    new=input("enter new student name")
    new3=int(input("enter new student marks"))
    name.append(new)
    rollno.append(len(rollno)+1)
    marks.append(new3)
    
def ranking(name,marks):
    for i in range(len(name)):
        for j in range(len(name)):
                
            if marks[i]>marks[j]:
                name[i],name[j]=name[j],name[i]
                marks[i],marks[j]=marks[j],marks[i]
                rollno[i],rollno[j]=rollno[j],rollno[i]
    printrank(name,marks)
def printrank(name,marks):
    for i in range(len(name)):
        print(name[i],"scored ",i+1,"rank with marks",marks[i])
def deletestudent():
    give=input("select which student should be removed")
    
    for i in range(len(name)-1):
        if give==name[i]:
            
            name.pop(i)
            marks.pop(i)
            rollno.pop(i)
    
def group(name,marks):
    for i in range(len(name)):
        if marks[i]>=90:
            stud[0].append(name[i])
        elif marks[i]>=80 and marks[i]<90:
            stud[1].append(name[i])
        elif marks[i]>=65 and marks[i]<80:
            stud[2].append(name[i])
        else:
            stud[3].append(name[i])
    print(stud)
ranking(name,marks)
addstudent(name,rollno,marks)
ranking(name,marks)
deletestudent()
ranking(name,marks)
group(name,marks)
        
