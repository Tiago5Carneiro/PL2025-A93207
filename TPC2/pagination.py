import os

def pagination(dict, page_size=10):
        
    total_pages = (len(dict) + page_size - 1) // page_size

    def print_page(page):
        os.system('cls' if os.name == 'nt' else 'clear')
        start = page * page_size
        end = start + total_pages
        for item, id in dict[start:end]:
            print(f"Id: {id}")
            for key, value in item.items():
                print(f"  {key}: {value}")
            print("\n" + "-"*80 + "\n")
        print(f"\nPage {page + 1} of {total_pages}")

    current_page = 0
    while True:
        print_page(current_page)
        command = input("Type 'n' to move to the next page, 'p' to go to the previous page, or 'q' to leave: ").strip().lower()
        if command == 'n':
            if current_page < total_pages - 1:
                current_page += 1
            else:
                print("You're already on the last page.")
        elif command == 'p':
            if current_page > 0:
                current_page -= 1
            else:
                print("You're already on the first page.")
        elif command == 'q':
            break
        else:
            print("Invalid command, type 'n', 'p' or 'q'.")