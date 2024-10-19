import os

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Collect all file names in a set to track duplicates, using full paths to ensure uniqueness across all folders
file_names = set()
duplicate_files = []

# Loop through each subdirectory in the current directory
for folder in os.listdir(current_directory):
    folder_path = os.path.join(current_directory, folder)
    
    # Only process subdirectories (ignore files in the root)
    if os.path.isdir(folder_path):
        # Loop through each file in the subdirectory
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            
            # Ensure it's a file (ignore nested folders)
            if os.path.isfile(file_path):
                # Check if the file name already exists (across all folders)
                if file in file_names:
                    duplicate_files.append(file_path)  # Add to duplicates list
                else:
                    file_names.add(file)  # Add unique file names to the set

# Rename duplicate files by appending a unique suffix
for file_path in duplicate_files:
    folder = os.path.dirname(file_path)
    base, ext = os.path.splitext(os.path.basename(file_path))
    counter = 1
    new_file_name = f"{base}_{counter}{ext}"
    new_file_path = os.path.join(folder, new_file_name)

    # Keep generating a new name until it's unique across **all** folders
    while new_file_name in file_names:
        counter += 1
        new_file_name = f"{base}_{counter}{ext}"
        new_file_path = os.path.join(folder, new_file_name)

    # Rename the file and add the new name to the set
    os.rename(file_path, new_file_path)
    file_names.add(new_file_name)  # Ensure the new name is also tracked
    print(f"Renamed: {file_path} to {new_file_path}")

print("All duplicate files have been renamed.")
