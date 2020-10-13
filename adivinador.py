import random
print("Pensa un numero entre 1 y 20 \n")

temp = input("Tu numero es mayor que 10? (Y/N)").upper()
if temp == "Y":
	temp = input("Tu numero es mayor que 15? (Y/N)").upper()
	if temp == ("Y"):
		print("Tu numero es: "+str(random.randint(15,20)))
	else:
		print("Tu numero es: "+str(random.randint(10,15)))
else:
	temp = input("Tu numero es mayor que 5? (Y/N)").upper()
	if temp == ("Y"):
		print("Tu numero es: "+str(random.randint(5,10)))
	else:
		print("Tu numero es: "+str(random.randint(1,5)))
print("(La empresa no se hace cargo si no sale tu numero)")


