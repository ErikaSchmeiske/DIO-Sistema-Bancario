# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 19:48:53 2023

@author: Erika
"""

# SISTEMA BANCÁRIO EM PYTHON

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        #Evita depósito de valores negativos
        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor: .2f}\n"
            
        else:
            print("Operação falhou. O valor informado é inválido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        #Verificações
        excedeu_saldo = valor > saldo        
        excedeu_limite = valor > limite        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
     
        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Você excedeu o limite de saques permitiu.")
        
        #Impedindo o saque de um valor negativo da conta
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : R$ {valor: .2f}\n"
            numero_saques += 1
        
        else:
            print("Operação fahou! O valor informado é inválido.")
        
        
    elif opcao == "e":
        print("\n -----------EXTRATO-------------")
        print("Não foram realizadas movimentações." if not extrato else extrato) #IF TERNÁRIO
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("----------------------------------")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione uma opção válida.")
        
    