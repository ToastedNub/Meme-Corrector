import os

current_directory = os.path.dirname(os.path.abspath(__file__))

file_names = set()
duplicate_files = []

for folder in os.listdir(current_directory):
    folder_path = os.path.join(current_directory, folder)
    
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            
            if os.path.isfile(file_path):
                if file in file_names:
                    duplicate_files.append(file_path)
                else:
                    file_names.add(file)

for file_path in duplicate_files:
    folder = os.path.dirname(file_path)
    base, ext = os.path.splitext(os.path.basename(file_path))
    counter = 1
    new_file_name = f"{base}_{counter}{ext}"
    new_file_path = os.path.join(folder, new_file_name)

    while new_file_name in file_names:
        counter += 1
        new_file_name = f"{base}_{counter}{ext}"
        new_file_path = os.path.join(folder, new_file_name)

    os.rename(file_path, new_file_path)
    file_names.add(new_file_name)  
    print(f"Renamed: {file_path} to {new_file_path}")

print("All duplicate files have been renamed.")
