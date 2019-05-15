"""
PURPOSE: Store stock data directly to InterSystems IRIS Data Platform using a custom structure.

NOTES: When running, choose option 2 to store stock data natively.
"""

from time import time
import irisnative


# Write to a test global
def set_test_global(iris_native):
    iris_native.set(8888, "^testglobal", "1")
    global_value = iris_native.get("^testglobal", "1")
    print("The value of ^testglobal(1) is {}".format(global_value))


# Store stock data directly into InterSystems IRIS
def store_stock_data(iris_native):
    # Clear global from previous runs
    iris_native.kill("^nyse")
    print("Storing stock data using Native API...")

    # Get stock data from file
    list_stock = []
    with open("all_stocks.csv") as f:
        lines = f.readlines()

        # Add stock data to list
        for line in lines:
            list_stock.append(line.rstrip("\n"))

    # Get current time
    start = int(time() * 1000)

    # Loop through list of stock and write global
    for i in range(1, len(list_stock)):
        iris_native.set(list_stock[i], "^nyse", i)

    # Get time consuming
    end = int(time() * 1000)
    time_consume = end - start
    print("Stored natively successfully. Execution time: {} ms".format(time_consume))


# Execute task based on user input
def execute_selection(selection, iris_native):
    if selection == 1:
        set_test_global(iris_native)
    elif selection == 2:
        store_stock_data(iris_native)
    elif selection == 3:
        print("TO DO: View stock data")
    elif selection == 4:
        print("TO DO: Generate trades")
    elif selection == 5:
        print("TO DO: Call Routines")


# Get connection details from config file
def get_connection_info(file_name):
    # Initial empty dictionary to store connection details
    connections = {}

    # Open config file to get connection info
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            # remove all white space (space, tab, new line)
            line = ''.join(line.split())

            # get connection info
            connection_param, connection_value = line.split(":")
            connections[connection_param] = connection_value
    return connections


def run():
    # Retrieve connection information from configuration file
    connection_detail = get_connection_info("connection.config")

    ip = connection_detail["ip"]
    port = int(connection_detail["port"])
    namespace = connection_detail["namespace"]
    username = connection_detail["username"]
    password = connection_detail["password"]

    # Create connection to InterSystems IRIS
    connection = irisnative.createConnection(ip, port, namespace, username, password)
    print("Connected to InterSystems IRIS")

    # Create an iris object
    iris_native = irisnative.createIris(connection)

    # Starting interactive prompt
    while True:
        print("1. Test")
        print("2. Store stock data")
        print("3. View stock data")
        print("4. Generate Trades")
        print("5. Call routines")
        print("6. Quit")
        selection = int(input("What would you like to do? "))
        if selection == 6:
            break
        elif selection not in range(1, 7):
            print("Invalid option. Try again!")
            continue
        execute_selection(selection, iris_native)


if __name__ == '__main__':
    run()
