import os
import re
from qdafile import QDAfile

# ディレクトリにあるtxtファイルの名前のリストを取得する関数
def get_txt_list(directory):
    txt_list = []
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            txt_list.append(file)
    return txt_list

#txtファイルの名前のリストをソートする関数
#filenameの形式　yyyymmdd_reactant_ion_eq_solvent_nuL.txt
#yyyymmddは日付、reactantは反応物、ionはイオン、eqは当量、solventは溶媒、nuLは滴下したイオンの量
#滴下したイオンの量でソートする
def sort_txt_list(txt_list):
    def extract_number(filename):
        # ファイル名の最後の部分から単位を除き数値を取得
        last = filename.split('_')[-1].split('.')[0]
        last = re.sub(r'(μL|µL|uL)$', '', last)
        try:
            return int(last)
        except ValueError:
            return float('inf')  # 数値が見つからない場合は無限大を返す

    txt_list.sort(key=extract_number)
    nuL_list = []
    for txt in txt_list:
        # ファイル名の最後の部分を取得し、単位を除いて数値に変換
        last = txt.split('_')[-1].split('.')[0]
        last = re.sub(r'(μL|µL|uL)$', '', last)
        nuL_list.append(last)
    
    for i in range(len(nuL_list)):
        nuL_list[i] = int(nuL_list[i])
    
    return txt_list, nuL_list

# tab区切りのtxtファイルを読み込む関数
def read_txt(file_path):
    with open(file_path, 'r', encoding='shift_jis') as file:
        data = file.readlines()
    
    # 空行や変換できない文字列をスキップ
    processed_data = {}
    for line in data:
        try:
            processed_line = [float(x) for x in line.split()]
            if len(processed_line) >= 2:
                processed_data[processed_line[0]] = processed_line[1]
        except ValueError:
            continue
    
    return processed_data

# ディレクトリにあるtxtファイルを読み込んで、辞書に格納する関数
# 辞書のキーは波長、値は吸光度
def read_txts(directory):
    txt_list = get_txt_list(directory)
    txt_list, nuL_list = sort_txt_list(txt_list)
    list_of_data = []
    for txt in txt_list:
        list_of_data.append(read_txt(os.path.join(directory, txt)))
    return list_of_data, nuL_list

# qdaを作成する関数
# dataには2次元リストを格納する。
# data = [[wavelength1, wavelength2, ...], [absorbance1-1, absorbance1-2, ...], [absorbance2-1, absorbance2-2, ...], ...]
def create_qda_file(directory, output_file):
    # 全ての波長を取得
    list_of_data, nuL_list = read_txts(directory)
    all_wavelengths = sorted(set().union(*[data.keys() for data in list_of_data]))
    
    # 吸光度データを並べる
    qda_data = []
    qda_data.append(all_wavelengths)
    for data in list_of_data:
        qda_data.append([data.get(wavelength, 0) for wavelength in all_wavelengths])
    
    # QDAファイルに書き込む
    headers = ['Wavelength']
    for nuL in nuL_list:
        headers.append(f'{nuL}uL')
    
    dtypes = ['>f8'] * len(headers)
    
    qda = QDAfile(qda_data, headers=headers, dtypes=dtypes)
    qda.write(output_file)
