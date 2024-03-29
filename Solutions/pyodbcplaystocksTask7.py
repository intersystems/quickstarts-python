"""
PURPOSE: Simulate adding stocks to your stock portfolio and see how you would have done.

NOTES: When running the application,
1. Choose option 1 to view top 10 stocks.
2. Choose option 3 to add 2 or 3 stocks to your portfolio (using names from top 10 and 2016-08-12).
3. Choose option 6 using date 2017-08-10 to view your % Gain or Loss after a year.
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


# Create portfolio table
def create_portfolio_table(connection):
    cursor = connection.cursor()
    create_table = "CREATE TABLE Demo.Portfolio(Name varchar(50) unique, PurchaseDate date, " \
                   "PurchasePrice numeric(10,4), Shares int, DateTimeUpdated datetime)"
    try:
        cursor.execute(create_table)
        print("Created Demo.Portfolio table successfully.")
        connection.commit()
    except Exception as e:
        print("Error creating portfolio: " + str(e))


# Add item to portfolio
def add_portfolio_item(connection, name, purchase_date, price, shares):
    try:
        sql = "INSERT INTO Demo.Portfolio (name,PurchaseDate,PurchasePrice,Shares,DateTimeUpdated) VALUES (?,?,?,?,?)"
        cursor = connection.cursor()
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        current_time = datetime.now()
        cursor.execute(sql, name, purchase_date, float(price), float(shares), current_time)
        print("Added new line item for stock: {}.".format(name))
        connection.commit()
    except Exception as e:
        print("Error adding to portfolio: " + str(e))


# Update item in portfolio
def update_portfolio_item(connection, name, purchase_date, price, shares):
    sql = "UPDATE Demo.Portfolio SET purchaseDate = ?, purchasePrice= ?, shares = ?, DateTimeUpdated= ? WHERE name= ?"
    cursor = connection.cursor()
    purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
    current_time = datetime.now()
    cursor.execute(sql, purchase_date, float(price), float(shares), current_time, name)
    if cursor.rowcount > 0:
        print("Updated {} successfully.".format(name))
    else:
        print("{} does not exist.".format(name))
    connection.commit()


# Delete item from portfolio
def delete_portfolio_table(connection, name):
    sql = "DELETE FROM Demo.Portfolio WHERE name = ?"
    cursor = connection.cursor()
    cursor.execute(sql, name)
    if cursor.rowcount > 0:
        print("Deleted {} successfully.".format(name))
    else:
        print("{} does not exist.".format(name))
    connection.commit()


# View your portfolio to know % Gain or Loss
def view_portfolio_table(connection, trans_date):
    sql = "SELECT pf.name, pf.purchaseprice, pf.purchaseDate, st.stockclose, pf.shares, pf.DateTimeUpdated " \
          "FROM Demo.Portfolio as pf JOIN Demo.Stock as st on st.name = pf.name WHERE st.Transdate = ?"
    cursor = connection.cursor()
    rows = cursor.execute(sql, datetime.strptime(trans_date, "%Y-%m-%d"))
    print("Name\tPurchase Date\tPurchase Price\tStock Close\tShares\tDatetime Updated\t\t% Change\tGain or Loss")
    for row in rows:
        name = row[0]
        purchase_price = row[1]
        purchase_date = row[2]
        stock_close = row[3]
        shares = row[4]
        current_time = row[5]
        percent_change = (stock_close - purchase_price) / purchase_price * 100
        start_value = purchase_price * shares
        end_value = stock_close * shares
        gain_or_loss = round(end_value - start_value, 2)
        print("{}\t{}\t{}\t\t{}\t{}\t{}\t{}\t{}"
              .format(name, purchase_date, purchase_price, stock_close,
                      shares, current_time, percent_change, gain_or_loss))


# Task 2: View top 10 stocks for selected date
# Note: Choose 2016/08/12 for date
def task_view_top10_stock(connection):
    date = input("On which date? (YYYY-MM-DD) ")
    find_top_on_date(connection, date)


# Task 3: Create Portfolio Table
def task_create_portfolio(connection):
    print("Create portfolio")
    create_portfolio_table(connection)


# Task 4: Add item to Portfolio table
# Note: Choose stock name using list of stocks generated by Task 2
def task_add_to_portfolio(connection):
    print("Add to portfolio")
    name = input("Name: ")
    date = input("Date (YYYY-MM-DD): ")
    price = input("Price: ")
    shares = input("Number of shares: ")
    add_portfolio_item(connection, name, date, price, shares)


# Task 5: Update item in Portfolio table
def task_update_portfolio(connection):
    print("Update portfolio")
    name = input("Which stock you are going to update: ")
    date = input("New Date (YYYY-MM-DD): ")
    price = input("New Price: ")
    shares = input("New Number of shares: ")
    update_portfolio_item(connection, name, date, price, shares)


# Task 6: Delete item from Portfolio table
def task_delete_portfolio(connection):
    print("Delete from portfolio")
    name = input("Which stock you want to delete? ")
    delete_portfolio_table(connection, name)


# Task 7: View your Portfolio to see how much you gain/loss
# Note: Choose option 3 to add 2 or 3 stocks to your portfolio (using names from top 10 and 2016-08-12 as date);
# then choose option 6 using date 2017-08-10 to view your % Gain or Loss after a year.
def task_view_porfolio(connection):
    print("View portfolio")
    trans_date = input("Selling on which date? (YYYY-MM-DD) ")
    view_portfolio_table(connection, trans_date)


# Execute task based on user input
def execute_selection(selection, connection):
    if selection == 1:
        task_view_top10_stock(connection)
    elif selection == 2:
        task_create_portfolio(connection)
    elif selection == 3:
        task_add_to_portfolio(connection)
    elif selection == 4:
        task_update_portfolio(connection)
    elif selection == 5:
        task_delete_portfolio(connection)
    elif selection == 6:
        task_view_porfolio(connection)


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
    driver = "{InterSystems IRIS ODBC35}"

    # Create connection to InterSystems IRIS
    connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}' \
        .format(driver, ip, port, namespace, username, password)
    connection = pyodbc.connect(connection_string)
    connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    connection.setencoding(encoding='utf-8')
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
