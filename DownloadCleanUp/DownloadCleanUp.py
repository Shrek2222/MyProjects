import os
import re
from collections import defaultdict

def find_duplicates(folder_path):
    files_dict = defaultdict(list)
    regex = re.compile(r'\((\d+)\)$')
    
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            base_name = regex.sub('', filename.rsplit('.', 1)[0])
            files_dict[base_name].append(filename)
    
    duplicates = {key: value for key, value in files_dict.items() if len(value) > 1}
    return duplicates

def prompt_user_for_deletion(duplicates, folder_path):
    for base_name, files in duplicates.items():
        print(f"Found duplicates for: {base_name}")
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")
        
        delete_choice = input("Do you want to delete these duplicates? (y/n): ").strip().lower()
        if delete_choice == 'y':
            for file in files[1:]:
                os.remove(os.path.join(folder_path, file))
                print(f"Deleted: {file}")

def main():
    downloads_folder = os.path.expanduser("~/Downloads")
    duplicates = find_duplicates(downloads_folder)
    if duplicates:
        prompt_user_for_deletion(duplicates, downloads_folder)
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    main()

