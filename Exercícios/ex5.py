#Pintando a parede

largura = float(input("Largura: "))
altura = float(input("altura: "))
area = largura * altura
tinta = area / 2

print(f"A área do terreno {largura} x {altura} é de {area}m²")
print(f"Para pintar esse terreno, você precisará de {tinta}L de tinta")
