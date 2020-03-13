class Student:
    s_name = input("Enter name of the student: ")
    s_roll_no = input("ENter the roll no of the student:")
    s_class = input("Enter the class of the studnet:")
    subjects = [['oop theory','oop practical','oop internal'],['dm theory','dm practical','oop internal']['wp theory','wp practical','wp internal']['pp theory','pp practical','pp internal']['dbms theory','dbms practical','dbms internal'],['it tools practials','it tools internals']]
    marks = []
    for i in subjects:
        marks.append(sum(list(map(int(input(f"Enter marks of {i[0],i[1],i[2]}").rstrip().split())))))

    def total_marks(self):
        print(sum(Student.marks))
    def percentage_of_total_marks(self):
        print(sum(Student.marks)/850 * 100)