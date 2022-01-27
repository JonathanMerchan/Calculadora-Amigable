""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular división: (4)")
  print("==================================================")
   
  opcion = input()
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion=int(menu_operaciones())

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
n1 = int (input("Ingrese el primer numero a operar \n"))
n2 = int (input("Ingrese el segundo numero a operar \n"))
op=""
r=""
if operacion == 1:
  r = calc.sumar_numeros(n1,n2)
  op = "SUMA"
elif operacion==2:
  r = calc.restar_numeros(n1,n2)
  op = "RESTA"
elif operacion==3:
  r = calc.multiplicar_numeros(n1,n2)
  op = "MULTIPLICACION"
elif operacion==4:
  if n2!=0:
    r = calc.dividir_numeros(n1,n2)
    op = "DIVISION"
  else:
    r="N/A"
    print("No se puede dividir por cero")

print(f"EL resultado de la {op} de {n1} y {n2} es {r} \n")


