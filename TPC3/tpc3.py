import re
# Syntax : 
# Title - # Example
# Bold **example**
# Italic *example*
# Image ![example](example.jpg)
# Link [example](example.com)
# List 1. example


def generate_html(file_path):
    html = open(file_path[:-3]+".html", "a")
    with open(file_path, encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            processed_line = line
            temp_line = ""

            # Header
            title = re.split(r'#', processed_line)
            if len(title)>1:
                header = 0
                for segment in title:
                    if segment == "":
                        header += 1
                    else:
                        break
                header_str = str(header)
                processed_line = "<h" + header_str + ">"+line[header:][:-1]+"</h" + header_str + ">"

            # Bold
            text = re.split(r'\*\*', processed_line)    
            if len(text) > 1:
                for i,segment in enumerate(text):
                    if i % 2 == 1:
                        temp_line += "<b>"+segment+"</b>"
                    else:
                        temp_line += segment
                processed_line = temp_line

            # Italic
            text = re.split(r'\*', processed_line)
            temp_line = ""
            if len(text) > 1:
                for i,segment in enumerate(text):
                    if i % 2 == 1:
                        temp_line += "<i>"+segment+"</i>"
                    else:
                        temp_line += segment
                processed_line = temp_line
            html.write(processed_line)


    html.close()
            
def menu():
    
    while True:
        print("1 - Generate html from file")
        print("2 - Open html on local host")
        print("3 - Exit")
    
        option = input("Choose an option : ")

        if option == '1':
            file_path = input("Enter the file path: ")
            file_path = "dataset/test.md"
            generate_html(file_path)
        elif option == '2':
            print("Opening html on local host")
        elif option == '3':
            print("Goodbye!")
            break

def main():
    menu()

if __name__ == "__main__":
    main()