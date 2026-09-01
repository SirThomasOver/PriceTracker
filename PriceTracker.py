nome = input("Olá, eu sou o PriceTracker! antes de começarmos, qual seu nome?")
url = input("É um prazer te conhecer, " + nome + "! Vamos rastrear nosso produto? Cole aqui o URL do produto: ")
while url == "":
    url = input("Ops! Parece que você não digitou nada. Por favor, cole o URL do produto: ")
while url != "":
    try:
        import urllib.request
        urllib.request.urlopen(url)
        print("Link válido! Vamos continuar.")
        break
    except:
        url = input("Ops! Parece que o link não está funcionando. Por favor, reinsira o URL e tente novamente.")
print("URL cadastrada:", url) 
