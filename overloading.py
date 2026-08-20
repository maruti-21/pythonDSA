# method overloading
class arithmatic():
    def add(self, *args):
        print(sum(args))

obj=arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(45,80,800)
