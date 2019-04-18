# quickstarts-python
This code shows PyODBC, and the Native API access. It is required for the Python quickstart which can be found here: https://learning.intersystems.com/course/view.php?name=Python%20QS   
Note that our code and supporting wheel files are designed for Python 3 because Python 2 will retire in 2020. If you want to use Python 2, please contact us for more details.


## Contents
* `pyodbcplayTask7.py`: to see how to store and retrieve data relationally
* `nativeplayTask5.py`: to see how to access directly the underlying structure within InterSystems IRIS

## Configuration files
`connections.config`: contains connection details for PyODBC, and Native API.

## How to run

1.  Verify you have an [<span class="urlformat">instance of InterSystems IRIS</span>](https://learning.intersystems.com/course/view.php?name=Get%20InterSystems%20IRIS), 
and an IDE that supports Python (such as **PyCharm**). 
If you are using AWS, Azure, or GCP, that you have followed the steps to [change the password for InterSystems IRIS](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=ACLOUD#ACLOUD_interact).
2.  If you are using AWS, GCP, or Microsoft Azure, load the sample stock data into InterSystems IRIS:  
    `$ iris load http://github.com/intersystems/Samples-Stock-Data`  
    
    If you are using InterSystems Labs, the sample stock data is already loaded. You can skip to the next step.
3. Clone the repo and open it in your IDE. Notes that all codes and supported materials are in **Solutions** folder
4. In `connections.config` file, modify the host and password to be the correct values for your InterSystems IRIS instance. 
Although port and username are most likely the defaults, you should verify those values are corrects.

## Connect to InterSystems via PyODBC

**Note**: If you have InterSystems IRIS installed locally in your machine, you do not need to set up InterSystems PyODBC driver.

**Prerequisite**: You should have [PyODBC](https://pypi.org/project/pyodbc/) already installed in your local machine.
If you having trouble installing PyODBC, please see [how to install PyODBC](pyodbc_install.md)

Before installing InterSystems driver, navigate to the **Solutions** directory of your terminal: `cd Solutions` 

### Set up InterSystems PyODBC driver for Windows:

* Run `pyodbc_wheel\pyodbc_whODBC-2018.1.1.635.0-win_x64.exe` file.

###  Set up InterSystems PyODBC driver for Mac OSX and Linux:

* Run `odbcinst –i –d –f pyodbc_wheel/odbcinst.ini`

## Connect to InterSystems via the Native API

Before installing, make sure you are in **Solutions** directory of your terminal.

### Set up the Native API for Windows:

* Run `pip install nativeAPI_wheel\irisnative-1.0.0-cp36-cp36m-win_amd64.whl`

### Set up the Native API for Mac:

* Run `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl`

### Set up the Native API for Linux:

* Run `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl`


## Having trouble installing InterSystems wheel for PyODBC and Native API?

* Our written code and supporting wheel files are designed for Python 3 because Python 2 will retire in 2020. If you want to use Python 2, please contact us for more details.
* Depending on the version of Mac OSX that you are using, you may have to change the filename to get the wheel file for the IRIS Native API to be installed. For example, if you are using Mac version 10.12, rename `irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl` to `irisnative-1.0.0-cp34-abi3-macosx_10_12_x86_64.macosx_10_14_x86_64.whl`
* Depending on the version of Python 3 that you are using, you may have to change the filename to get the wheel file for the IRIS Native API to be installed. For example: If you are using Python 3.7, rename `irisnative-1.0.0-cp36-cp36m-win_amd64.whl` to `irisnative-1.0.0-cp37-cp37m-win_amd64.whl`