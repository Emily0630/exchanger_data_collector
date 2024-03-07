# Import

import pandas
import os
import re
import pandas as pd

# find file
# read and get file info
# build table


# Define paras
Folder_Name_1 = "../exchanger-experiments"
Folder_Name_2 = "results_BNBD"
iters = ['10k', '50k']
s1_cs2_dic = {
    1:[1,2,3,4],
    2:[1,2,3,4],
    4:[1,2,3,4],
    5:[1,2],
    7:[1,2,3,4],
    8:[1,2],
    10:[1,2,3,4],
    11:[1,2],
}
s1_cs10_dic = {
    3:[1,2,3,4,5,6,7,8],
    5:[3,4],
    6:[1,2,3,4],
    8:[3,4],
    9:[1,2,3,4],
    11:[3,4],
    12:[1,2,3,4]
}



suffix1_2 = []
suffix1_10 = []
for i in s1_cs2_dic:
    for j in s1_cs2_dic[i]:
        if j == 1:
            suffix1_2.append(i)
        else:
            suffix1_2.append(f"{i}-{j}")
for i in s1_cs10_dic:
    for j in s1_cs10_dic[i]:
        if j == 1:
            suffix1_10.append(i)
        else:
            suffix1_10.append(f"{i}-{j}")


suffix2 = ["10k", "50k"]
for i in ["10k", "50k"]:
    for j in range(1, 9):
        suffix2.append(f"{i}_{j}")

# print(suffix1_1)

# Helper Functions

def find_string_in_filename(filename):
    pattern = re.compile(r'synthdata_link-conf-mu-(.*?)_dist-conf-(.*?)_seed-0_ours_coupon_(.*?)_eval\.txt')

    match = pattern.search(filename)
    if match:
        # Extract string1 and string2 from the file name
        string1, string2, date = match.groups()
        return string1, string2, date


def read_content_from_file(content):
    patterns = {
        'precision': r'\$precision\s*\[1\]\s*(\d+\.?\d*)',
        'recall': r'\$recall\s*\[1\]\s*(\d+\.?\d*)',
        'f1score': r'\$f1score\s*\[1\]\s*(\d+\.?\d*)'
    }

    # Dictionary to hold the values of each metric
    metrics = {}

    # Search for the patterns in the file content and extract the numeric values
    for metric, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            metrics[metric] = float(match.group(1))
    return metrics

# In for loop

txt_files_contents = {}

df_entries = []
# new_entry = {
#     'round': [],
#     'split': [],
#     'replicates': [],
#     'duplicates': [],
#     'distortion': [],
#     'm1': [],
#     'm2': [],
#     'm3': []
# }

for s1_1 in suffix1_1:
    print(s1_1)
    for s2  in suffix2:
        path = Folder_Name_1 + s1_1 + '/' + Folder_Name_2 + s2
        if os.path.exists(path):
            entries = os.listdir(path)
            txt_files = [entry for entry in entries if entry.endswith('.txt')]
            for file in txt_files:
                s3, s4, date = find_string_in_filename(file)
                file_path = os.path.join(path, file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read the content of the file
                    content = file.read()
                    metric = read_content_from_file(content)
                    new_entry = {
                        'round': s1_1,
                        'replicates': s2,
                        'duplicates': s3,
                        'distortion': s4,
                        'm1': metric['precision'],
                        'm2': metric['recall'],
                        'm3': metric['f1score'],
                        "date": date,
                    }
                    df_entries.append(new_entry)

print(len(df_entries))
entry_df = pd.DataFrame(df_entries)
entry_df.to_csv("data.csv")

