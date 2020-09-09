minhaTupla = ("Açai","Nutella","Leite Ninho")
print("Mostrar a tupla: ", minhaTupla)
print("Mostrar item em posição específica: ", minhaTupla[0])
print("Mostrar o último item da tupla: ", minhaTupla[-1])
print("Mostrar um intervalo de itens: ", minhaTupla[1:2])

listaClandestina = list(minhaTupla)
print("Lista clandestina: ", listaClandestina)
listaClandestina[2] = "Leite Condensado"
print("Lista clandestina com dado alterado: ", listaClandestina)

minhaTupla = tuple(listaClandestina)