# Import

import pandas
import os
import re
import pandas as pd

# find file
# read and get file info
# build table


# Define paras
Folder_Name_1 = "../exchanger-experiments-"
Folder_Name_2_list = "results_5000records_50k_2"
iters = ['10k', '50k']
s1_list = [i for i in range(1,2)]
s2_list = [""]
for i in range(2, 5):
    s2_list.append("-" + str(i))


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

for s1 in s1_list:
    for s2 in s2_list:
        folder2 = Folder_Name_2_list
        path = Folder_Name_1 + str(s1) + s2 + '/' + folder2
        print(path)
        if os.path.exists(path):
            entries = os.listdir(path)
            rds_files = [entry for entry in entries if entry.endswith('.rds')]
            for file in rds_files:
                os.remove(file)

