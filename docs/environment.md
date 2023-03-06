# Environment
This documents go through the process of managing environments. 

## Create a python virtual environment

### From zero
1. Go to the project directory
2. Create the environment 
    > python -m venv sentinel-env
3. Activate the environment
    > .\sentinel-env\Scripts\activate

### From an existing requirements.txt file
Then use the resulting requirements.txt to create a pip virtual environment:
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt


## (re)create requirements.txt
### ❤️From our local python virtual environment
> pip list --format=freeze > requirements.txt

### 💥❗ Create requirements from an anaconda environment (discourage)
You can create the requirements.txt from an anaconda environment but this 
method isn't recommended as the output isn't 100% compatible with pip
> conda list -e > requirements.txt

## Activate environment
1. Go to the project directory
2. .\sentinel-env\Scripts\activate

## Links
### requirements.txt vs setup
https://towardsdatascience.com/requirements-vs-setuptools-python-ae3ee66e28af#:~:text=The%20requirements.&text=txt%20is%20a%20file%20listing,be%20pinned%20or%20non%2Dpinned.

### create requirements.txt from conda environment
https://stackoverflow.com/questions/50777849/from-conda-create-requirements-txt-for-pip3
