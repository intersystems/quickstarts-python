# quickstarts-python
This code shows how to connect a Python application with an InterSystems server using the Native API. It is used in the online exercise [<span class="urlformat">Python quickstart</span>](https://learning.intersystems.com/course/view.php?name=Python%20QS).
Note that our code and supporting wheel files are designed for Python 3. If you want to use Python 2, please contact [<span class="urlformat">online.training@intersystems.com</span>](online.training@intersystems.com) for more details.

## Supported platforms

| Operating System | Version |
| -- | :-----: |  
| Windows | Windows 10, Windows Server 2012, 2016, 2019 |
| Mac | Apple macOS 10.13, 10.14 |
| Linux | <ul><li>Oracle Linux 7</li><li>Red Hat Enterprise Linux 7</li><li>SUSE Linux Enterprise Server 12</li><li>Ubuntu 18.04</li><li>CentOS-7</li></ul> |


## Contents
### Python files 
* `nativeplaystocksTask1.py`: to make a connection to an instance of InterSystems IRIS Data Platform using the Native API
* `nativeplaystocksTask6.py`: to see how to access directly the underlying structure within InterSystems IRIS

### Configuration files
* `connection.config`: contains connection details for Native API, including `ip`, `port`, `namespace`, `username`, and `password`.

## How to run

1.  Verify you have an instance of InterSystems IRIS, and an IDE that supports Python (such as **VS Code**). To download Community Edition locally, get an InterSystems IRIS installation kit from the [<span class="urlformat">evaluation kit download page</span>](https://evaluation.intersystems.com/Eval/). To use InterSystems IRIS in a container, get an image from the [<span class="urlformat">InterSystems Container Registry</span>](https://containers.intersystems.com/contents). 
2.  If you are using a local or container instance, load the sample stock data into InterSystems IRIS:  
    `$ iris load http://github.com/intersystems/Samples-Stock-Data`  
    
    If you are using InterSystems Labs, the sample stock data is already loaded. You can skip to the next step.
3. Clone the repo and open it in your IDE. Notes that all code and supported materials are in **Solutions** folder
4. In `connection.config` file, modify the host and password to be the correct values for your InterSystems IRIS instance. 
Although port and username are most likely the defaults, you should verify those values are correct. The port value should be the superserver port. 

## Connect to InterSystems via the Native API

To connect using the Native API, you will need the DB-API driver. If InterSystems IRIS is installed locally or in a container on your development system, you can find the file in `install-dir\dev\python`, where `install-dir` is the InterSystems IRIS installation directory (`install-dir` in a container is `/usr/irissys`). You can also download the driver from the InterSystems IRIS [<span class="urlformat">driver distribution page</span>](https://intersystems-community.github.io/iris-driver-distribution/). Put this driver in the **Solutions** directory. 

Before installing the driver, make sure you are in **Solutions** directory of your terminal: `cd Solutions` 

Install the driver using `pip`:

`pip install intersystems_irispython-3.2.0-py3-none-any.whl` 

## Run sample Python code to connect with InterSystems IRIS database

1. Run `python nativeplaystocksTask1.py` to make a connection to an instance of InterSystems IRIS Data Platform using the Native API.
2. Run `python nativeplaystocksTask6.py` to store and view data using globals, the underlying structure within InterSystems IRIS.

