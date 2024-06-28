import os

def merge_txt_files_in_directory():
    # 取得腳本所在資料夾的路徑
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # 取得資料夾中所有文本檔案的檔名
    file_names = [f for f in os.listdir(current_directory) if f.endswith('.txt') and f != os.path.basename(__file__)]
    # 按檔名排序
    file_names.sort()

    # 檢查資料夾中是否存在文本檔案
    if not file_names:
        print("No .txt files found in the directory.")
        return

    # 使用第一個檔案的檔名做為輸出檔的檔名
    first_file_name = file_names[0]
    output_file_name = f"{os.path.splitext(first_file_name)[0]}-merge.txt"
    output_file = os.path.join(current_directory, output_file_name)

    # 打开输出文件以写入模式
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 遍歷文本內容，以將其寫入輸出檔
        for file_name in file_names:
            file_path = os.path.join(current_directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # 添加換行符，分隔不同檔案的內容

    print(f"Merged {len(file_names)} files into {output_file}")

# 執行
merge_txt_files_in_directory()
