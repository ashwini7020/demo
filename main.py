print('good morning')
print(' how are you')

def factorial(num):
    if num<0:
        print("cant calculate factorial")
        return
    if num<=1:
        print("factorial is",1)
    fact=1
    for i in range(2,num+1):
        fact = fact*i
    print("the factorial is:",fact)
    return
factorial(5)
