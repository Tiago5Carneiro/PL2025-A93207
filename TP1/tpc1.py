text = "Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=OfF E deu-nos 7= dias para o fazer...ON Cada trabalho destes vale 0.25 valores da nota final!"

def main():
    total = 0
    soma = True

    # Temporary string to place digits when found
    num = ""

    # Variable for the printing after finding a special case
    print_index = 0

    for i, c in enumerate(text):

        # Check if char is digit and add it to the current number being parsed
        if c.isdigit():
            num += c 
        else:

            # If num is not empty add it to the total and empty it
            if num:
                if soma:
                    total += int(num)
                num = ""
            
            # Beginning the 'ON' or 'OFF' check
            if c.lower() == 'o':

                # Check if 'ON' is present
                palavra = text[i:i+2].lower()
                if palavra == "on":
                    print(text[print_index:i+2])
                    print_index = i+2
                    soma = True

                # Check if 'OFF' is present
                palavra += text[i+2].lower()
                if palavra == "off":
                    print(palavra)
                    print(text[print_index:i+3])
                    print_index = i+3
                    soma = False
        
            # In case of '=' print the total
            elif c == '=':
                print(text[print_index:i+1])
                print_index = i+1
                print(">>" + str(total))

    # Check if there is a number at the end of the text
    if num and soma:
        total += int(num)
    print(">>" + str(total))

if __name__ == "__main__":
    main()