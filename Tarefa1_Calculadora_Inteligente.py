#Calculadora inteligente
print('Vamos iniciar a calculadora inteligente, siga os passos a seguir.')
resultado = 0
continue_with_result = False

while True:
    if continue_with_result:
        print(f'Utilizando o resultado anterior {resultado: .2f}')
        var_1 = resultado
    else:
        while True:
            try:
                var_1 = float(input(f'Digite o primeiro número: '))
                break
            except ValueError:
                print('Entrada iválida. Por favor, digite um número válido.')
    while True:
        try:
            var_2 = float(input('Digite o segundo número: '))
            break
        except ValueError:
            print('Entrada iválida. Por favor, digite um número válido.')
    while True:
        print('\nEscolha a operação')
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        try:
            operation = int(input("Digite o número da operação desejada:"))
            if operation in [1,2,3,4,5]:
                break
            else:
                print('Opção inválida. Por favor, escolha um número entre 1 e 5.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')

    if operation == 1:
        resultado = var_1 + var_2
        print(f'Resultado da soma: {resultado: .2f}')
    elif operation == 2:
        while True:
            print('\nEscolha a ordem da operação')
            print(f'\n1.{var_1} - {var_2}')
            print(f'\n2.{var_2} - {var_1}')
            try: 
                order = int(input('Qual a ordem da subtração:'))
                if order == 1:
                    resultado = var_1 - var_2
                elif order == 2:
                    resultado = var_2 - var_1
                else:
                    print('Opção inválida. Escolha 1 ou 2')
                    continue
                break
            except ValueError:
                print('Entrada inválida. Por favor, escolha 1 ou 2.')
        print(f"Resultado da subtração: {resultado: .2f}")
    elif operation == 3:
        resultado = var_1 * var_2
        print(f'Resultado da multiplicação: {resultado: .2f}')
    elif operation == 4:
        while True:
            print('\nEscolha a ordem da divisão')
            print(f'\n1.{var_1} / {var_2}')
            print(f'\n2.{var_2} / { var_1}')
            try:
                order = int(input('Qual a ordem da divisão?'))
                if order == 1:
                    if var_2 == 0:
                        print('Não é possível dividir por 0. Informe outro número.')
                        var_2 = float(input('Digite o segundo número novamente: '))
                        continue
                    resultado = var_1 / var_2
                elif order == 2:
                    while var_1 == 0:
                        print('Não é possível dividir por 0.Informe outro número.')
                        var_1 = float(input('Digite o primeiro número novamente: '))
                        continue
                    resultado = var_2 / var_1
                else:
                    print('Opção inválida. Escolha 1 ou 2')
                    continue
                break
            except ValueError:
                print('Entrada inválida. Por favor, escolha 1 ou 2.') 
        print(f"Resultado da divisão: {resultado: .2f}")
    elif operation == 5:
        print(f'Encerrando a calculadora inteligente... O último resultado foi: {resultado:.2f}') 
        break

    while True:  
        continue_choice = input('Deseja continuar usando esse resultado? (s/n): ').strip().lower()
        if continue_choice in ['s','n']:
            continue_with_result = continue_choice == 's'
            break
        else:
            print('Entrada inválida. Responda com "s" para sim ou "n" para não.')


