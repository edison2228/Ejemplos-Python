'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print ("===> Calculo de Factura IVA<===")
fact = float(input("¿Ingrese el valor de la factura?"))
iva = (input("¿Ingrese el IVA?"))
def factura(total,iva):
    iva_float = float(iva)
    total_val = (total*iva_float)/100
    valor_total=total+total_val
 
    print(f"\nSubtotal",total,"\nIVA ",iva_float,"\nTotal ",{valor_total})
    

if iva == "":
  iva="12"
  print("¡El IVA sera 12%!") #esta sentencia no se ejecuta
   
else:
  print("¡El IVA sera el ingresado!") #esta sentencia no se ejecuta
    
factura(fact,iva)
