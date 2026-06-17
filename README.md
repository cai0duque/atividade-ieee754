# Calculadora IEEE 754 de Precisão Simples (32 bits)

Este é um projeto acadêmico focado no aprendizado de arquitetura de computadores e representação de dados. O script Python implementa a conversão e a operação matemática de soma de números de ponto flutuante, simulando o comportamento de baixo nível do hardware. 

A grande diferença deste projeto é que **toda a conversão matemática foi construída totalmente do zero**. Processos como divisão sucessiva para partes inteiras, multiplicação sucessiva para partes fracionárias, normalização do bit implícito e aplicação do viés do expoente estão detalhados e modularizados no código-fonte.

---

## 🛠️ Aviso de Dependências

Este projeto não utiliza libs nem dependências! Ele foi inteiramente construído utilizando **Python puro**.

* **Sem instalações:** Você não precisa rodar nenhum comando de instalação (como `pip install`).
* **Sem bibliotecas prontas:** O código **não** utiliza bibliotecas de estruturação de bytes ou otimização matemática (como `struct`, `math` ou `numpy`).

---

## ☁️ Como Executar na Nuvem

Caso você não possua o ambiente Python configurado no seu computador, você pode rodar e interagir com este programa diretamente pelo seu navegador através de plataformas virtuais gratuitas. Escolha uma das opções abaixo:

### 1. Executando no Google Colab
O Google Colab é uma plataforma do Google que permite executar códigos em Python na nuvem de forma muito interativa.

1. Acesse o site do Google Colab.
2. Clique na opção **"Novo notebook"** na tela inicial.
3. Abra o arquivo `calculadora_ieee754.py` em qualquer bloco de notas ou leitor de texto e **copie todo o código**.
4. **Cole o código** na primeira célula cinza que aparecerá no centro da tela do Colab.
5. Pressione o botão de **"Play"** (ícone circular com um triângulo) ao lado esquerdo da célula, ou aperte o atalho `Shift + Enter`.
6. O programa começará a rodar e um terminal simulado aparecerá logo abaixo da célula. Basta inserir os números decimais e visualizar o resultado matemático!

### 2. Executando no OneCompiler (Ainda mais rápido)
O OneCompiler é um compilador virtual super rápido e não exige sequer que você tenha uma conta logada.

1. Acesse a área de Python no site OneCompiler.
2. No editor de texto central (o arquivo `main.py`), você verá um pequeno código de exemplo. **Apague todo aquele código**.
3. Abra o arquivo `calculadora_ieee754.py` original do projeto e **copie todo o código**.
4. **Cole o nosso código** no editor que você acabou de esvaziar.
5. Clique no botão azul **"Run"** localizado no canto superior direito da tela.
6. Na aba de "Output" (ou terminal de saída) na parte inferior direita, o programa começará a rodar pedindo seus inputs. Digite os valores desejados, aperte "Enter" e veja a "mágica" acontecer.