usuarios = []

while True:
    opcao = input("Escolha uma opção (1 - Adicionar usuário, 2 - Exibir resultados e sair): ")
    
    if opcao == '1':
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        peso = float(input("Digite o peso (kg): "))
        altura = float(input("Digite a altura (m): "))
        
        imc = peso / (altura ** 2)
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
        
        usuarios.append({'nome_completo': f"{nome} {sobrenome}", 'imc': imc, 'situacao': situacao})
    
    elif opcao == '2':
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in usuarios:
                print(f"Nome: {usuario['nome_completo']}, IMC: {usuario['imc']:.2f}, Situação: {usuario['situacao']}")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

