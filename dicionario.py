meuDicionario = {
 "nome"     : "Ana",  #quando houver mais itens, colocar a vírgula
 "idade"    :  16  
}
print("Mostrando meu dicionário:      ",meuDicionario)

#Acessando valores específicos pela chave
print("Mostrando o valor pela chave:  ",meuDicionario['nome'])
print("Mostrando o valor pela chave:  ",meuDicionario['idade'])

#Acessando valores pelo método get()
print("Mostrar valor pelo método get: ",meuDicionario.get('nome'))

#Alterar valores específicos do dicionário
meuDicionario ['nome'] = 'Carolina'
print("Mostrando o dicionário com valor alterado:", meuDicionario)

#Percorrendo o dicionário para retornar as chaves
for x in meuDicionario :
    print("Percorrendo o dicionário: ",x)

#Percorrendo o dicionário para retornar os valores
for x in meuDicionario:
    print("Percorrendo o dicionário: ",meuDicionario[x])

#Percorrendo o dicionário para retornar os valores com o método .values()
for x  in meuDicionario.values():
    print("Percorrendo o dicionário para retornar valores: ",x)

#Percorrendo valores forma alternativa
for x in meuDicionario:
    print(x + ":",meuDicionario[x]) 

#Comandos condicionais
if 'nome' in meuDicionario :
    print("Sim, nome está no dicionário!")
else:
    print("Não, nome não está no dicionário!")

#Itens por linha
print("Tamanho do dicionário: ", len(meuDicionario))

#Adicionando novo item ao dicionário
meuDicionario['endereço']  = 'Centro'
print("Adicionando novo item: (Chave e Valor)", meuDicionario)

#Removendo item do dicionário com função .pop()
meuDicionario.pop('endereço')
print("Dicionário com item removido:",meuDicionario)


