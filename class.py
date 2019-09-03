class student:
    sum1=0
    def marks(self):
        self.a=int(input("\nEnter CIE marks\n"))
        self.b=int(input("\nEnter SEE marks\n"))
        self.sum1=self.a+self.b
    def display(self):
        return self.sum1


s1=student()
s1.marks()
print("\nStudent Info 1:\n")
x=s1.display()
print("\n")
print(x)
s2=student()
s2.marks()
print("\nStudent Info 2:\n")
y=s2.display()
print(y)
print("\n\n\n")


if x>y:
    print("Student 1 is topper")
else:
    print("Student 2 is topper")




