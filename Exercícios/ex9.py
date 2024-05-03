# Aluguel de carros

n1 = float(input("quantos dias alugados? "))
n2 = float(input("quantos km rodados? ")) 
dia = 20
km = 10
res = dia * n1 + km * n2
print("o total a pagar é de R${:.2f}".format(res))