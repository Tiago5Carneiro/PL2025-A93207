import json 
import re
stock = {}

# listar
# moedas (input de dinheiro)
# selecionar
# sair

cash = 0 

def insert_coin(command):
    global cash
    coins = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}
    coins_command = command.split()[1:]
    
    for coin in coins_command:
        coin = coin.strip(".").lower()
        if coin in coins:
            cash += coins[coin]

    print(f"maq: Saldo = {cash}c")


def select(command):
    global cash
    cod_produto = command.split()[1]

    for key,item in stock.items():
        if key == cod_produto:
            if item["quant"] > 0:
                if cash >= item["preço"]*100:
                    cash -= item["preço"]*100
                    item["quant"] -= 1
                    print(f'maq: Pode retirar o produto dispensado "{item["nome"]}"')
                    print(f"maq: Saldo = {cash}c")
                else:
                    print("maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {cash}c; Pedido = {item['preço']*100}c")
            else:
                print("maq: Produto esgotado")
            return
    print("maq: Código inválido")

def list():
    print("maq:")
    print(f"{'cod':<5} | {'nome':<50} | {'quantidade':<10} | {'preço':<5}")
    print("-" * 80)
    
    for key,value in stock.items():
        print(f"{key:<5} | {value['nome']:<50} | {value['quant']:<10} | {value['preço']:<5}")

def load_stock():
    # Reading the JSON file
    data = json.load(open("dataset/stock.json", "r"))

    for item in data:
        stock[item['cod']] = item

def menu():
    moedas_regex = re.compile(r"MOEDAS")
    select_regex = re.compile(r"SELECIONAR")

    while True:
        command = input(">> ")
        if command == "LISTAR":
            list()
        elif moedas_regex.search(command):
            insert_coin(command)
        elif select_regex.search(command):
            select(command)
        elif command == "SAIR":
            print(f"maq: Podem ser retiradas as seguintes moedas: {cash}c")
            print("maq: Até à próxima")
            break
        else:
            print("maq: Comando inválido")


if __name__ == "__main__":
    load_stock()
    menu()
