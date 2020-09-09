minhaTupla = ("Açai","Nutella","Leite Ninho","tupla")
print("Mostrar a tupla: ", minhaTupla)
print("Mostrar item em posição específica: ", minhaTupla[0])
print("Mostrar o último item da tupla: ", minhaTupla[-1])
print("Mostrar um intervalo de itens: ", minhaTupla[1:2])

#Burlando alteração de dados na tupla
listaClandestina = list(minhaTupla)
print("Lista clandestina: ", listaClandestina)
listaClandestina[2] = "Leite Condensado"
print("Lista clandestina com dado alterado: ", listaClandestina)

minhaTupla = tuple(listaClandestina)

#Criar a tupla com apenas um item -> USAR A VÍRGULA
minhaTuplaDois = ('tupla',)
print("Verificando o tipo de dado:",type (minhaTuplaDois))
print("Acessando pela posição ordenada:", minhaTuplaDois[0])
print("Acessando pela indexação negativa:", minhaTuplaDois[-1])

#deletar a tupla completamente
#del minhaTuplaDois
#print("Apagar a tupla:", minhaTuplaDois)

#Juntando Tuplas
minhaTuplaTres = minhaTupla + minhaTuplaDois
print("Juntando tuplas: ", minhaTuplaTres)

#Contando quantas vezes repete a palavra tupla
repeticao = minhaTuplaTres.count('tupla')
print("Contando quantas vezes repete:", repeticao)

#Função Index retorna a primeira posição do item buscado
posicaoItem = minhaTuplaTres.index('tupla')
print("Posição do item tupla:", posicaoItem)



