@echo off
setlocal

REM 確認是否有拖曳檔案到此bat
if "%~1"=="" (
    echo drag backup wow.exe to .bat to replace
    pause
    exit /b 1
)

REM 獲取被拖曳的檔案完整路徑
set "source_file=%~1"

REM 獲取檔案所在的目錄
set "target_dir=%~dp1"

REM 設定目標檔案名稱為wow.exe
set "target_file=%target_dir%wow.exe"

REM 將檔案複製為wow.exe，如果wow.exe已經存在則覆蓋
copy /y "%source_file%" "%target_file%"

if exist "%target_file%" (
    echo replace wow.exe
) else (
    echo replace faild, copy failed.
)

pause
