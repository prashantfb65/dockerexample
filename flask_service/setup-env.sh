export INNOV_DB_DATA=${HOME}/innovation/project/database/db
#!/bin/sh
mkdir -p $HOME/.pythonvenv
python3 -m venv $HOME/.pythonvenv/innovation
source $HOME/.pythonvenv/innovation/bin/activate
export PATH="$HOME/.pythonvenv/innovation/bin:$PATH"
export PYTHONDONTWRITEBYTECODE=1
