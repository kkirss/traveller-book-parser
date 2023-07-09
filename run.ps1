python -m venv "$PSScriptRoot\.venv"
. "$PSScriptRoot\.venv\Scripts\activate.ps1"
pip install -r "$PSScriptRoot\requirements.txt" --upgrade | find /V "already satisfied"

$env:PYTHONPATH="$PSScriptRoot\src"

python "$PSScriptRoot\main.py"

Remove-Item Env:\PYTHONPATH
