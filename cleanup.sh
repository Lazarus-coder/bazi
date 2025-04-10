#!/bin/bash

# Create a backup of the original project
mkdir -p backup
cp -r *.py backup/
cp -r README.md backup/

# Remove unnecessary files
rm -f shengxiao.py
rm -f luohou.py

# Keep only the essential files
essential_files=(
  "bazi.py"
  "common.py" 
  "convert.py"
  "datas.py"
  "ganzhi.py"
  "sizi.py"
  "yue.py"
)

# Copy the new README
cp README_TRIMMED.md README.md

echo "Project cleaned up. Removed shengxiao.py and luohou.py."
echo "Essential files kept: ${essential_files[*]}"
echo "Original files backed up to ./backup/"
echo "To test the program, run: python bazi.py -g 1990 8 23 12" 