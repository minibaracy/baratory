# Sistema de depósito em conta
saldo = float(input("Informe o saldo da sua conta: "))
deposito = float(input("Informe o valor a ser depositado: "))
saldo += deposito
print(f"Novo saldo: R$ {saldo:.2f}")

# Sistema de orçamento e gasto
orcamento = float(input("Informe seu orçamento: "))
gasto = float(input("Informe o gasto: "))
orcamento -= gasto
print(f"Orçamento restante: R$ {orcamento:.2f}")

# Sistema de estoque
estoque_inicial = int(input("Informe o estoque no início do dia: "))
vendido = int(input("Informe a quantidade vendida: "))
estoque_inicial -= vendido
print(f"Estoque final: {estoque_inicial}")

# Multiplicação por 3
numero = int(input("Informe um número: "))
numero *= 3
print(f"Número multiplicado por 3: {numero}")

# Conversão horas para dias
horas = float(input("Informe quantidade de horas: "))
horas /= 24
print(f"Em dias: {horas:.2f}")

# Minutos para horas inteiras
minutos = int(input("Informe minutos: "))
minutos //= 60
print(f"Horas inteiras: {minutos}")

# Segundos para minutos inteiros
segundos = int(input("Informe segundos: "))
segundos //= 60
print(f"Minutos inteiros: {segundos}")

# Verificação par/ímpar
num = int(input("Informe um número: "))
num %= 2
print(f"Resultado do módulo 2: {num}")
if num == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# Estoque com vendas, reposição e módulo 6
estoque = int(input("Informe valor de estoque: "))
vendas = int(input("Informe vendas: "))
estoque -= vendas
reposicao = int(input("Informe reposição: "))
estoque += reposicao
estoque %= 6
print(f"Estoque final após módulo 6: {estoque}")

# Conversão segundos para minutos e segundos restantes
total_segundos = int(input("Informe tempo em segundos: "))
minutos = total_segundos // 60
segundos_restantes = total_segundos % 60
print(f"{minutos} minutos e {segundos_restantes} segundos")

# Distância metros para km e metros restantes
metros = int(input("Informe distância em metros: "))
km = metros // 1000
metros_restantes = metros % 1000
print(f"{km} km e {metros_restantes} metros")