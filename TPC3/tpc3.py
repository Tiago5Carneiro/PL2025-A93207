import re
import subprocess

last_html_generated = "dataset/test.md"

# Regular expressions precompiled
header_regex = re.compile(r' *#')
list_regex = re.compile(r'^[1-9]+\.')
bold_regex = re.compile(r'(.*?)\*\*(.*?)\*\*(.*?)')
italic_regex = re.compile(r'(.*?)\*(.*?)\*(.*?)')
image_regex = re.compile(r'(.*?)!\[(.*?)\]\((.*?)\)(.*?)')
link_regex = re.compile(r'(.*?)\[(.*?)\]\((.*?)\)(.*?)')

# Replaces '#' with the correspondent header tag
def apply_header(line):

    # Splitting the line to check if it is a header
    title = header_regex.split(line)
    output = line

    # If '#' exists
    if len(title)>1:
        header = 0
        print(title)
        # Counting the number of '#' to know which header tag to use
        for segment in title:
            if segment == "":
                header += 1
            elif segment == " ":
                pass
            else :
                break
        
        # If it is a valid header
        if 0 < header <= 6:
            
            header_str = str(header)

            # Removing the '#' and '\n' from the line
            output = "<h" + header_str + ">"+line[header:][1:-1]+"</h" + header_str + ">\n"

    return output

# Opens ordered list and/or adds list items
def apply_list(line,was_list):

    # Splitting the line to check if it is a list
    list = list_regex.split(line)

    # If there is a list
    if len(list) > 1:

        line = ""

        # For each segment in the list
        for i,segment in enumerate(list):
            
            # If it is the first segment and it is the first element of the list
            if i == 0 and was_list==False :
                was_list = True
                line += "<ol>\n"

            # The 2nd segment is a list item
            elif i ==1:
                line += "<li>"+segment[1:-1]+"</li>\n"

    # If it is not a list and is_list is greater than 0 it means it was a list previously
    elif was_list:
        line = "</ol>\n" + line
        was_list = False

    return line, was_list

# Replaces '**' with the correspondent bold tag
def apply_bold(line):
    output = bold_regex.sub(r'\1<b>\2</b>\3', line)
    return output

# Replaces '*' with the correspondent italic tag
def apply_italic(line):
    output = italic_regex.sub(r'\1<i>\2</i>\3', line)
    return output

# Replaces '![alt](src)' with the correspondent image tag
def apply_image(line):
    output = image_regex.sub(r'\1<img src="\3" alt="\2">\4', line)
    return output

# Replaces '[text](link)' with the correspondent link tag
def apply_link(line):
    output = link_regex.sub(r'\1<a href="\3">\2</a>\4', line)
    return output

# Parses the line and applies the correspondent tags
def parse_line(line,was_list):

    # Header
    line = apply_header(line)
    
    # List
    line, was_list = apply_list(line,was_list)

    # Bold
    line = apply_bold(line)

    # Italic
    line = apply_italic(line)

    # Image
    line = apply_image(line)

    # Link
    line = apply_link(line)

    return line,was_list

def generate_html(file_path):

    # Change file if was given
    if file_path != "":
        last_html_generated = file_path[:-3]+".html"

    # going from dataset/test.md to output/test.html
    last_html_generated = re.sub(r'.*/', 'output/', file_path)
    last_html_generated = last_html_generated[:-3]+".html"

    # Openning the file output file
    html = open(last_html_generated, "w")

    # Openning the file to be read
    with open(file_path, encoding='utf-8') as file:

        content = file.readlines()

        # Keeping track if the list was open
        was_list = False

        for line in content:

            # Parsing the line
            new_line,was_list = parse_line(line,was_list)

            # Writing the line to the html file
            html.write(new_line)
        
        # Closing the list if it was open at the end of the file
        if was_list:
            html.write("</ol>\n")

    html.close()
            
def menu():
    
    while True:
        print("1 - Generate html from file")
        print("2 - Open html on local host")
        print("3 - Exit")
    
        option = input("Choose an option : ")

        # Generate html from file, empty for default test
        if option == '1':
            file_path = input("Enter the file path (leave empty for the default test to be used): ")
            file_path = "dataset/test.md"
            generate_html(file_path)
        
        # Open html on local host
        elif option == '2':
            print("Opening last html file used on local host")

            try:
                
                # Going from dataset/test.html to output/test.md
                html_file = re.sub(r'.*/','output/',last_html_generated)
                html_file = html_file[:-3]+".html"

                # Open the Live Server process
                server_process = subprocess.Popen(["live-server",html_file])
                print("Live Server is running. Press Enter to stop it...")
                input()

                # Stopping the Live Server process
                server_process.terminate()
                print("Live Server stopped.")

            except:

                # If live-server is not installed
                print("Please install live-server with npm wigth the command: npm install -g live-server")

        # Exit
        elif option == '3':
            print("Goodbye!")
            break

def main():
    menu()

if __name__ == "__main__":
    main()