usuarios = []

while True:
    print("Menu:")
    print("1 - Adicionar usuário")
    print("2 - Exibir resultados e sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        peso = float(input("Digite o peso (kg): "))
        altura = float(input("Digite a altura (m): "))
        
        imc = peso / (altura ** 2)
        
        # Classificação do IMC
        if imc < 18.5:
            situacao = "Abaixo do peso"
        elif imc < 25:
            situacao = "Peso normal"
        elif imc < 30:
            situacao = "Sobrepeso"
        elif imc < 35:
            situacao = "Obesidade grau I"
        elif imc < 40:
            situacao = "Obesidade grau II"
        else:
            situacao = "Obesidade grau III (mórbida)"
        
        # Armazenando os dados
        usuarios.append({
            'nome_completo': f"{nome} {sobrenome}",
            'imc': imc,
            'situacao': situacao
        })
    
    elif opcao == '2':
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            break
        
        # Exibindo resultados
        for usuario in usuarios:
            print(f"Nome completo: {usuario['nome_completo']}")
            print(f"IMC: {usuario['imc']:.2f}")
            print(f"Situação: {usuario['situacao']}\n")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
