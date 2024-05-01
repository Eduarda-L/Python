#calcular a media

n1 = float(input("primeira nota do aluno: "))
n2 = float(input("segunda nota do aluno: "))
m = (n1 + n2) / 2
print("A media entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1, n2, m))

#string (input) na função float, faz com que seja convertida para número flutuante
#.1f é para arredondar o número para 1 casa decimal
#.format é para formatar o número

#calculadora de cm/mm (p/implementações)

medida = float(input("uma distancia em metros: "))
cm = medida * 100
mm = medida * 1000
print("a medida de {}m corresponde a {:.0f}cm e \n{:.0f}mm".format(medida, cm, mm))