class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, member_t, name, age):
        self.member_t = member_t
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Member_t:"{}" Name:"{}" Age:"{}"'.format(self.member_t, self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, member_t, name, age, salary):
        SchoolMember.__init__(self, member_t, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self,member_t, name, age, marks):
        SchoolMember.__init__(self, member_t, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))



class Headmaster(SchoolMember):
   '''Represents a headmaster.'''
   def __init__(self, member_t, name, age, experience):
        SchoolMember.__init__(self, member_t, name, age)
        self.experience = experience
        print('(Initialized Headmaster: {})'.format(self.name))

   def tell(self):
        SchoolMember.tell(self)
        print('Experience: "{:d}" yrs'.format(self.experience))


t = Teacher('teacher','Mrs. Shrividya', 40, 30000)
s = Student('student','Swaroop', 25, 75)
h = Headmaster('headmaster', 'jankro', 60, 8)
# prints a blank line
print()
print('the member_t refers to the member type')
members = [t, s, h]
for member in members:
    # Works for both Teachers and Students
    member.tell()
    print()
