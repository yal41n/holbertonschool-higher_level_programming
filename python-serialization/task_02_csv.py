#!/usr/bin/python3
"""
CSV to JSON Converter Module

Provides a function to convert CSV data into JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert the contents of a CSV file into a JSON file named data.json.

    Args:
        csv_filename (str): The input CSV filename.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        data_list = []

        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(dict(row))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True
    except (OSError, csv.Error, json.JSONDecodeError):
        return False
