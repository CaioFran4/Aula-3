tipo = str(input("O seu número é par ou impar? (somente par ou impar)")).strip().lower
par = tipo in ["par","Par"]
impar = tipo in ["impar","Impar"]
Quantidade = int(input("Qual a quantidade de números?: "))




contador = 1
while (contador <= Quantidade):
    if par:
     par % 2 == 0
    resultado = tipo * contador
    print(f"{Quantidade} X {contador} = {resultado}")
    contador = contador + 1
   
    
    