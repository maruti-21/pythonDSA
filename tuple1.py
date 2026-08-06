mytuple=("prashant","kumar",23,5.6,"python","komal","ankush")
print(mytuple)
print(type(mytuple))
print(mytuple[0])
print(mytuple[1])
print(mytuple[3])
# mytuple[2]="sunil" # it will give error because tuple is immutable
print(mytuple)

init_tuple=()
print(init_tuple.__len__())
# result =0
# print(init_tuple[0]) # it will give error because tuple is empty
# init_tuple=(type(init_tuple),)
# print(init_tuple)


init_tuple_a='a','b'
iniy_tuple_b=('a','b')
print(init_tuple_a==iniy_tuple_b) # it will give true because both are tuple and have same value
print(type(init_tuple_a)) # it will give <class 'tuple'>    
print(id(init_tuple_a)) # it will give the memory address of the tuple
print(id(iniy_tuple_b)) # it will give the memory address of the tuple

# new mcq
init_tuple_a='1','2'
iniy_tuple_b=('3','4')
print(init_tuple_a+iniy_tuple_b) # it will give false because both are tuple but have different value


init_tuple=('python',)*3
print(type(init_tuple)) # it will give 'pythonpythonpython' because it will repeat the string 3 times

# 
init_tuble=(1,)*3
init_tuple[0]=2 # it will give error because tuple is immutable
print(init_tuple)

init_tuple=((1,2),)*7
print(len(init_tuple[3:8])) # it will give 7 because it will repeat the tuple (1,2) 7 times


