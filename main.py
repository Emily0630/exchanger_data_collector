# Import

import pandas
import os


# Define paras
Folder_Name_1 = "exchanger-experiments"
Folder_Name_2 = "results_10k"
suffix1_1 = []
for i in range(1,13):
    suffix1_1.append("-" + str(i))
suffix1_2 = ["", "-2"]
suffix2 = [""]
for i in range(2,21):
    suffix2.append("_" + str(i))

print(suffix1_1)

# In for loop

txt_files_contents = {}

for s1_1 in suffix1_1:
    for s1_2 in suffix1_2:
        for s2  in suffix2:
            path = Folder_Name_1 + s1_1 + s1_2 + '/' + Folder_Name_1 + s2
            entries = os.listdir(path)
            txt_files = [entry for entry in entries if entry.endswith('.txt')]
            for file in txt_files:
                file_path = os.path.join(path, file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read the content of the file
                    content = file.read()
                    # Store the content with the file name as key
                    txt_files_contents[file_path] = content


for file_path, content in txt_files_contents.items():
    print(f"Contents of {file_path}:")
    print(content)
    print("----------")