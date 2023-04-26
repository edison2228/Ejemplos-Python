'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print ("===> Factorial de un Numero<===")
num = float(input("¿Ingrese el numero?"))

def factorial(num): 
    if num < 0: 
        print("No existe el factorial de un numero negativo")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

 
print("Factorial de",num,"es ==>", factorial(num)) 
