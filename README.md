# binarytranslate

A simple Python repository that translates simple characters into binary. Program copyright (C) Peter Nielsen 2020.
I'm on GitHub: @peternielsen112 and also Repl.it by the same username.
Please email any problems or suggestions to me at <dirigo112@gmail.com>.



### Contents

- [Instructions](#instructions)

    - [Terminal](#terminal)
    
    - [Explorer and other GUIs](#windows-explorer-and-other-guis)

- [How it Works](#how-it-works)



### Instructions

##### Terminal:


**Note: this is for Windows.**

1. Navigate to the folder in Git Bash. `$ cd C:/example/path/binarytranslate`.

2. Run the main file by using the command: `$ python main.py`.

3. When prompted, enter a digit up to the specified number (currently, this is `2047`).

4. Watch your digit be printed out in binary!


##### Windows Explorer and other GUIs:

1. Navigate to the folder in Windows Explorer or Finder (MacOS).

2. Double-click on the file and it will open a Python shell. ***PYTHON MUST BE INSTALLED.***

3. You'll be prompted for a number up to `2047`. Enter one.

4. Output in binary is given.


### How it Works:


The program takes input from the user using Python's out-of-the-box `input()` function. This input is saved as a variable, `user_input`. Then, for every binary place from 1024 to 1, that amount is subtracted if the number is that big. During each calculation, the program determines whether to set that place's digit to `1` or `0`. The digits are combined and then printed to the console.
