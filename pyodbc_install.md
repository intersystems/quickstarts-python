## Install pyodbc for Windows

1. Run `pip install pyodbc`

## Install pyodbc for Mac OSX

1. Run `brew update`
2. Run `brew install unixodbc`
3. Run `pip install pip==7.1.2`
4. Run `pip install --upgrade --global-option=build_ext --global-option="-I/usr/local/include" --global-option="-L/usr/local/lib" --allow-external pyodbc --allow-unverified pyodbc pyodbc`


## Install pyodbc for Linux

1. Run `apt-get update`
2. Run `apt-get install python3-pip`
2. Run `apt-cache search iodbc`
3. Run `apt-get install -y unixodbc-dev iodbc`
4. Run `pip install --upgrade --global-option=build_ext --global-option="-I/usr/local/include" --global-option="-L/usr/local/lib" pyodbc`
