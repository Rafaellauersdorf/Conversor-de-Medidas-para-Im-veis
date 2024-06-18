def converter_medidas():
    while True:
        print("\033[1;33mEscolha a opção de conversão (ou digite 'SAIR' para sair):\033[0m")
        print("\033[1;33m1. Hectares para Alqueires\033[0m")
        print("\033[1;33m2. Hectares para Metros Quadrados\033[0m")
        print("\033[1;33m3. Alqueires para Hectares\033[0m")
        print("\033[1;33m4. Alqueires para Metros Quadrados\033[0m")
        print("\033[1;33m5. Metros Quadrados para Hectares\033[0m")
        print("\033[1;33m6. Metros Quadrados para Alqueires\033[0m")

        opcao_str = input("\033[1;34mDigite o número da opção desejada:\033[0m")

        if opcao_str.upper() == "SAIR":
            print("Encerrando o programa...")
            break

        try:
            opcao = int(opcao_str)
        except ValueError:
            print("\033[1;31mOpção inválida. Por favor, digite uma das opções de 1 a 6 ou 'SAIR'.\033[0m")
            continue

        if opcao < 1 or opcao > 6:
            print("\033[1;31mOpção inválida. Por favor, escolha um número de 1 a 6.\033[0m")
            continue

        valor_str = input("\033[1;33mDigite o valor a ser convertido (\033[1;31mNÃO\033[0m \033[1;33muse vírgula):\033[0m ")

        if "," in valor_str:
            print("\033[1;31mErro: Utilize ponto (.) para separar decimais.\033[0m")
            continue

        valor_str = valor_str.replace(".", "")

        try:
            valor = float(valor_str)
        except ValueError:
            print("\033[1;31mErro: Digite um número válido.\033[0m")
            continue

        if opcao == 1:
            resultado = valor * 0.4132
            print(f"{valor:,.2f} hectares equivalem a {resultado:,.2f} alqueires")
        elif opcao == 2:
            resultado = valor * 10000
            print(f"{valor:,.2f} hectares equivalem a {resultado:,.2f} metros quadrados")
        elif opcao == 3:
            resultado = valor * 2.42
            print(f"{valor:,.2f} alqueires equivalem a {resultado:,.2f} hectares")
        elif opcao == 4:
            resultado = valor * 24200
            print(f"{valor:,.2f} alqueires equivalem a {resultado:,.2f} metros quadrados")
        elif opcao == 5:
            resultado = valor / 10000
            print(f"{valor:,.0f} metros quadrados equivalem a {resultado:,.2f} hectares")
        elif opcao == 6:
            resultado = valor / 24200
            print(f"{valor:,.0f} metros quadrados equivalem a {resultado:,.2f} alqueires")

        continuar = input("\033[1;32mDeseja fazer outra conversão? (s/n): \033[0m")
        if continuar.lower() != "s":
            break

# Apresentação inicial (fora do loop)
print("\033[1;36mBem-vindo ao Conversor de Medidas de Imóveis do setor de Patrimônio do IAT!\033[0m")
print("\033[1;32mDesenvolvido por:\033[0m \033[1;35mRafael Souza\033[0m")
converter_medidas()  # Chama a função para iniciar as conversões
