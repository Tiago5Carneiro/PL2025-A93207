import re
from pagination import pagination

file_path = "obras.csv"

def process_csv(file_path):
    composers = set()
    period_count = {}
    period_works = {}
    
    with open(file_path, encoding='utf-8') as file:

        lines = file.readlines()
        headers = lines[0].strip().split(';')
        
        for line in lines[1:]:
            line_vals = re.split(r';', line.strip())
            row = dict(zip(headers, line_vals))
            print(row)
            composers.add(row['compositor'])
            
            if row['periodo'] in period_count:
                period_count[row['periodo']] += 1
            else:
                period_count[row['periodo']] = 1
            
            if row['periodo'] in period_works:
                period_works[row['periodo']].append(row['nome'])
            else:
                period_works[row['periodo']] = [row['nome']]
    
    sorted_composers = sorted(composers)
    
    for period in period_works:
        period_works[period].sort()
    
    return sorted_composers, period_count, period_works

# Example usage
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
            pagination(composers_list)
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
