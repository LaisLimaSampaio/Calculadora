acumulador = 0

def calcular(operacao, numero):
    global acumulador
    try:
        if operacao == "+":
            acumulador += numero
        elif operacao == "-":
            acumulador -= numero
        elif operacao == "*":
            acumulador *= numero
        elif operacao == "/":
            if numero == 0:
                raise ZeroDivisionError("Divisão por zero não pode ser realizada.")
            acumulador /= numero
        return True

    except ZeroDivisionError as e:
        return f"Erro: {e}"
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def obter_numero_inicial():
    while True:
        try:
            return float(input("Digite o número inicial: "))
        except ValueError:
            print("Erro: Por favor, digite apenas números.")

def obter_operacao():
    operadores_validos = {"+", "-", "/", "*", "0"}
    while True:
        operacao = input("Digite a operação: ").strip()
        if operacao in operadores_validos:
            return operacao
        else:
            print("Operação inválida. Tente novamente.")

def obter_numero():
    while True:
        try:
            return float(input("Digite um número: "))
        except ValueError:
            print("Erro: Por favor, digite apenas números.")

acumulador = obter_numero_inicial()  
while True:
    print("------------------------ MENU ------------------------")
    print("                ESCOLHA UMA OPERAÇÃO")
    print("                     (+) Adição")
    print("                     (-) Subtração")
    print("                     (*) Multiplicação")
    print("                     (/) Divisão")
    print("                     (0) Sair")
    print("                                                       ")
    print(f"                   Acumulador: {acumulador}")

    operacao = obter_operacao()
    if operacao == "0":
        print("Saindo...")
        break

    numero = obter_numero()
    resposta = calcular(operacao, numero)
    if resposta is not True:
        print(resposta)
    else:
        print(f"Resultado: {acumulador}")
