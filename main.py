from functools import reduce 
import operator 

class Person:
    _name : str
    _address : str
    def __init__(self,name, address):
        self._name = name
        self._address = address
    def getName(self):
        return self._name
    def setName(self,name):
        self._name = name
        return True
    def getAddress(self):
        return self._address
    def setAddress(self,address):
        self._address = address
        return True
    def __str__(self):
        return str(self._name) +" "+ str(self._address)
    def __del__(self):
        print("i have been deleted")
class Employee(Person):
    number : int
    salary : float
    __jobTitle : str
    __loans : list
    def __init__(self,name,address,number,salary,jobTitle,loan):
        self.number = number
        self.salary = salary
        self.__jobTitle = jobTitle
        self.__loans = loan
        super().__init__(name,address)
    def getLoans(self):
        return self.__loans
    def getSalary(self):
        return self.salary
    def setSalary(self,salary):
        self.salary = salary
        return True
    def getJobTitle(self):
        return self.__jobTitle
    def setJobTitle(self,jobTitle):
        self.__jobTitle = jobTitle
        return True
    def geTotalLoan(self):
        return reduce(operator.add,self.__loans)
    def geMaxLoan(self):
        return  max(self.__loans)
    def getMinLoan(self):
        return min(self.__loans)
    def setLoans(self,loan):
        self.__loans = loan
        return True
    def __str__(self):
        return super().__str__()+ " " + str(self.number)+ " " +  str(self.salary)+ " " + self.__jobTitle+ " " + str(self.__loans)
    def __del__(self):
        print("i have been deleted")
class Student(Person):
    studentNumber : int 
    __subject : str
    __marks : dict
    def __init__(self, name, address,studentNumber , subject,mark):
        self.studentNumber = studentNumber
        self.__subject = subject
        self.__marks = mark
        super().__init__(name, address)
    def getSubject(self):
        return self.__subject
    def setSubject(self,subject):
        self.__subject = subject
    def getMarks(self):
        return self.__marks
    def setMarks(self,marks):
        self.__marks = marks
        return True
    def getAverage(self):
        sum = 0
        for key , value in self.__marks.items():
            sum += value
        return sum / len(self.__marks)
    def getAmarks(self):
        output = " "
        for key ,mark in self.__marks.items():
            if(mark >= 90):
                output += str(key) + " " +str(mark)  + " "
        return output
    def __str__(self):
        return super().__str__()+ " " + str(self.studentNumber)+ " " + str(self. __subject)+ " " + str(self.__marks)+ " " + str(self.getAverage())
    def __del__(self):
        print("i have been deleted")


Employee1 = Employee("Ahmad yazan","Amman, Jordan",100,500,"HR consultant",[434,200,1020])
print(Employee1)
Employee2 = Employee("Hala Rana","Aqaba, Jordan",2000,750,"department manager",[150,3000,250])
print(Employee2)
Employee3 = Employee("Mariam Ali","Mafraq, Jordan",600,750,"HR s consultant",[300,2000,300,250,500,235])
print(Employee3)

Student1 = Student("Kalid Ali","Irbid Jordan",20109100,"History", {
  "English": 100,
  "Arabic": 90,
  "Art": 95
  } )
print(Student1)
Student2 = Student("Reem Hani","Zarqa Jordan",20109100,"software eng.", {
  "English": 80,
  "Arabic": 90,
  "Art": 75,
  "pro": 90,
  "os": 73,
  "calc" : 85
  } )
print(Student2)
Student3 = Student("nawras abdulla","Amman Jordan",20109100,"History", {
  "English": 100,
  "Arabic": 90,
  "Art": 95
  } )
print(Student3)
Student4 = Student("Amal Raed","Tafila Jordan",20109100,"software eng.", {
  "English": 80,
  "Arabic": 90,
  "Art": 75,
  "pro": 90,
  "os": 73,
  "calc" : 91
  } )
print(Student4)

# 1
EmployeeList = [Employee1,Employee2,Employee3]
# 2
StudentList = [Student1,Student2,Student3,Student4]
# 3
for num in EmployeeList:
    print(num.number)
# 4
for num in StudentList:
    print(num.studentNumber)
# 5
for emp in EmployeeList:
    print(emp)
# 6
for stud in StudentList:
    print(stud ,"AVG", stud.getAverage())
# 7
stArr = []
for stud in StudentList:
    stArr.append(stud.getAverage())
print(max(stArr))
# 8
empArr = []
for emp in EmployeeList:
   print(emp.geMaxLoan())
# 9
for emp in EmployeeList:
   print(emp.getMinLoan())
# 10
for emp in EmployeeList:
   print(emp.geTotalLoan())
# 11
dicOfLoans = []
for emp in EmployeeList:
    dicOfLoans = {
        str(emp.number) : emp.getLoans()
    }
print(dicOfLoans)
# 12
totalloan = []
for loan in EmployeeList:
    totalloan.append(loan.geTotalLoan())
print(min(totalloan))
print(max(totalloan))
# 13 
for stud in StudentList:
   print(stud.getAmarks())

# 14
empSalaries = []
for emp in EmployeeList:
    empSalaries.append(emp.salary)
print(max(empSalaries))
# 15 
print(min(empSalaries))
# 16
totalSalaries = 0
for salary in empSalaries:
    totalSalaries += salary
print(totalSalaries)
# 17
# del EmployeeList
# del StudentList
