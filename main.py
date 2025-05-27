import os

# Caminho da pasta com as fotos
pasta = "assets/dia-dos-namorados1"
caminho_completo = os.path.join(os.getcwd(), pasta)

# Lista todos os arquivos da pasta
arquivos = sorted(os.listdir(caminho_completo))

# Filtra apenas arquivos de imagem comuns (opcional, mas recomendável)
extensoes_imagem = (".jpg", ".jpeg", ".png", ".webp", ".gif")
arquivos_imagem = [f for f in arquivos if f.lower().endswith(extensoes_imagem)]

# Gera as linhas no formato desejado
linhas = []
for nome in arquivos_imagem:
    titulo = os.path.splitext(nome)[0]
    linha = f'{{ src: "assets/{pasta}/{nome}", title: "{titulo}" }},'
    linhas.append(linha)

# Escreve no arquivo .txt
with open("fotos_formatadas.txt", "w", encoding="utf-8") as arquivo_saida:
    for linha in linhas:
        arquivo_saida.write(" " * 12 + linha + "\n")

print("Arquivo 'fotos_formatadas.txt' gerado com sucesso.")
