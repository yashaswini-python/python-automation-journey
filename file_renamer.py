import os

# CHANGE this to a folder on your computer that contains test files
folder = r"C:\Users\YourName\Desktop\test_files"

files = os.listdir(folder)

for i, filename in enumerate(files, start=1):
    old_path = os.path.join(folder, filename)
    
    name, ext = os.path.splitext(filename)  # keep the extension
    new_name = f"renamed_file_{i}{ext}"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")

print("Done!")
