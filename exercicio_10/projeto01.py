# Dicionário principal para armazenar os dados das praias
praias = {}

while True:
    # Solicita o nome da praia
    nome = input("Digite o nome da praia (ou pressione Enter para encerrar): ").strip()

    # Encerra o loop se o nome estiver vazio
    if nome == "":
        break

    # Verifica se a praia já foi cadastrada
    if nome in praias:
        print("Esta praia já foi cadastrada. Utilize outro nome.\n")
        continue

    try:
        # Coleta os dados numéricos
        distancia = int(input(f"Informe a distância de {nome} até o centro da cidade (em km): "))
        veranistas = int(input(f"Informe o número médio de veranistas na última temporada em {nome}: "))
        acesso = int(input(f"Informe o tipo de acesso à {nome} (0 = não asfaltado, 1 = asfaltado): "))

        # Valida o tipo de acesso
        if acesso not in (0, 1):
            print("Tipo de acesso inválido. Digite 0 para não asfaltado ou 1 para asfaltado.\n")
            continue

        # Adiciona a praia ao dicionário principal
        praias[nome] = {
            "distancia_km": distancia,
            "veranistas": veranistas,
            "acesso": acesso
        }

        print(f"Praia '{nome}' cadastrada com sucesso.\n")

    except ValueError:
        # Trata erro de conversão de tipos
        print("Erro: informe apenas valores numéricos válidos para distância, número de veranistas e tipo de acesso.\n")

# Exibe os dados cadastrados
print("\nLista de Praias Cadastradas:")
for nome, dados in praias.items():
    acesso_str = "Asfaltado" if dados["acesso"] == 1 else "Não asfaltado"
    print(f"Praia: {nome}")
    print(f"  Distância do centro: {dados['distancia_km']} km")
    print(f"  Número médio de veranistas: {dados['veranistas']}")
    print(f"  Tipo de acesso: {acesso_str}\n")

# Análise dos dados no dicionário 'praias'

# 1. Número de praias a até 15 km do centro
praias_ate_15km = [nome for nome, dados in praias.items() if dados["distancia_km"] <= 15]
quantidade_ate_15km = len(praias_ate_15km)

# 2. Média de veranistas nas praias com acesso não asfaltado
veranistas_nao_asfaltado = [
    dados["veranistas"] for dados in praias.values() if dados["acesso"] == 0
]
if veranistas_nao_asfaltado:
    media_veranistas_nao_asfaltado = sum(veranistas_nao_asfaltado) / len(veranistas_nao_asfaltado)
else:
    media_veranistas_nao_asfaltado = 0

# 3. Praias asfaltadas com menos de 1000 veranistas
asfaltadas_menos_1000 = [
    (nome, dados["distancia_km"])
    for nome, dados in praias.items()
    if dados["acesso"] == 1 and dados["veranistas"] < 1000
]

# Exibe os resultados
print("Análise dos dados cadastrados:\n")

print(f"1. Número de praias a até 15 km do centro: {quantidade_ate_15km}")

print("2. Média de veranistas nas praias com acesso não asfaltado: "
      f"{media_veranistas_nao_asfaltado:.2f}")

print("3. Praias com acesso asfaltado e menos de 1000 veranistas:")
if asfaltadas_menos_1000:
    for nome, distancia in asfaltadas_menos_1000:
        print(f"   - {nome}: {distancia:.1f} km do centro")
else:
    print("   Nenhuma praia atende a esse critério.")
