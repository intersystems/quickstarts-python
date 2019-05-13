# quickstarts-python
This code shows PyODBC, and the Native API access. It is required for the Python quickstart which can be found here: 
[https://learning.intersystems.com/course/view.php?name=Python%20QS](https://learning.intersystems.com/course/view.php?name=Python%20QS)   
Note that our code and supporting wheel files are designed for Python 3 because Python 2 will retire in 2020. If you want to use Python 2, please contact us for more details.

## Supported platforms

| Operating System | Version |
| -- | :-----: |  
| Windows | Windows 10, Windows Server 2012, 2016, 2019 |
| Mac | Apple macOS 10.13, 10.14 |
| Linux | <ul><li>Oracle Linux 7</li><li>Red Hat Enterprise Linux 7</li><li>SUSE Linux Enterprise Server 12</li><li>Ubuntu 18.04</li><li>CentOS-7</li></ul> |


## Contents
* `pyodbcplaystocksTask7.py`: to see how to store and retrieve data relationally
* `nativeplaystocksTask6.py`: to see how to access directly the underlying structure within InterSystems IRIS

## Configuration files
`connection.config`: contains connection details for PyODBC and Native API.

## Installation wheels
* `nativeAPI_wheel`: contains installation wheel for using Python with Native API.
*  `pyodbc_wheel`: contains installation wheel for using Python with PyODBC.

## How to run

1.  Verify you have an [<span class="urlformat">instance of InterSystems IRIS</span>](https://learning.intersystems.com/course/view.php?name=Get%20InterSystems%20IRIS), 
and an IDE that supports Python (such as **PyCharm**). 
If you are using AWS, Azure, or GCP, that you have followed the steps to [change the password for InterSystems IRIS](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=ACLOUD#ACLOUD_interact).
2.  If you are using AWS, GCP, or Microsoft Azure, load the sample stock data into InterSystems IRIS:  
    `$ iris load http://github.com/intersystems/Samples-Stock-Data`  
    
    If you are using InterSystems Labs, the sample stock data is already loaded. You can skip to the next step.
3. Clone the repo and open it in your IDE. Notes that all codes and supported materials are in **Solutions** folder
4. In `connection.config` file, modify the host and password to be the correct values for your InterSystems IRIS instance. 
Although port and username are most likely the defaults, you should verify those values are corrects.

## Connect to InterSystems via PyODBC

**Note**: If you have InterSystems IRIS installed locally in your machine, you do not need to set up InterSystems PyODBC driver.

**Prerequisite**: You should have [PyODBC](https://pypi.org/project/pyodbc/) already installed in your local machine.
If you having trouble installing PyODBC, please see [how to install PyODBC](pyodbc_install.md)

Before installing InterSystems driver, navigate to the **Solutions** directory of your terminal: `cd Solutions` 
    
| Operating System | Command |
| -- | :--: |  
| Local instance | InterSystems IRIS PyODBC driver is installed. You can skip this step. |
| Windows | `pyodbc_wheel\ODBC-2018.1.1.635.0-win_x64.exe` |
| Mac, Linux | `odbcinst –i –d –f pyodbc_wheel/odbcinst.ini` |    

## Connect to InterSystems via the Native API

Before installing, make sure you are in **Solutions** directory of your terminal.

| Operating System | Command |
| -- | :--: |  
| Window | `pip install nativeAPI_wheel\irisnative-1.0.0-cp34.cp35.cp36.cp37-none-win_amd64.whl` |
| Mac | `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl`  |
| Linux | `pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl` |

## Run sample Python code to connect with InterSystems IRIS database

1. Run `python pyodbcplaystocksTask1.py` to make a connection to an instance of InterSystems IRIS Data Platform using the PyODBC.
2. Run `python nativeplaystocksTask1.py` to make a connection to an instance of InterSystems IRIS Data Platform using the Native API.