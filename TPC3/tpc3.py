import re
# Syntax : 
# Title - # Example
# Bold **example**
# Italic *example*
# Image ![example](example.jpg)
# Link [example](example.com)
# List 1. example

def apply_header(line):
    title = re.split(r'#', line)
    output = line
    if len(title)>1:
        header = 0
        for segment in title:
            if segment == "":
                header += 1
            else:
                break
        header_str = str(header)
        output = "<h" + header_str + ">"+line[header:][:-1]+"</h" + header_str + ">\n"
    return output

def apply_bold(line):
    text = re.split(r'\*\*', line)    
    output = line
    if len(text) > 1:
        output = ""
        for i,segment in enumerate(text):
            if i % 2 == 1:
                output += "<b>"+segment+"</b>"
            else:
                output += segment
    return output

def apply_italic(line):
    text = re.split(r'\*', line)
    output = line
    if len(text) > 1:
        output = ""
        for i,segment in enumerate(text):
            print(text)
            if i % 2 == 1:
                output += "<i>"+segment+"</i>"
            else:
                output += segment
    return output
    

def parse_line(line, is_list):
    processed_line = line
    temp_line = ""
    was_list = False
    # Header
    processed_line = apply_header(processed_line)
    
    # List

    list = re.split(r'[1-9]+\.', processed_line)
    if len(list) > 1:
        is_list +=1
        print(is_list)
        for i,segment in enumerate(list):
            if i == 0 and is_list == 1 and segment == "":
                temp_line += "<ol>\n"
            elif i ==1:
                temp_line += "<li>"+segment[:-1]+"</li>\n"
        processed_line = temp_line
    elif is_list > 0:
        is_list = 0
        was_list = True

    # Bold
    processed_line = apply_bold(processed_line)

    # Italic
    processed_line = apply_italic(processed_line)
    if was_list:
        processed_line += "</ol>\n"
    return processed_line, is_list

def generate_html(file_path):

    html = open(file_path[:-3]+".html", "w")
    with open(file_path, encoding='utf-8') as file:
        content = file.readlines()
        is_list = 0
        for line in content:
            new_line, is_list = parse_line(line, is_list)
            html.write(new_line)
        if is_list > 0:
            html.write("</ol>\n")
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