import re
from pathlib import Path
import pathlib

# 需要替换版本号的文件
current_path = Path.cwd()
paths = [Path(f"{current_path}/src/statscalculation/__init__.py"), Path(f"{current_path}/pyproject.toml")]

# pattern
# pattern = f""

for path in paths:
    with path.open("r") as f:
        content = f.read()
        print(content)