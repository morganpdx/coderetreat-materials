
## How to start testing in Javascript

This guide also assumes you have node installed.  To check if you have node installed, you can type `node -v`.

First, it's a good idea to create a project location to house all the work you're going to be doing today.  Here's an example of creating one called `coderetreat`:

- Open your VSCode window and click on the `x0 !0` icon in the bottom left corner of the window, in the blue status tray.  This will open a terminal window in VSCode; you can also select `View -> Terminal` or `Terminal -> New Terminal` from the menu.  VSCode will create a bash or powershell window, depending on whether you're using a Mac or Windows computer.
- (Optional) Browse to the location you'd like to create this directory
- Inside the terminal window, type the following:

```
mkdir coderetreat
cd coderetreat
``` 

- Next we need to initialize our directory with a package.json and install our test framework; for this example we'll be using (mocha)[http://mochajs.org/].  From inside the directory you just created, initialize a new npm project

```
npm init
```

You can select the defaults for most of the questions, or update them as you prefer; however for the `test command` question, type `mocha`, as that's what we're going to be using.  Once your package.json file is generated, install mocha for this project:

```
npm install --save-dev mocha
```

The next step is to create a test file.  Inside your project directory, create a file called `test.js`.  We're going to create a very simple assert in here, just to be sure everything is working.  This could be considered your first configuration test, if you're going to go on and build a larger TDD effort upon this walkthrough.  Inside your `test.js` file, enter the following code:

```
const assert = require('assert)

it('should return true', () => {
    assert.equal(true, false)
})

```

In your terminal, type `npm test`.  If everything is working, your test should run successfully but the assert should fail.  Update the code to assert that `assert.equal(true, true)` and run your test again.  Is it now green?  Then your testing is set up correctly, and your first configuration test is complete!  You can then go on to start writing more tests, such as testing a function returns 'Hello World'.  We've included samples of this in this folder.