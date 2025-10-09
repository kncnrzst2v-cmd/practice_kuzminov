@echo off
echo Тест 1: запуск с параметрами
python vfs_emulator.py --vfs-path C:\my_vfs --script test.vfs

echo Тест 2: запуск только со скриптом  
python vfs_emulator.py --script test.vfs

echo Тест 3: запуск без параметров
python vfs_emulator.py