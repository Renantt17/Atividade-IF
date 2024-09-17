A = 1
B = 1

print("")
print("Atividade 1:")
A = int(input("Digite um valor para A, de preferencia 1 a 4: "))
if (A == 1) or (A == 2) or (A == 3) or (A == 4):
  print("A é 1, 2, 3 ou 4")

else:
  print("A não é 1, 2, 3 ou 4")


print("")
print("Atividade 2:")
if (A >= 1):
  print ("O valor da variavel A é Positivo")
  
elif (A < 0):
  print ("O valor da variavel A é Negativo")
  
else:
  print ("É zero")


print("")
print("Atividade 3:") 
VAR = input("Digite uma letra, A ou B: ")

if (VAR <= 'A'):
  AB = float(input("Digite o valor de AB: "))  
  if (AB >= 0):
    print("AB é positivo")
  else:
    ("AB é menor que Zero")

elif (VAR <= 'B'):
  AC = float(input("Digite o valor de AC: "))
  if (AC >= 0):
    print("AC é positivo")
  else:
    print("AC é menor que Zero")
else:
  print("Deu o karaio novamente")
  
