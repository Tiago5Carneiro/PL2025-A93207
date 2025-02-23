import re
import subprocess
import pyautogui
import time

last_html_generated = "dataset/test.md"

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

def apply_list(line,is_list,was_list):
    list = re.split(r'[1-9]+\.', line)
    output = line
    if len(list) > 1:
        output = ""
        is_list +=1
        for i,segment in enumerate(list):
            if i == 0 and is_list == 1 and segment == "":
                output += "<ol>\n"
            elif i ==1:
                output += "<li>"+segment[:-1]+"</li>\n"
    elif is_list > 0:
        is_list = 0
        was_list = True
    return output, is_list, was_list

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
            if i % 2 == 1:
                output += "<i>"+segment+"</i>"
            else:
                output += segment
    return output
    
def apply_image(line):
    image = re.split(r'\!\[', line)
    output = line

    if len(image) > 1:
        output = ""
        for i,segment in enumerate(image):
            if i >= 1:
                image_props = re.split(r'\)',image[i])
                
                for j,segment in enumerate(image_props):
                    if j == 0:
                        image_props = re.split(r'\]\(',segment)
                        output += "<img src=\"" + image_props[1]+ "\" alt=\"" + image_props[0]+ "\">"
                    elif j % 2 == 1 and segment != "":
                        output += segment
                        output += ')'  
                    else:
                        output += segment
            else:
                output += segment
    return output

def apply_link(line):
    link = re.split(r'\[', line)
    output = line
    if len(link) > 1:
        output = ""
        for i,segment in enumerate(link):
            if i >= 1:
                link_props = re.split(r'\)',link[i])
                
                for j,segment in enumerate(link_props):
                    if j == 0:
                        link_props = re.split(r'\]\(',segment)
                        output += "<a href=\""+link_props[1]+"\">"+link_props[0]+"</a>"
                    else :
                        output += segment
            else:
                output += segment
    print("Link output",output)
    return output

def parse_line(line, is_list):
    processed_line = line
    temp_line = ""
    was_list = False
    # Header
    processed_line = apply_header(processed_line)
    
    # List

    processed_line, is_list, was_list = apply_list(processed_line,is_list,was_list)

    # Bold
    processed_line = apply_bold(processed_line)

    # Italic
    processed_line = apply_italic(processed_line)

    # Image
    processed_line = apply_image(processed_line)

    # Link
    processed_line = apply_link(processed_line)

    if was_list:
        processed_line = "</ol>\n" + processed_line
    return processed_line, is_list

def generate_html(file_path):

    # Change file if was given
    if file_path != "":
        last_html_generated = file_path[:-3]+".html"

    # going from dataset/test.md to output/test.html
    last_html_generated = re.sub(r'.*/', 'output/', file_path)
    last_html_generated = last_html_generated[:-3]+".html"

    # Open the file
    html = open(last_html_generated, "w")
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
            file_path = input("Enter the file path (leave empty for the default test to be used): ")
            file_path = "dataset/test.md"
            generate_html(file_path)
        elif option == '2':
            print("Opening html on local host")
            try:
                html_file = re.sub(r'.*/','output/',last_html_generated)
                html_file = html_file[:-3]+".html"
                server_process = subprocess.Popen(["live-server",html_file])
                print("Live Server is running. Press Enter to stop it...")
                input()  # Wait for user input

                # Stop the Live Server process
                server_process.terminate()
                print("Live Server stopped.")
            except:
                print("Please install live-server with npm wigth the command: npm install -g live-server")
        elif option == '3':
            print("Goodbye!")
            break

def main():
    menu()

if __name__ == "__main__":
    main()