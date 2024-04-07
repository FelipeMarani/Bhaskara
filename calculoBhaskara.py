import math
a, b, c = map(int, input("digite três numeros seguidos para os valores a, b e c: ").split())
dlt = (b**2) - (4 * a * c)
print(f"Valor de delta é {dlt}")
if dlt < 0:
    print(f"Não possui raiz real")  
elif dlt == 0:
    print("Possui uma das raízes iguais a 0.00")
else:
    x1 = (-(b) + math.sqrt(dlt)) / (2*a)
    x2 = (-(b) - math.sqrt(dlt)) / (2*a)
    print(f"Possui duas raizes sendo x1=  {x1:.2f} e x2= {x2:.2f}")


