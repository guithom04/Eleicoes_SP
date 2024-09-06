import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

# Inicializa o objeto pytrends para realizar as consultas no Google Trends
pytrends = TrendReq(hl='en-US', tz=360)

# Definir as palavras-chave para comparação
# Essas são as personalidades cujas buscas no Google queremos comparar
keywords = ['Pablo Marçal', 'Boulos', 'Ricardo Nunes', 'Tabata Amaral']

# Filtro geográfico - restringe os dados ao estado de São Paulo (SP)
geo = 'BR-SP'

# Define o intervalo de tempo da busca - de 16 de agosto de 2023 até 5 de setembro de 2024
timeframe = '2023-08-16 2024-09-05'

# Constrói a consulta para múltiplas palavras-chave com o filtro geográfico e o intervalo de tempo
pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')

# Busca os dados de interesse ao longo do tempo para todas as palavras-chave
data = pytrends.interest_over_time()

# Verifica se os dados foram retornados e se a coluna existe
if not data.empty:
    # Remove a coluna 'isPartial' (opcional), que indica se os dados são parciais
    data = data.drop(columns=['isPartial'])

    # Exibe as últimas linhas dos dados de forma organizada com pandas
    print("Dados do Google Trends (Comparação):")
    print(data.tail())

    # Define cores personalizadas para cada palavra-chave no gráfico
    colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

    # Criação do gráfico para comparar as tendências de busca
    plt.figure(figsize=(12, 8))
    
    # Plota cada palavra-chave com uma cor personalizada
    for i, keyword in enumerate(keywords):
        plt.plot(data.index, data[keyword], marker='o', linestyle='-', color=colors[i], label=keyword)

    # Adiciona título e rótulos aos eixos
    plt.title('Comparação de Tendências de Busca no Google: São Paulo (Desde 16 de agosto de 2023)', fontsize=16, fontweight='bold')
    plt.xlabel('Tempo', fontsize=14)
    plt.ylabel('Interesse ao longo do tempo (0 a 100)', fontsize=14)

    # Rotaciona os rótulos do eixo x para melhor legibilidade
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    # Adiciona linhas de grade para facilitar a leitura
    plt.grid(True, linestyle='--', alpha=0.6)

    # Adiciona uma legenda para diferenciar as palavras-chave, posicionada no canto superior esquerdo
    plt.legend(title='Termos de Busca', title_fontsize='13', fontsize='12', loc='upper left')

    # Ajusta o layout para evitar que os rótulos sejam cortados
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()

else:
    # Caso não sejam encontrados dados
    print(f"Nenhum dado encontrado para os termos especificados.")
