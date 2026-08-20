class new:
    a=10
    # b=3456
    def __init__(self):
        self.name="prashant"
obj1=new()
obj2=new()
obj3=new()
print(obj1.a)
print(obj2.a)
print(obj3.a)
new.a=78
print(obj1.a)
print(obj2.a)
print(obj3.a)

