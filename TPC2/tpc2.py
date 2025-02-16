import re
from pagination import pagination

file_path = "obras.csv"

def process_csv(file_path):
    composers = set()
    period_count = {}
    period_works = {}
    
    with open(file_path, encoding='utf-8') as file:

        # Reading the first line to get the headers
        head = file.readline().strip()
        headers = re.split(r';', head)

        # Reading the whole content to its own variable 
        content = file.read()

        # Defining the regex pattern, using non capturing groups, and considering that the id is using O instead of 0
        # Catching name : ([^;]+);
        # Catching description : ("(?:[^"]|"")*"|[^;]*); - Catches descriptions considering they had brackets ("), also 
        # considering that it can be empty (""), and doesn't capture the subgroup of the discription that disregards the brackets
        # Catching creation year : (\d{4});
        # Catching period : ([^;]+);
        # Catching composer : ([^;]+);
        # Catching duration : (\d{2}:\d{2}:\d{2});
        # Catching id : (?:O\d+)$
        regex = r'^([^;]+);("(?:[^"]|"")*"|[^;]*);(\d{4});([^;]+);([^;]+);(\d{2}:\d{2}:\d{2});(O\d+)$'
        
        # Find all matches  
        matches = re.findall(regex, content,re.MULTILINE)
    
        # Iterating over the matches
        for match in matches:
            
            # Creating tuple list with headers and its respective values for this row
            row = dict(zip(headers, match))
            composers.add(row['compositor'])
            
            # Adding the period in this row to the period count
            if row['periodo'] in period_count:
                period_count[row['periodo']] += 1
            else:
                period_count[row['periodo']] = 1
            
            # Adding the period in this row to the period works
            if row['periodo'] in period_works:
                period_works[row['periodo']].append(row['nome'])
            else:
                period_works[row['periodo']] = [row['nome']]
    
    # Sorting the composers and the period works after parsing the whole CSV
    sorted_composers = sorted(composers)
    for period in period_works:
        period_works[period].sort()

    # Returning all the structures created
    return sorted_composers, period_count, period_works

# Main with menu to choose the options
def main():
    composers_list, period_distribution, period_titles = process_csv(file_path)

    # Menu
    def menu():
        print("1 - Ordered writer list")
        print("2 - Work's distribution by period")
        print("3 - Work's dictionary by period")
        print("4 - Sair")
    
    while True:
        menu()
        option = input("Choose an option : ")
        
        if option == '1':
            print("\nOrdered writer list:")
            pagination(composers_list,is_set=True)
        elif option == '2':
            print("\nWork's distribution by period:")
            pagination(period_distribution)
        elif option == '3':
            pagination(period_titles)
            print("\nWork's dictionary by period:")
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
