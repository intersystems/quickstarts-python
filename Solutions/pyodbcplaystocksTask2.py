"""
PURPOSE: View top 10 stocks.

NOTES: When running the application, choose option 1 and try 2016-08-12.
"""

from datetime import datetime
import pyodbc


# Find top 10 stocks on a particular date
def find_top_on_date(connection, date):
    cursor = connection.cursor()
    sql = "SELECT distinct top 10 transdate,name,stockclose,stockopen,high,low,volume FROM Demo.Stock " \
          "WHERE transdate = ? ORDER BY stockclose desc"
    print("Date\t\tName\tOpening Price\tDaily High\tDaily Low\tClosing Price\tVolume")

    rows = cursor.execute(sql, datetime.strptime(date, "%Y-%m-%d"))
    for row in rows:
        for item in row:
            print("{}\t".format(item), end='')
        print("")


# Task 2: View top 10 stocks for selected date
# Note: Choose 2016/08/12 for date
def task_view_top10_stock(connection):
    date = input("On which date? (YYYY-MM-DD) ")
    find_top_on_date(connection, date)


# Execute task based on user input
def execute_selection(selection, connection):
    if selection == 1:
        task_view_top10_stock(connection)
    elif selection == 2:
        print("TO DO: Create Portfolio")
    elif selection == 3:
        print("TO DO: Add to Portfolio")
    elif selection == 4:
        print("TO DO: Update Portfolio")
    elif selection == 5:
        print("TO DO: Delete from Portfolio")
    elif selection == 6:
        print("TO DO: View Portfolio")


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
    driver = "{InterSystems ODBC}"

    # Create connection to InterSystems IRIS
    connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}'\
        .format(driver, ip, port, namespace, username, password)
    connection = pyodbc.connect(connection_string)
    print("Connected to InterSystems IRIS")

    # Starting interactive prompt
    while True:
        print("1. View top 10")
        print("2. Create Portfolio table")
        print("3. Add to Portfolio")
        print("4. Update Portfolio")
        print("5. Delete from Portfolio")
        print("6. View Portfolio")
        print("7. Quit")
        selection = int(input("What would you like to do? "))
        if selection == 7:
            break
        elif selection not in range(1, 8):
            print("Invalid option. Try again!")
            continue
        execute_selection(selection, connection)


if __name__ == '__main__':
    run()
