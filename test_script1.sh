#!/bin/bash
echo "Тест 1: запуск с vfs-path и script"
python3 vfs_emulator.py --vfs-path /home/user/my_vfs --script test.vfs

echo "Тест 2: запуск только со script"
python3 vfs_emulator.py --script test.vfs

echo "Тест 3: запуск без параметров"
python3 vfs_emulator.py