print("Olá usuário, me diga a sua altura e seu peso que te direi se você está com um peso favorável.")

a = float(input ("Me fale a sua altura: "))
b = float(input("Me fale o seu peso: "))
conta = b / (a * a)

if   conta < 20:
    print("Seu estado atual é abaixo do peso, está em peso em excesso.")
    
elif conta >= 20 and a <= 24.9:
    print("Seu estado atual é de normalidade, pudinzinho!")
     
elif conta >= 25 and b <= 29.9:
 print("Seu estado atual é de sobre peso!")
    
elif conta >= 30 and a <= 39.9:
    print("Seu estado atual é de obesidade!")
    
elif conta >= 40:
    print("Seu estado atual é de magreza!")
