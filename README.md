# python-automation-journey
My journey learning Python Automation (Selenium, scraping, PDFs, APIs, etc.)

import os

# CHANGE THIS path to your test folder
folder = r"C:\Users\yashan_vyuhpharma\OneDrive\Documents\yashu"

files = os.listdir(folder)

for i, filename in enumerate(files, start=1):
    old_path = os.path.join(folder, filename)
    # keep same extension
    name, ext = os.path.splitext(filename)
    new_name = f"renamed_file_{i}{ext}"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")

print("Done!")
