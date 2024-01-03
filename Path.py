from pathlib import Path
path=Path("ecommerce")
print(path.exists())

# path1=Path("emails")
# path1.mkdir()
# path1.rmdir()

path=Path()
# for file in path.glob('*.*'): # 列出所有檔案有.的
# for file in path.glob('*.py'): # 列出所有.py的檔案
for file in path.glob('*'): # 列出所有檔案
    print(file)