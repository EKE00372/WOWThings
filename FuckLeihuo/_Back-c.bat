@echo off
setlocal

REM 設定文件路徑
set "wow_exe_path=D:\World of Warcraft\_retail_\Wow.exe"

REM 提取文件版本信息
for /f "tokens=2 delims==" %%A in ('wmic datafile where name^="%wow_exe_path:\=\\%" get Version /value') do set "version=%%A"

echo Get version info: %version%

REM 檢查版本是否成功提取
if "%version%"=="" (
    echo Cannot get version info
    pause
    exit /b 1
)

REM 提取版本號的最後一部分
for /f "tokens=4 delims=." %%B in ("%version%") do set "build_number=%%B"

echo build number: %build_number%

REM 構建備份文件名
set "backup_file=Wow-%build_number%-c.exe"

REM 備份文件
copy "%wow_exe_path%" "%backup_file%"

if exist "%backup_file%" (
    echo Backup finish: %backup_file%
) else (
    echo Backup failed
)

pause
