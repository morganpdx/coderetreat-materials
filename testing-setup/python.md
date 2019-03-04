
## How to start testing in Python

This guide assumes you're using VSCode.  We recommend it as a full-featured IDE for Coderetreats, and suggest you install it prior to the day of your Coderetreat.  You can download it here: https://code.visualstudio.com/download. It's free, awesome, and very easy to install and use.

This guide also assumes you have python installed.  To check if you have python installed, you can type `python -V`.

First, it's a good idea to create a project location to house all the work you're going to be doing today.  Here's an example of creating one called `coderetreat`:

- Open your VSCode window and click on the `x0 !0` icon in the bottom left corner of the window.  This will open a terminal window in VSCode; you can also select `View -> Terminal` or `Terminal -> New Terminal` from the menu.  VSCode will create a bash or powershell window, depending on whether you're using a Mac or Windows computer.
- (Optional) Browse to the location you'd like to create this folder
- Inside the terminal window, type the following:

```
mkdir coderetreat
cd coderetreat
``` 
- Now let's create our first python test file.  Create a new file inside the coderetreat folder called `test.py`.  The next set of changes will all happen inside this file, so open it up in your VSCode editor.
- We first need to import the python unittest library.  To do this, type 
```
import unittest
``` 
at the top of the file.

- Next, we need to create our test class which will house all of our unit tests:
```
class My_Test_Class(unittest.TestCase):
```
- Lastly, at the bottom of the file, we'll write the following code:
```
if __name__ == '__main__':
    unittest.main()
```
This tells the Python interpreter how to run this test file if it's being run directly.

- Now we're ready to start writing tests!  To make sure that all you've setup is working properly, let's add a simple test so we have something to run.  Be sure that this and all other test methods start with the word `test`:
```
    def test_string_compare(self):
        a = 'a string'
        b = 'some another string'
        self.assertEqual(a, b)
```
- Save your `test.py` file
- In the terminal window, check that you're still in the same directory as the file you just saved, and type 
```
python test.py
```
- If all went well, your test should have successfully run, but failed.  If the output in your terminal looks like this, you're on the right track!
```
F
======================================================================
FAIL: test_string_compare (__main__.TestStringMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test.py", line 8, in test_string_compare
    self.assertEqual(a,b)
AssertionError: 'a string' != 'another string'
- a string
+ another string
?  ++++++


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

- (Optional) See if you can make the test pass, and run it again.
