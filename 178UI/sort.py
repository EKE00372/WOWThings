import csv
import re

def sort_csv_by_name(input_file, output_file):
    def sort_key(name):
        return re.sub(r'\[.*?\]', '', name).strip()

    # 讀取 csv 檔案
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # 根據名字創建輔助排序
    for row in rows:
        row['sort_key'] = sort_key(row['name'])

    # 排序
    rows_sorted = sorted(rows, key=lambda x: x['sort_key'])

    # 刪除輔助排序並獲取列名
    for row in rows_sorted:
        del row['sort_key']
    fieldnames = reader.fieldnames

    # 將排序後的資料輸出到新的 csv 檔案
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_sorted)

# 檔名
input_file = 'ui_wow.csv'   # 輸入檔名
output_file = 'ui_wow_sort.csv' # 輸出檔名

sort_csv_by_name(input_file, output_file)
