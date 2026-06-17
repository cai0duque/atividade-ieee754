# CALCULADORA IEEE 754 DE PRECISÃO SIMPLES (32 BITS)
def converter_inteiro_para_binario(valor_inteiro):
    """
    Converte a parte inteira de um número decimal para binário.
    Método matemático: Divisões sucessivas por 2, agrupando os restos.
    """
    if valor_inteiro == 0:
        return "0"
    
    bits = ""
    temp = valor_inteiro
    while temp > 0:
        resto = temp % 2
        bits = str(resto) + bits # O resto é adicionado à esquerda
        temp = temp // 2         # Divisão inteira
        
    return bits


def converter_fracao_para_binario(valor_fracionario, limite_bits=150):
    """
    Converte a parte fracionária de um número decimal para binário.
    Método matemático: Multiplicações sucessivas por 2, extraindo a parte inteira.
    O limite_bits previne loops infinitos em dízimas periódicas binárias.
    """
    if valor_fracionario == 0.0:
        return "0"
        
    bits = ""
    temp = valor_fracionario
    
    for _ in range(limite_bits):
        temp *= 2
        if temp >= 1.0:
            bits += "1"
            temp -= 1.0
        else:
            bits += "0"
            
        if temp == 0.0: # Fim exato da fração
            break
            
    return bits


def decimal_para_ieee754(numero):
    """
    Orquestra a conversão de um número decimal (float) para o formato IEEE 754 (32 bits).
    Retorna uma tupla: (sinal, expoente_binario, mantissa_binaria).
    """
    # Tratamento especial para o número zero
    if numero == 0.0:
        return "0", "00000000", "0" * 23

    # 1. Determinar o bit de sinal
    sinal = "1" if numero < 0 else "0"
    numero_absoluto = abs(numero)

    # 2. Separar parte inteira da fracionária
    parte_inteira = int(numero_absoluto)
    parte_fracionaria = numero_absoluto - parte_inteira

    # 3. Converter ambas as partes para binário
    bin_inteiro = converter_inteiro_para_binario(parte_inteira)
    bin_fracao = converter_fracao_para_binario(parte_fracionaria)

    # 4. Normalização (Colocar na forma 1.xxxxx * 2^e)
    # Precisamos encontrar o primeiro '1' para estabelecer o "bit implícito"
    if bin_inteiro != "0":
        # Ex: 101.11 -> O ponto anda para a esquerda.
        # A quantidade de casas que o ponto anda é (tamanho do inteiro - 1)
        expoente_verdadeiro = len(bin_inteiro) - 1
        # A mantissa é tudo após o primeiro '1' da parte inteira, mais a parte fracionária
        mantissa_bruta = bin_inteiro[1:] + bin_fracao
    else:
        # Ex: 0.00101 -> O ponto anda para a direita até depois do primeiro '1'.
        posicao_primeiro_um = bin_fracao.find("1")
        if posicao_primeiro_um == -1: # Prevenção de falha (não deve ocorrer se numero!=0)
            return sinal, "00000000", "0" * 23
            
        expoente_verdadeiro = -(posicao_primeiro_um + 1)
        # A mantissa é tudo após o primeiro '1' da parte fracionária
        mantissa_bruta = bin_fracao[posicao_primeiro_um + 1:]

    # 5. Cálculo do Expoente com Viés (Bias de 127 para 32 bits)
    expoente_com_vies = expoente_verdadeiro + 127
    # Converte o expoente para binário e garante que tenha exatamente 8 bits preenchendo com zeros à esquerda
    bin_expoente = converter_inteiro_para_binario(expoente_com_vies).zfill(8)

    # 6. Agrupar a Mantissa (23 bits)
    # Trunca se for maior que 23 bits, ou preenche com zeros à direita se for menor.
    mantissa = mantissa_bruta[:23].ljust(23, '0')

    return sinal, bin_expoente, mantissa


def ieee754_para_decimal(sinal, expoente, mantissa):
    """
    Converte a representação IEEE 754 binária de volta para decimal.
    Isso nos ajuda a comprovar a limitação e a perda de precisão dos 32 bits!
    """
    if expoente == "00000000" and mantissa == "0" * 23:
        return 0.0
        
    # Remove o viés para achar o expoente real
    expoente_real = int(expoente, 2) - 127
    
    # Recria o valor da mantissa adicionando o "bit implícito" (1.0)
    valor_mantissa = 1.0 
    for i, bit in enumerate(mantissa):
        if bit == '1':
            # i + 1 representa as posições fracionárias (2^-1, 2^-2, etc)
            valor_mantissa += 2 ** -(i + 1)
            
    resultado = valor_mantissa * (2 ** expoente_real)
    return -resultado if sinal == "1" else resultado


def main():
    print("======================================================")
    print(" CALCULADORA IEEE 754 (PRECISÃO SIMPLES) - PASSO A PASSO")
    print("======================================================\n")

    # ==========================================
    # PASSO 1: Entrada de Dados
    # ==========================================
    try:
        num1 = float(input("Digite o 1º número decimal: "))
        num2 = float(input("Digite o 2º número decimal: "))
    except ValueError:
        print("Erro: Por favor, insira números válidos.")
        return

    print("\n--- PASSO 2: Conversão Matemática e Exibição ---")
    
    # Conversão do Primeiro Número
    sinal1, exp1, man1 = decimal_para_ieee754(num1)
    print(f"\nNúmero 1: {num1}")
    print("IEEE 754: [Sinal (1 bit)] | [Expoente (8 bits)] | [Mantissa (23 bits)]")
    print(f"          [{sinal1}]             | [{exp1}]          | [{man1}]")

    # Conversão do Segundo Número
    sinal2, exp2, man2 = decimal_para_ieee754(num2)
    print(f"\nNúmero 2: {num2}")
    print("IEEE 754: [Sinal (1 bit)] | [Expoente (8 bits)] | [Mantissa (23 bits)]")
    print(f"          [{sinal2}]             | [{exp2}]          | [{man2}]")


    # ==========================================
    # PASSO 3: Operação Simulada e Comparação
    # ==========================================
    print("\n\n--- PASSO 3: Operação de Soma e Comparação ---")
    
    # Operação Matemática (Soma dos decimais inseridos)
    soma_nativa = num1 + num2
    
    # Passamos a soma pela conversão IEEE 754 de 32 bits manual
    sinal_soma, exp_soma, man_soma = decimal_para_ieee754(soma_nativa)
    
    print(f"\nResultado Esperado da Soma (num1 + num2): {soma_nativa}")
    print("\nConversão do Resultado para IEEE 754 (32 bits simulado):")
    print("IEEE 754: [Sinal (1 bit)] | [Expoente (8 bits)] | [Mantissa (23 bits)]")
    print(f"          [{sinal_soma}]             | [{exp_soma}]          | [{man_soma}]")
    
    # Para demonstrar a perda de precisão, re-convertemos a string 32 bits de volta para decimal
    resultado_simulado_32bits = ieee754_para_decimal(sinal_soma, exp_soma, man_soma)
    
    print("\n------------------------------------------------------")
    print(" COMPARAÇÃO DE PRECISÃO (64-bit Python vs 32-bit Simulado)")
    print("------------------------------------------------------")
    print(f"Resultado Nativo (Python 64-bits) : {soma_nativa}")
    print(f"Resultado na Calculadora (32-bits): {resultado_simulado_32bits}")
    
    diferenca = abs(soma_nativa - resultado_simulado_32bits)
    
    if diferenca == 0.0:
        print("\nConclusão: NÃO HOUVE perda de precisão para esta operação.")
        print("O número pôde ser representado com exatidão nos 23 bits de mantissa.")
    else:
        print(f"\nConclusão: HOUVE perda de precisão devido ao limite de 32 bits.")
        print(f"Diferença observada de: {diferenca}")
        print("Isso ocorre porque os bits excedentes (após a 23ª casa da mantissa)")
        print("foram truncados/perdidos na conversão!")
        
    print("\n======================================================")

if __name__ == "__main__":
    main()