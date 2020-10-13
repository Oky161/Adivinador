import random
print("Pensa un numero entre 1 y 80")
print("")
temp = input("Tu numero es mayor que 40? (Y/N)")
if temp == "Y":
	temp = input("Tu numero es mayor que 60? (Y/N)")
	if temp == ("Y"):
		print("Tu numero es: "+str(random.randint(60,80)))
	else:
		print("Tu numero es: "+str(random.randint(40,60)))
else:
	temp = input("Tu numero es mayor que 20? (Y/N)")
	if temp == ("Y"):
		print("Tu numero es: "+str(random.randint(20,40)))
	else:
		print("Tu numero es: "+str(random.randint(1,20)))
print("(La empresa no se hace cargo si no sale tu numero)")


