## Table of Contents
* [1) Instalation](#installation)
* [2) Project Motivation](#motivation)
* [3) File Descriptions](#file)
* [4) Results](#results)
* [5) Licesing, Authors, Acknowledgements](#licesing)

## 1) Instalation <a class="anchor" id="installation"></a>

This project was developed in Python 3 using Jupyter Notebook 6.1.6 and Python libraries installed with Anaconda 4.8.3 for Windows.

Before you begin, make sure to run this command in your terminal to install pytest:
```
pip install -U pytest
```

Then, to run pytest, just enter:
```
pytest
```
Right now, not all of the tests should pass. Fix the function to pass all its tests! Once all your tests pass, try writing some additional unit tests of your own!

## 2) Project Motivation <a class="anchor" id="motivation"></a>

The main goal of this project is to document the exercises from the Data Science Nanodegree Udacity with focus on **Class 3 - Software Engineering Practices Pt II**. The main topics taught in this lesson are:
* Testing
* Logging
* Code review

This exercise consisting in using the **pytest** tool and the function **assert()** to create a **test_ file** in order to build some test case to verify the correctness of a function.

## 3) File Descriptions <a class="anchor" id="file"></a>

* **Python files files:**
    * **computer_launch.py:** It creates the function days_until_launch() that is responsible to calculate the days left before launch.
    * **test_computer_launch.py:** It has some test cases to verify if the fuction days_until_launch() created on computer_launch.py is working properly.

## 4) Results <a class="anchor" id="results"></a>

*  By installing the tool pytest and running it in the terminal, we can run test_ files that contains some test cases to verify if a piece of code is working properly;
* Using the compute_launch.py we can run the *#Original code without correction* section and observe that the pytest will return an error message for test_days_until_launch_0_negative() case;
* We can also comment the *#Original code without correction* section and uncomment the *#Corrected/fixed solution - uncomment to check the difference in pytest* section. This will fix the test_days_until_launch_0_negative().

## 5) Licesing, Authors, Acknowledgements <a class="anchor" id="licesing"></a>

This project is part of the Data Science Nanodegree from [Udacity](https://www.udacity.com/school-of-data-science).