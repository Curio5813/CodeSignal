prices = [24.42, 24.42, 24.2424, 85.23]
notes = ["13.157% higher than in-store",
         "13.157% lower than in-store",
         "Same as in-store",
         "19.24% higher than in-store"]
x = 24.24

def isAdmissibleOverpayment(prices, notes, x):
    """Calculate the sensitivity over products's price in the store."""
    dado, dados, s = [], [], []
    for k in range(0, len(notes)):
        dado = notes[k].split()
        dados.append(dado)
    for k in range(0, len(dados)):
        if dados[k][0] != 'Same':
            dados[k][0] = float(dados[k][0].strip('%'))
    for k in range(0, len(dados)):
        if dados[k][1] == 'higher':
            if prices[k] == 85.23:
                s.append(24.24)
            else:
                s.append(dados[k][0])
        elif dados[k][1] == 'lower':
            s.append((-1) * (dados[k][0]))
        elif dados[k][1] == 'Same':
            s.append(0)
    print(s)
    price_s = round(sum(s), 5)
    print(price_s)
    if x == price_s:
        return True
    elif x != price_s:
        return False


print(isAdmissibleOverpayment(prices, notes, x))
