import requests

def obter_cotacao_cripto(cripto, moeda):
    """Obtém a cotação de uma criptomoeda em relação a uma moeda específica."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies={moeda}"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta um erro se a resposta for um erro HTTP
        dados = resposta.json()
        
        if cripto in dados:
            return dados[cripto][moeda]
        else:
            raise ValueError(f"Criptomoeda {cripto} não encontrada.")
    
    except requests.exceptions.RequestException as e:
        return f"Erro na conexão: {str(e)}"
    
    except ValueError as e:
        return str(e)
