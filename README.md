# test_de_python_v2

# setup

the project is not publicly available in pip repositories, you have to clone it and build your pip package :

    # clone the repository
    git clone https://github.com/laurent-carrie-20201101/test_python_v2.git

    cd test_de_python_v2

    # create a virtual env for python
    virtualenv .venv --python=3.8

    # activate it
    . .venv/bin/activate

    # install requirements
    pip install -r requirements.txt

    # local install
    pip install -e .

    # run the tests
    pytest
