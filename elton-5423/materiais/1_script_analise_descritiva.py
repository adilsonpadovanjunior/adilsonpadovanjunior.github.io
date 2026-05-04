import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# 1. DEFINIR CAMINHOS (ABSOLUTO)
# =========================

caminho_arquivo = r"C:\Users\Aluno\Documents\TCC\dados\base_dados.xlsx"
pasta_resultados = r"C:\Users\Aluno\Documents\TCC\resultados"

os.makedirs(pasta_resultados, exist_ok=True)

# =========================
# 2. CARREGAR BASE
# =========================

df = pd.read_excel(caminho_arquivo)
print(df.head())

# =========================
# 3. DEFINIR COLUNA DE TEMPO
# =========================

coluna_tempo = "Ano"  # alterar conforme a base

# =========================
# 4. ESTATÍSTICAS DESCRITIVAS
# =========================

variaveis_numericas = df.select_dtypes(include="number")

estatisticas = variaveis_numericas.describe().T
estatisticas_resumo = estatisticas[["mean", "min", "max", "std"]]
estatisticas_resumo.columns = ["Média", "Mínimo", "Máximo", "Desvio padrão"]

print("\nEstatísticas descritivas:")
print(estatisticas_resumo)

estatisticas_resumo.to_excel(os.path.join(pasta_resultados, "estatisticas_descritivas.xlsx"))

# =========================
# 5. GRÁFICOS DE SÉRIE TEMPORAL
# =========================

for coluna in variaveis_numericas.columns:
    if coluna != coluna_tempo:
        plt.figure(figsize=(10, 5))
        plt.plot(df[coluna_tempo], df[coluna], marker="o")
        plt.title(f"Evolução de {coluna}")
        plt.xlabel(coluna_tempo)
        plt.ylabel(coluna)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(pasta_resultados, f"grafico_{coluna}.png"))
        plt.close()

# =========================
# 6. COMPARAÇÃO ENTRE VARIÁVEIS
# =========================

plt.figure(figsize=(10, 5))

for coluna in variaveis_numericas.columns:
    if coluna != coluna_tempo:
        plt.plot(df[coluna_tempo], df[coluna], marker="o", label=coluna)

plt.title("Comparação entre variáveis")
plt.xlabel(coluna_tempo)
plt.ylabel("Valores")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(pasta_resultados, "comparacao_variaveis.png"))
plt.close()

# =========================
# 7. CORRELAÇÃO
# =========================

correlacao = variaveis_numericas.corr()

print("\nMatriz de correlação:")
print(correlacao)

correlacao.to_excel(os.path.join(pasta_resultados, "matriz_correlacao.xlsx"))

print("\nAnálise descritiva concluída.")

# =========================================================
# ORIENTAÇÕES IMPORTANTES PARA MONOGRAFIA (LEITURA OBRIGATÓRIA)
# =========================================================

# 1. SOBRE A BASE DE DADOS
# - A base deve estar organizada em formato de tabela:
#   (i) Colunas = variáveis
#   (ii) Linhas = períodos (tempo)
# - Não utilizar células mescladas
# - Evitar valores vazios ou textos em colunas numéricas

# 2. SOBRE A COLUNA DE TEMPO
# - Verificar se a variável definida em "coluna_tempo" está correta
# - Pode ser: Ano, Mês, Data, etc.
# - A ordem dos dados deve estar cronológica

# 3. SOBRE AS ESTATÍSTICAS
# - Média: valor médio da variável
# - Mínimo e máximo: identificam extremos
# - Desvio padrão: mede a variabilidade dos dados
# - Interpretar se há grande variação ou estabilidade

# 4. SOBRE OS GRÁFICOS
# - Observar:
#   (i) Tendência (crescimento, queda ou estabilidade)
#   (ii) Picos ou quedas abruptas
#   (iii) Possíveis mudanças de comportamento ao longo do tempo

# 5. SOBRE A COMPARAÇÃO ENTRE VARIÁVEIS
# - Verificar se as variáveis apresentam comportamento semelhante
# - Cuidado: escalas muito diferentes podem dificultar a visualização

# 6. SOBRE A CORRELAÇÃO
# - Valores próximos de +1 → relação positiva
# - Valores próximos de -1 → relação negativa
# - Valores próximos de 0 → pouca ou nenhuma relação
# - IMPORTANTE: correlação não implica causalidade

# 7. SOBRE A ESCRITA DA ANÁLISE DESCRITIVA
# - O aluno deve descrever:
#   (i) Comportamento geral das variáveis
#   (ii) Tendências observadas
#   (iii) Possíveis relações entre variáveis
#   (iv) Eventos atípicos (se existirem)
# - Evitar apenas "descrever o gráfico"
# - Interpretar economicamente os resultados

# 8. SOBRE REPRODUTIBILIDADE
# - Manter organização do projeto:
#   (i) Pasta "dados"
#   (ii) Pasta "resultados"
#   (iii) Script separado
# - Isso permite replicar o estudo

# =========================================================
# FIM DO SCRIPT
# =========================================================