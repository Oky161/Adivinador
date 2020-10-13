import random

N1, N2 = 1, 50
r = [N1, N2]
intentos = 4

print(f"Pensa un numero entre {N1} y {N2} \n")


for _ in range(intentos):
	temp = input(f"Tu numero es mayor o igual a {int((r[0]+r[1])/2)}(Y/N)")
	if temp == "Y":
		r = [int((r[0]+r[1])/2), int(r[1])]
	else:
		r = [int(r[0]), int((r[0]+r[1])/2)]

if input(f"Tu numero es {random.randint(r[0], r[1])}? (Y/N)") == "Y":
	print("ggez")
else:
	print("rip...")
