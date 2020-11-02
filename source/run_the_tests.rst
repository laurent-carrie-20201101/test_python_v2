=============
run the tests
=============

the tests are written in python, using the pytest framework. According to the coding style of pytest, the tests
are located in the test directory, and it uses the datadir fixtures to find the csv file.

the tests read the csv files and write parquet, or read parquet files. Unit tests are independant, this is why the same
ingestion occurs in different tests.

the test are run by lauching pytest in the root directory. They may seem long, but this is because they run sparks,
so for a small dataset this is overkill, but we want to test the code.