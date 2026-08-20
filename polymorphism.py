# having many forms
# we can define polymorphism as the abillity of a msg to be displayed in more than one following
# eg. a person in real world can perform many task at aa time like at the sametime eat, play, watch, etc
class principal:
    def role(self):
        print("I am managing the college")
        
class hod:
    def role(self):
        print("i am managinig the teacher and students")
        
class teacher:
    def role(self):
        print("i am mamnaging the sullyabus")
        
def func(obj):
    obj.role()
campus=[principal(),hod(),teacher()]
for obj in campus:
    
    func(obj)
     