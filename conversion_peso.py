libra_kilo = 2.2046 

# Vamos a escribir un programa que haga conerviones 
peso = float(input("Dame el valor del peso en Kg: "))

# 1Kg = 2.2046 lb
peso_libras = peso * libra_kilo 

print("El valor del peso expresado en Kg es: " ,  peso)
print("El valor del peso expresado en lb es: " ,  peso_libras)

peso_auto = float(input("Dame el valor del peso del auto en Kg: "))
peso_auto_libras = peso_auto * libra_kilo 

print("El valor del peso del auto expresado en Kg es: " ,  peso_auto)
print("El valor del peso del auto expresado en lb es: " ,  peso_auto_libras)