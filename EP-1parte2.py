# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:38:32 2018

@author: Gabriel Miras
"""
import json 
with open ('PE1.txt', 'r') as arquivo:
    estoque = json.loads(arquivo.read())
x=1

while x >= 0:
    print('''Controle de estoque
          0 - sair
          1 - adicionar item
          2 - remover item
          3 - alterar item
          4- imprimir estoque''')
    x = int(input('Faça sua escolha:'))
    if x == 0:
        print('Até mais!')
        break
    elif x == 1:
        produto = input('Nome do produto: ')
        produto = produto.lower()
        if produto not in estoque:
            quantidade = int(input('Quantidade inicial: '))
            if quantidade < 0:
                print('A quantidade inicial não pode ser negativa.')
                quantidade = int(input('Quantidade inicial: '))
            else:
                estoque[produto] = quantidade
        else:
            print('Produto já cadastrado!')
    elif x == 2:
        produto = input('Nome do produto: ')
        produto = produto.lower()
        if produto in estoque:
            del(estoque[produto])
    elif x == 3:
        produto = input('Nome do produto: ')
        produto = produto.lower()
        if produto in estoque:
            quantidade = estoque[produto]
            adicao = int(input('Quantidade: '))
            quantidade_nova = adicao + quantidade            
            print('Novo estoque de {0}: {1} '.format(produto, quantidade_nova))
            del(quantidade)
            estoque[produto] = quantidade_nova            
    elif x == 4:
        for keys,values in estoque.items():
            print('{0} : {1}'.format(keys, values))

        
            
            
with open ('PE1.txt', 'w') as arquivo:
    estoque_atualizado = json.dumps(estoque)
    arquivo.write(estoque_atualizado)        