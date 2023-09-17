--------------- SETUP ---------------

# installs pipenv
pip install pipenv

# Check Python version
python -version

# Sets virtual environment directory
set WORKON_HOME=D:\Programming\virtual-environments

# To check whether properly set:
echo $Env:WORKON_HOME

# Create a virtual environment with --python 3.11.5
pipenv --python 3.11.5 (to create virtual environment)

# Activate the environment (like go into that environment)
pipenv shell

# Install the requirements (within the environment if activated)
pipenv install -r requirements.txt

# Pipenv location
Get-Command pipenv

-------------- RUN -----------------
in terminal directory with pipenv shell

pipenv run streamlit run "d:/AI programming/1_PROJECTS/GORILLA_LLM/app.py"

OR

pipenv shell
streamlit run "d:/AI programming/1_PROJECTS/GORILLA_LLM/app.py"


------------ POST COMPLETION ------------------

# Generate a requirements.txt from my pipfile.lock

pipenv lock -r

# pipenv lock (to pin down exact versions of dependencies)
pipenv lock


---------------- OTHER COMMANDS ------------------
# Check location of shell
pipenv --venv

# Check installed packages
pipenv run pip freeze
