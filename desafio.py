CONSTANTE_BONUS = 1000
nome_valido = False
salario_valido = False
bonus_valido = False

# 1) Solicite ao usuário que digite seu nome
while not nome_valido:
    try:
        nome_usuario = input("Digite seu nome: ")
        if len(nome_usuario) ==0:
            raise ValueError("O nome está vazio.")
            
        elif any(char.isdigit() for char in nome_usuario):
            raise ValueError("O nome não deve conter números.")
            
        elif nome_usuario.isspace():
            print("Você só digitou espaço!")
            
        else:
            print("Nome válido: ", nome_usuario)
            nome_valido = True
    except ValueError as e:
        print(e)
        

# 2) Solicite ao usuário que digite o valor do seu salário
# Converta a entrada para um número de ponto flutuante

while not salario_valido:
    try:
        salario_usuario = float(input("Digite seu salário: "))
        if salario_usuario< 0:
            print("O sálario tem que ser um valor positivo!")
        else:
            salario_valido = True

    except ValueError:
        print("Digite um número para o sálario!")
        

# 3) Solicite ao usuário que digite o valor do bônus recebido 
# Converte a entrada para um número de ponto flutuante

while not bonus_valido:
    try:
        bonus_usuario = float(input("Digite o valor do bônus: "))
        if bonus_usuario < 0:
            print("Digite um valor positivo!")
        else:
            bonus_valido = True    
    except ValueError:
        print("Digite um número para o bônus!")
        

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario*bonus_usuario

# 5) Imprima a mensagem persolazida incluindo o nome do usuário,e o valor do bônus
print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")