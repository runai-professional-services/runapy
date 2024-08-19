import os
import json


def load_test_data(filename):
    filepath = os.path.join(os.path.dirname(__file__), "test_data", filename)
    with open(filepath, "r") as file:
        return json.load(file)
