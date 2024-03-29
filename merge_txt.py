# @作用：合并多个sql文件
# @输入：文件路径：input_path，输出路径：output_path
# @输出：merge.sql
# @用法：直接运行
import os
import time
from tqdm import tqdm
input_path = "data/"
output_path = "merged_GGPoker/"
if not os.path.exists(output_path):
    os.mkdir(output_path)
suffix = ".txt"
files = []
for file in os.listdir(input_path):
    file_path = os.path.join(file)
    if os.path.splitext(file_path)[1] == suffix:
        files.append(file_path)
# print("files:", files)
file_num = len(files)
# print(file_num)
# result = open(output_path + 'merged_SQL_Joint_LuJia.sql', 'w', encoding='utf-8')
result = open(output_path + 'merged.txt', 'w', encoding='utf-8')
for i in tqdm(range(file_num)):
    # print(input_path+files[i])
    file = open(input_path + files[i], 'r', encoding='utf-8')
    lines = file.readlines()
    result.writelines(lines)
result.close()
