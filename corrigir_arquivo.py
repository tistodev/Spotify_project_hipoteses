import pandas as pd

try:
    df = pd.read_csv("track_in_spotify - spotify.csv", sep=";", encoding="utf-8-sig", on_bad_lines='skip')
    print("Arquivo carregado com sucesso!")
except UnicodeDecodeError:
    print("Erro com UTF-8, tentando ISO-8859-1...")
    df = pd.read_csv("track_in_spotify - spotify.csv", sep=";", encoding="ISO-8859-1", on_bad_lines='skip')
    print("Arquivo carregado com ISO-8859-1!")

# Limpa os nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# Corrige nome da primeira coluna, se necessário
df.rename(columns={df.columns[0]: 'track_id'}, inplace=True)

# Salva CSV corrigido com codificação UTF-8-SIG
df.to_csv("spotify_corrigido.csv", sep=";", index=False, encoding="utf-8-sig")
print("\n✅ Arquivo salvo como 'spotify_corrigido.csv'")
