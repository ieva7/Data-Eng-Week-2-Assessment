# SETUP

Please be advised that the program was built by and for Python v3.10 and later. Previous Python versions may return an error for some type-hints and other attributes when trying to run code.

It is recommended that you run this code in a virtual environment. To set one up, please run:
`python3 -m venv venv`.

To activate the environment, please run:
`source ./venv/bin/activate`

Before attempting to run the code, please make sure you run:
`pip3 install -r requirements.txt`


# test_1.py

This is the main file for test_1. Its methods and their tests are in methods_test_1.py and test_methods_test_1.py, respectively.

Test_1.py reads from 'tests/step1.log' file and runs functions to filter out invalid log lines. It also converts valid log lines to dictionary objects.

The file has pre-written tests for the user to track their progress on the two tasks.

Correct attemps will be marked by 'SUCCESS' statements printed to console.

Incorrect attempts to identify invalid log lines will be indicated via terminal and via 'step-1-failure-output.log' file that would be produced upon incorrect output.

*Please note, the code in file from line 22 has not been altered whatsoever per explicit instruction.*


# test_2.py

This is the main file for test_2. Its methods and their tests are in methods_test_2.py and test_methods_test_2.py, respectively.

Test_2.py reads input from 'people.csv' and allocates closest court of the desired type using the 'https://courttribunalfinder.service.gov.uk/' API.

The results are neatly projected to the console in a table format using Rich Console.

Any errors in the collection and outputting process will be printed to the terminal.


# test_3.py

This is the main file for test_3. Its test file is test_test_3.py, please refer to this file to satisfy test_3 testing requirements,

Test_3.py has one function that accepts a current time string in the HH:MM:SS format. There are constraints on what type of input is accepted, and any violations of said constraints are printed to the terminal.



## To run the main files, please adhere to this format:
`python3 [file]`, where file will be test_1.py, test_2.py, and/or test_3.py.



Please refer to the original instructions below.

# Data engineering Python tests

> For interviews in April 2022.

This test is to assess your ability to write Python code and to discuss how you think about coding problems during the interview. Don't worry if you don't complete the whole test - you can still pass the interview.

You should have been introduced to a person you can contact to clarify questions or solve technical issues. If anything is unclear or something is wrong, ask them as soon as possible. Asking questions will not affect how we score you on the test, so it is better to ask sooner rather than later.

You are free to use the internet to solve these tests and you can install additional packages. However, the solutions to this test can be achieved using Python and its standard libraries. Use whatever you're most comfortable with. This coding test was written and tested with python 3.8.

## Working with the code

If you can, clone this repo and work on your solutions on your own computer.

If you don't have a computer where you can do this, you can [complete the test on Google Colab](https://colab.research.google.com/drive/1jIYgeEKarkr6FHAnys6wVSoTIl24PjW6?usp=sharing) instead. Please create a copy of the notebook before you start.

During the interview we'll ask you to share your screen to show and discuss your solutions. You don't need to push your changes to Github or save them anywhere else.


## Doing the tests

There are 3 scripts in the root of this repo/directory:

- test_1.py
- test_2.py
- test_3.py

These scripts do not need to be completed in order, but we do recommend you do.

In each script is a comment block starting with `[TODO]`. This lays out what needs to be done to solve the test for that particular script. The remaining comments are there to explain the code and direct you.

### Test 1
This asks you to extract and structure data from the file `sample.log`. You'll need to complete 2 short functions.

When you think you have the answer, run `python test_1.py` and it will be automatically tested.

### Test 2
This asks you do get data from an API and match it with data from the file `people.csv`.

You're free to approach this however you like. We'll ask you to describe your approach and reasoning during the interview.

### Test 3
This asks you to fix a broken function and then write a unit test for it.
