# Sample Visual Studio Code Configuration for Python Development

This repository contains sample configuration files that can be used to set up Visual Studio Code for Python development. The configuration files include extension recommendations, settings to configure the IDE to use a virtual environment within the IDE and to use PyTest to execute tests from within the editor, and settings and debug configuration to allow for use of the [experimental debugger](https://github.com/Microsoft/vscode-python/issues/538).

The repository also contains a sample Python application that can be used to test the IDE's capabilities. *While the sample configuration files are applicable for development in Python 2, the code was written targeting Python 3.*

## Setting Up the Environment

To try out the code in this repo, follow these steps:

1. Ensure Python and Git are installed in your environment.

2. Download and install Visual Studio Code 

   Visual Studio Code can be [downloaded and installed from the internet](https://code.visualstudio.com/download) or you can install it using a package manager supported on your operating system.

3. Clone this repository and open the repository directory

   ```
   $ git clone https://github.com/phillipdwright/vscode-python-sample-configuration.git
   $ cd vscode-python-sample-configuration
   ```

4. Set up and activate a virtual environment and install requirements

   ```
   $ python3 -m venv .venv
   $ source venv/bin/activate
   $ pip install -r dev-requirements.txt
   ```

5. Open the local project repo in Visual Studio Code

   Within Visual Studio Code, select the *Open Folder* option, and navigate to the folder containing the files in this repository.

6. Install recommended extensions

   Once the folder is open in Visual Studio Code, you will see a notification prompting you to install recommended extensions. Choose the *Install All* option. Once the extensions are installed, Visual Studio Code will prompt you to reload the application.

## Using the IDE for Testing and Debugging

All unit tests in the project can be run by choosing the "Run Tests" option from the Status Bar test runner. Alternatively, with a unit test file open, run an individual unit test or all tests in a unit test class by choosing the "Run Test" annotation above the method or class definition.

To debug a unit test, add any desired breakpoints to the test by clicking to the left of the line number on which the breakpoint is needed, and choose the "Debug Test" annotation above the method definition. To debug code in a script or module, with the script or module open, choose "Debug > Start Debugging" from the menu, or press the F5 key.

While debugging, values assigned to variables can be viewed by hovering over the variable names in an executing test, script, or module, or they can be viewed from the Debug view in the `VARIABLES` section. Notice that variables with attributes can be expanded and collapsed to view the values assigned to those attributes.
