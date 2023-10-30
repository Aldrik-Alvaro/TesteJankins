import calculadora

def main():
    while True:
        print("Calculadora Simples")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '1':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calculadora.somar(a, b)
            print("Resultado: ", resultado)

        elif escolha == '2':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calculadora.subtrair(a, b)
            print("Resultado: ", resultado)

        elif escolha == '3':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calculadora.multiplicar(a, b)
            print("Resultado: ", resultado)

        elif escolha == '4':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            try:
                resultado = calculadora.dividir(a, b)
                print("Resultado: ", resultado)
            except ValueError as e:
                print("Erro:", e)

        elif escolha == '5':
            print("Saindo da calculadora.")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
