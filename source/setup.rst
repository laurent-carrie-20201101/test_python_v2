=====
setup
=====


.. code-block:: bash
    :linenos:

    # il faut d'abord cloner le repository pour avoir les sources en local
    git clone https://github.com/laurent-carrie-20201101/test_python_v2.git
    cd test_python_v2

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
