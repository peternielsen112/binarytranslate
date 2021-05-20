# Binary Translator
[![Github All Releases](https://img.shields.io/github/downloads/peternielsen112/binarytranslate/total.svg)](https://github.com/peternielsen112/binarytranslate/releases)
[![GitHub release](https://img.shields.io/github/release/peternielsen112/binarytranslate/all.svg)](https://github.com/peternielsen112/binarytranslate/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date-pre/peternielsen112/binarytranslate.svg)](https://github.com/peternielsen112/binarytranslate/releases)
[![GitHub license](https://img.shields.io/badge/License-GNU%20GPL%203.0-blue)](https://github.com/peternielsen112/binarytranslate/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/peternielsen112/binarytranslate.svg)](https://github.com/peternielsen112/binarytranslate/stargazers)

---
### Contents

- [Requirements](#requirements)

- [About](#about)

- [Instructions](#instructions)

    - [Git Bash](#git-bash)

    - [Terminal.app](#terminal.app)
    
    - [File-Browsing GUIs](#file-browsing-guis)

- [How it Works](#how-it-works)

- [About the Creator](#about-the-creator)

---
### Requirements

* Python 3.7 or above
* No modules are required.

---
### About
[Binary Translator](https://github.com/peternielsen112/binarytranslate) ia a simple Python repository that translates numbers into binary. This program is copyright (C) 2021 Peter Nielsen. See LICENSE.md for more details.


---
### Instructions

##### Git Bash:

1. Navigate to the folder in Git Bash. `cd C:/example/path/to/binarytranslate`.

2. Run the main file using the command: `python main.py`. **Python must be installed on your system** for this operation to complete.

3. When prompted, enter an integer up to `65535`.

4. Output in binary is given.

##### Terminal.app:

1. Navigate to the folder in Terminal: `cd ~/example/path/to/binarytranslate`
2. Run the main file using this command: `python3 main.py`. **Python must be installed on your system** for this operation to complete.
3. When prompted, enter an integer up to `65535`.
4. Output in binary is given.

##### File Browsing GUIs:

1. Navigate to the folder in Windows Explorer or Finder (MacOS).

2. Double-click on the file and it will open a Python shell. **Python must be installed on your system** for this operation to complete.

3. When prompted, enter an integer up to `65535`.

4. Output in binary is given.

---
### How it Works:
The program takes input from the user using Python's out-of-the-box [input()](https://docs.python.org/3/library/functions.html#input) function. This input is saved as a variable, `user_input`. Then, for every binary place in a large range, that amount is subtracted if the number is great enough to meet a binary value. During each calculation, the program determines whether to set that place's digit to `1` or `0`. The digits are combined and then printed to the console using an [f string](https://docs.python.org/3/tutorial/inputoutput.html). If an option that is higher than `65535` is given, it returns an error message; another error will be returned if the input is not an integer (using a [try/except statement](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)).

---
### About the Creator
I create programs in a variety of languages, from Python to JavaScript to CSS and more. I'm on GitHub: [@peternielsen112](https://github.com/peternielsen112) and also [Replit.com](https://replit.com/@peternielsen112) by the same username.
Please email any problems or suggestions to me at <dirigo112@gmail.com>.
