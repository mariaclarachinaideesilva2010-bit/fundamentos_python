# Autor: Maria Clara
# Projeto: Dicionários

# Projeto aquele lá
escola = {
    "salas":"sala_musica",
    "localizacao": "bloco_a",
    "qtd_lugares": "40",
    "caracteristicas": "acustica"
}

# Acessando dados do dicionário
print(f"Sala disponível: {escola["salas"]}")

# Adicionando mais itens ao dicionário
escola["iluminacao"] = "led"
print(f"Sala disponível {escola["iluminacao"]}")

# Alterando um valor do dicionário
escola["salas"] = "sala"
print(f"Sala disponível: {escola["salas"]}")