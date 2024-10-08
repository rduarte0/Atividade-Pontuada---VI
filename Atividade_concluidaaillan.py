import os
os.system ("cls || clear")

pessoas = []
quantidade = 0
soma_salarios = 0.0

while True:
    print("Menu:")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados e sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        salario = float(input("Digite o salário: "))
        
        # Armazenando dados
        pessoas += [{'idade': idade, 'sexo': sexo, 'salario': salario}]
        quantidade += 1
        soma_salarios += salario
    
    elif opcao == '2':
        if quantidade == 0:
            print("Nenhuma pessoa cadastrada.")
            break
        
        # a) Média de salário
        media_salario = soma_salarios / quantidade
        
        # b) Maior e menor idade 
        idades = [p['idade'] for p in pessoas]
        maior_idade = max(idades)
        menor_idade = min(idades)
        
        # c) Quantidade de mulheres com salário a partir de R$ 5.000,00
        quantidade_mulheres = 0
        for p in pessoas:
            if p['sexo'] == 'F' and p['salario'] >= 5000.00:
                quantidade_mulheres += 1
        
        print(f"Média de salário do grupo: R$ {media_salario:.2f}")
        print(f"Maior idade do grupo: {maior_idade} anos")
        print(f"Menor idade do grupo: {menor_idade} anos")
        print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres}")
        break
    
    else:
        print("Opção inválida, tente novamente.")
