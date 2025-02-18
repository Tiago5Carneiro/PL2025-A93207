import os

def pagination(struct, page_size=10, is_set=False):
        
    total_pages = (len(struct) + page_size - 1) // page_size

    # In case of dictionary
    def print_page_dict(page):
        os.system('cls' if os.name == 'nt' else 'clear')
        start = page * page_size
        end = start + total_pages
        if total_pages == 1:
            items = list(struct.items())
        else :
            items = list(struct.items())[start:end]
        for id, item in items:
            print(f"Id: {id}")
            print(f"Value: {item}")
            print("\n" + "-"*80 + "\n")
        print(f"\nPage {page + 1} of {total_pages}")

    # In case of set
    def print_page_set(page):
        os.system('cls' if os.name == 'nt' else 'clear')
        start = page * page_size
        end = start + total_pages
        i = start
        for val in struct[start:end-1]:
            i+=1
            print(f"{i} - {val}")
        print("\n" + "-"*80 + "\n")
        print(f"\nPage {page + 1} of {total_pages}")

    # Page selection loop
    current_page = 0
    while True:
        if is_set:
            print_page_set(current_page)
        else :
            print_page_dict(current_page)
        command = input("Type 'n' to move to the next page, 'p' to go to the previous page, or 'q' to leave: ").strip().lower()
        if command == 'n':
            if current_page < total_pages - 1:
                current_page += 1
            else:
                print("You're already on the last page.")
                input("Press Enter to continue...")
        elif command == 'p':
            if current_page > 0:
                current_page -= 1
            else:
                print("You're already on the first page.")
                input("Press Enter to continue...")
        elif command == 'q':
            break
        else:
            print("Invalid command, type 'n', 'p' or 'q'.")
            input("Press Enter to continue...")