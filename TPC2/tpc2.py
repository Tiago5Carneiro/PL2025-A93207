import re

file_path = "obras.csv"

def process_csv(file_path):
    composers = set()
    period_count = {}
    period_works = {}
    
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(';')
        
        for line in lines[1:]:
            values = re.split(r';', line.strip())
            row = dict(zip(headers, values))
            
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

    # Printing results
    print("Lista ordenada de compositores:", composers_list)
    print("\nDistribuição das obras por período:", period_distribution)
    print("\nDicionário de obras por período:", period_titles)
