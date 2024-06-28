import os

def update_log_files_in_directory():
    # 取得腳本所在資料夾的路徑
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # 取得資料夾中所有文本檔案的檔名
    file_names = [f for f in os.listdir(current_directory) if f.endswith('.txt')]
    
    for file_name in file_names:
        file_path = os.path.join(current_directory, file_name)
        
        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 修改內容
        updated_lines = []
        for line in lines:
            updated_lines.append(line.replace("ADVANCED_LOG_ENABLED,0", "ADVANCED_LOG_ENABLED,1"))
        
        # 寫入檔案中
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
        
        print(f"Updated log file: {file_path}")

# 執行
update_log_files_in_directory()
