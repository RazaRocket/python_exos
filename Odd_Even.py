# Odd or Even
nombre = int(input("Entrer un chiffre: "))

def parité(i):
  if i % 4 == 0:
    return("ce nombre est un multiple de 4")
  elif i % 2 == 0:
    return("ce nombre est pair")
  else:
    return("ce nombre n'est pas pair")

print(parité(nombre)) 


num =int(input("Entrer un 1er nombre: "))
check = int(input("Entrer un 2nd nombre: "))

def verif(a,b):
  if a % b == 0:
    return("Ce sont deux nombres divisibles")
  else:
    return("Ils ne sont pas divisibles entre eux")
  
print(verif(num,check))
