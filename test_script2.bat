@echo off
echo Тест 1: запуск с параметрами
python second-stage.py --vfs-path C:\my_vfs --script test.vfs

echo Тест 2: запуск только со скриптом  
python second-stage.py --script test.vfs

echo Тест 3: запуск без параметров
python second-stage.py