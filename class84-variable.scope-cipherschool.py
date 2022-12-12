# def func():
#     x=7  #local variable
#     return x
# def func2():
#     print(x)
# func2()  no output


# x=5  #global
# def func():
#     x=7  #local variable
#     return x
# print(x)
# print(func())



x=5  #global
def func():
    global x #local to global 
    x=7  #local variable
    return x
print(x)  
print(func()) 
print(x)
#output 577