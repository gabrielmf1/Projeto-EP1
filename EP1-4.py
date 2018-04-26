#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:08:36 2018

@author: gabrielacaruso
"""
import json

with open ('ep1.txt', 'r') as arquivo:
    estoque = json.loads(arquivo.read())

while True:   
    print('''Controle de estoque
          0 - sair
          1 - adicionar item
          2 - remover item
          3 - alterar item
          4 - imprimir estoque
          5 - estoque negativo
          6 - imprimir preço total''')    
    x = int(input('Faça sua escolha: '))    
    if x == 0:
        print('Até mais!')
        break
    elif x == 1:
        produto = input('Nome do produto: ')
        produto = produto.lower()
        if produto not in estoque:        
            quantidade = int(input('Quantidade inicial: '))      
            while quantidade < 0:
                print('A quantidade inicial não pode ser negativa.')
                quantidade = int(input('Quantidade inicial: '))
            while quantidade >= 0:
                preco = float(input('Preço inicial: '))
                if preco not in estoque:
                    while preco < 0:
                        print('O preço inicial não pode ser negativo.')
                        preco = float(input('Preço inicial: '))
                    if preco >= 0:
                        estoque[produto] = {'quantidade': quantidade, 'preco': preco}
                        break
        else:
            print('Produto já cadastrado!')    
        estoque[produto] = {'quantidade': quantidade, 'preco': preco}                   
    elif x == 2:
        produto = input('Nome do produto: ')
        produto = produto.lower()
        if produto in estoque:
            del(estoque[produto])           
    elif x == 3:
        produto = input('Nome do produto: ')
        produto = produto.lower()
        if produto in estoque:
            opcao = str(input('Alterar quantidade ou preço?(q/p) '))
            quantidade=estoque[produto]['quantidade']
            preco=estoque[produto]['preco']
            if opcao == 'q':
                adicao = int(input('Quantidade: '))
                quantidade_nova = adicao + quantidade            
                print('Novo estoque de {0}: {1} '.format(produto, quantidade_nova))
                del(quantidade)
                estoque[produto] = {'quantidade': quantidade_nova, 'preco': preco}
            else:
                adicao2 = int(input('Preço: '))
                preco_novo = adicao2 + preco            
                print('Novo preço de {0}: {1} '.format(produto, preco_novo))
                del(preco)
                estoque[produto] = {'quantidade': quantidade, 'preco': preco_novo}
    elif x == 4:      
        for i in estoque:
            print('{0} : {1}'.format(i, estoque[i]["quantidade"]))
    elif x == 5:
        estoque_negativo = []
        for e in estoque:
            if estoque[e]['quantidade'] < 0:
                estoque_negativo.append(e)
        for i in estoque_negativo:
            print('{} : {}'.format(i,estoque[i]["quantidade"]))
    elif x == 6:
        i = 0
        for e in estoque:
            i += estoque[e]['quantidade'] * estoque[e]['preco']
        print(i)

with open ('ep1.txt', 'w') as arquivo:
    estoque_atualizado = json.dumps(estoque)
    arquivo.write(estoque_atualizado)        
