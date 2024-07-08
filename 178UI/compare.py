import csv

def compare_csv_files_ignore_timestamp_and_trailing_spaces(file_a, file_b, output_file):
    # 讀取 A 檔案的內容，儲存到字典裡，忽略第三列和最後一列末尾的無效空格
    with open(file_a, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        content_a = {tuple(row[:2] + [row[3].rstrip()]) for row in reader}

    # 讀取 B 檔案的內容，儲存到字典裡，忽略第三列和最後一列末尾的無效空格
    with open(file_b, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        content_b = [row for row in reader]

    # 找出 B 檔案中，與 A 檔案不同的條目，忽略第三列和最後一列末尾的無效空格
    diff_entries = [row for row in content_b if tuple(row[:2] + [row[3].rstrip()]) not in content_a]

    # 將更改過的條目寫入 C 檔案
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in diff_entries:
            writer.writerow(row)

# 檔名
file_a = 'old.csv'    # A 檔案
file_b = 'new.csv'    # B 檔案
output_file = 'compare.csv'  # 輸出檔名

compare_csv_files_ignore_timestamp_and_trailing_spaces(file_a, file_b, output_file)
