print("Olá usuário, me diga a sua altura e seu peso que te direi se você está com um peso favorável.")

a = float(input ("Me fale a sua altura: "))
b = float(input("Me fale o seu peso: "))
conta = b / (a * a)

if   conta < 20:
    print("Seu estado atual é abaixo do peso, está em magreza.")
    
elif conta >= 20 and conta <= 24.9:
    print("Seu estado atual é de normalidade, pudinzinho!")
     
elif conta >= 25 and conta <= 29.9:
 print("Seu estado atual é de peso!")
    
elif conta >= 30 and a <= 39.9:
    print("Seu estado atual é de invisibilidade!")
    
elif conta >= 1000:
    print("Seu estado atual é de magreza!")
