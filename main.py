# Import

import pandas
import os
import re

# find file
# read and get file info
# build table


# Define paras
Folder_Name_1 = "../exchanger-experiments"
Folder_Name_2 = "results_10k"
suffix1_1 = []
for i in range(1,13):
    suffix1_1.append("-" + str(i))
suffix1_2 = ["", "-2"]
suffix2 = [""]
for i in range(2,21):
    suffix2.append("_" + str(i))

# print(suffix1_1)

# Helper Functions

def find_string_in_filename(filename):
    pattern = re.compile(r'synthdata_link-conf-mu-(.*?)_dist-conf-(.*?)_seed-0_ours_coupon_[\w_]+_[\d_]+_eval\.txt')

    match = pattern.search(filename)
    if match:
        # Extract string1 and string2 from the file name
        string1, string2 = match.groups()
        return string1, string2


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

for s1_1 in suffix1_1:
    for s1_2 in suffix1_2:
        for s2  in suffix2:
            path = Folder_Name_1 + s1_1 + s1_2 + '/' + Folder_Name_2 + s2
            if os.path.exists(path):
                entries = os.listdir(path)
                txt_files = [entry for entry in entries if entry.endswith('.txt')]
                for file in txt_files:
                    s3, s4 = find_string_in_filename(file)
                    print(file, s3, s4)
                    file_path = os.path.join(path, file)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        # Read the content of the file
                        content = file.read()
                        metric = read_content_from_file(content)
                        print(metric)





