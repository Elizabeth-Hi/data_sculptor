from influxdb import InfluxDBClient
from typing import List, Dict, Union


class InfluxDBManager:
    def __init__(self, host: str, port: int, username: str, password: str, database: str):
        """
        Initialize the InfluxDBManager.

        Args:
            host (str): The hostname of the InfluxDB server.
            port (int): The port number of the InfluxDB server.
            username (str): The username for authentication.
            password (str): The password for authentication.
            database (str): The name of the database to connect to.
        """
        self.client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)

    def create_database(self, database: str):
        """
        Create a new database.

        Args:
            database (str): The name of the database to create.
        """
        self.client.create_database(database)

    def write_data(self, measurement: str, tags: Dict[str, str], fields: Dict[str, Union[str, float, int]], time: str = None):
        """
        Write a data point to the database.

        Args:
            measurement (str): The name of the measurement to write to.
            tags (Dict[str, str]): A dictionary of tag keys and values.
            fields (Dict[str, Union[str, float, int]]): A dictionary of field keys and values.
            time (str, optional): The timestamp for the data point. If not provided, the server's local time is used.
        """
        json_body = [
            {
                "measurement": measurement,
                "tags": tags,
                "fields": fields
            }
        ]
        if time:
            json_body[0]["time"] = time
        self.client.write_points(json_body)

    def query_data(self, query: str) -> List[Dict]:
        """
        Execute a query and return the results.

        Args:
            query (str): The InfluxDB query string to execute.

        Returns:
            List[Dict]: A list of dictionaries, where each dictionary represents a data point.
        """
        result = self.client.query(query)
        return list(result.get_points())

    def get_measurements(self) -> List[str]:
        """
        Get a list of all measurements in the database.

        Returns:
            List[str]: A list of measurement names.
        """
        result = self.client.get_list_measurements()
        return [item['name'] for item in result]

    def get_field_keys(self, measurement: str) -> List[Dict[str, str]]:
        """
        Get the field keys for a specific measurement.

        Args:
            measurement (str): The name of the measurement.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing field key information.
        """
        query = f'SHOW FIELD KEYS FROM "{measurement}"'
        return self.query_data(query)

    def get_tag_keys(self, measurement: str) -> List[Dict[str, str]]:
        """
        Get the tag keys for a specific measurement.

        Args:
            measurement (str): The name of the measurement.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing tag key information.
        """
        query = f'SHOW TAG KEYS FROM "{measurement}"'
        return self.query_data(query)

    def close(self):
        """Close the database connection."""
        self.client.close()


