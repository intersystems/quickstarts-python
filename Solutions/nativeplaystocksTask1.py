"""
PURPOSE: Makes a connection to an instance of InterSystems IRIS Data Platform using the native API
"""

import irisnative


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


if __name__ == '__main__':
    run()
