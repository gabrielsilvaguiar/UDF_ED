from datetime import datetime

filaPreferencial = []
filaNormal = []
senhaPreferencial = 1
senhaNormal = 1

def adicionar_a_fila(tipo_atendimento, tipoFila):
    global senhaPreferencial, senhaNormal
    if tipoFila == 'preferencial':
        filaPreferencial.append(f"{tipo_atendimento} - Senha: {senhaPreferencial}")
        senhaPreferencial += 1
    elif tipoFila == 'normal':
        filaNormal.append(f"{tipo_atendimento} - Senha: {senhaNormal}")
        senhaNormal += 1

def verificar_horario():
    agora = datetime.now()
    return agora.hour < 18  # Retorna True se for antes das 18 horas

print("\n------Bem-vindo(a) a UBS-UDF------")
print("\n1-Clinico Geral \n2-Genecologia \n3-Pediatria \n4-Geriatria \n5-Ortopedia")

if verificar_horario():
    total = int(input("\nQual é o tipo de atendimento que você deseja? "))

    if total == 1:
        tipo_atendimento = "Clinico Geral"
    elif total == 2:
        tipo_atendimento = "Genecologia"
    elif total == 3:
        tipo_atendimento = "Pediatria"
    elif total == 4:
        tipo_atendimento = "Geriatria"
    elif total == 5:
        tipo_atendimento = "Ortopedia"
    else:
        print("Tipo de atendimento inválido.")
        tipo_atendimento = None

    if tipo_atendimento:
        tipoFila = input("Você é preferencial? (s/n) ").strip().lower()
        if tipoFila == 's':
            adicionar_a_fila(tipo_atendimento, 'preferencial')
        elif tipoFila == 'n':
            adicionar_a_fila(tipo_atendimento, 'normal')
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
else:
    print("Desculpe, não estamos emitindo senhas após as 18 horas.")

print("Fila Preferencial:", filaPreferencial)
print("Fila Normal:", filaNormal)