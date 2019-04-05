# quickstarts-python
This code shows PyODBC, and the Native API access. It is required for the Python quickstart which can be found here: https://learning.intersystems.com/course/view.php?name=Python%20QS   
Note that our code and supporting wheel files are designed for Python 3 because Python 2 will retire in 2020. If you want to use Python 2, please contact us for more details.


## Contents
* `pyodbcplayTask7.py`: to see how to store and retrieve data relationally
* `nativeplayTask4.py`: to see how to run methods within InterSystems IRIS
## Configuration files
`connections.config`: contains connection details for PyODBC, and Native API.

## Connect to InterSystems via PyODBC

**Note**: If you have InterSystems IRIS installed locally in your machine, you do not need to set up InterSystems PyODBC driver.

**Prerequisite**: You should have [PyODBC](https://pypi.org/project/pyodbc/) already installed in your local machine.
If you having trouble installing PyODBC, please see [how to install PyODBC](pyodbc_install.md)

### Set up InterSystems PyODBC driver for Windows:

* Execute `ODBC-2018.1.1.635.0-win_x64.exe` file.

###  Set up InterSystems PyODBC driver for Mac OSX and Linux:

* Run `odbcinst –i –d –f odbcinst.ini`

## Connect to InterSystems via the Native API

### Set up the Native API for Windows:

* Run `pip install wheel/irisnative-1.0.0-cp36-cp36m-win_amd64.whl`

**Note:** Depending on the version of Python 3 and the version of Platform that you are using, you may have to change the filename to get the wheel file to be installed.

* If you are using Python 3.7, rename `irisnative-1.0.0-cp36-cp36m-win_amd64.whl` to `irisnative-1.0.0-cp37-cp37m-win_amd64.whl`

### Set up the Native API for Mac:

* Run `pip install wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl`

### Set up the Native API for Linux:

* Run `pip install wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl`

## How to run

1. Clone the repo and open it in your IDE.
2. In `connections.config` file, modify the host and password to be the correct values for your InterSystems IRIS instance. 
Although port and username are most likely the defaults, you should verify those values are corrects.
3. To run a file, in the terminal, type: `python filename.py`, in which, replace `filename.py` with the name of the file you want to run.