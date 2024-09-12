import requests

url = "http://www.google.com.br"

try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a resposta tem um código de status 2xx (sucesso)
    print(f"O site {url} está acessível.")
except requests.exceptions.RequestException as e:
    print(f"Não foi possível acessar o site {url}. O erro foi: {e}")