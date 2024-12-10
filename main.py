from qda_function import create_qda_file
import os

# dataフォルダ内のフォルダ名をすべてリストに格納する
# ここでは、'data'フォルダ内のフォルダ名を取得する
folder_list = os.listdir('data')
print(folder_list)

# dataフォルダ内の各フォルダに対してqdaファイルを作成する
for folder in folder_list:
    directory = os.path.join('data', folder)
    if os.path.isdir(directory):
        create_qda_file(directory, f'{folder}.qda')
    else:
        print(f"Skipping non-directory: {directory}")