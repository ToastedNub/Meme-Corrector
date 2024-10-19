import os

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Collect all file names in a set to track duplicates
file_names = set()
duplicate_files = []

# Loop through each folder in the current directory
for folder in os.listdir(current_directory):
    folder_path = os.path.join(current_directory, folder)
    if os.path.isdir(folder_path):  # Check if it's a directory
        # Loop through each file in the directory
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):  # Ensure it's a file
                if file in file_names:
                    duplicate_files.append(file_path)
                else:
                    file_names.add(file)

# Rename duplicate files by appending a unique suffix
for file_path in duplicate_files:
    base, ext = os.path.splitext(file_path)
    counter = 1
    new_file_path = f"{base}_{counter}{ext}"

    # Create a new unique name until it does not conflict
    while os.path.basename(new_file_path) in file_names:
        counter += 1
        new_file_path = f"{base}_{counter}{ext}"

    # Rename the file and add the new name to the set
    os.rename(file_path, new_file_path)
    file_names.add(os.path.basename(new_file_path))
    print(f"Renamed: {file_path} to {new_file_path}")

print("All duplicate files have been renamed.")
