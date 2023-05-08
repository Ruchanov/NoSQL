import json
import os

def create_table(name, columns):
    data = {"columns": columns, "rows": []}
    with open("database/" + name + ".json", "w") as f:
        json.dump(data, f)


def delete_table(name):
    os.remove("database/" + name + ".json")


def add_row(name, row):
    with open("database/" + name + ".json", "r") as f:
        data = json.load(f)
    data["rows"].append(row)
    with open("database/" + name + ".json", "w") as f:
        json.dump(data, f)


def delete_row(name, id):
    with open("database/" + name + ".json", "r") as f:
        data = json.load(f)
    new_rows = []
    for row in data["rows"]:
        if row.get("id") != id:
            new_rows.append(row)
    data["rows"] = new_rows
    with open("database/" + name + ".json", "w") as f:
        json.dump(data, f)


def update_row(name, id, new_data):
    with open("database/" + name + ".json", "r") as f:
        data = json.load(f)
    for row in data["rows"]:
        if row.get("id") == id:
            row.update(new_data)
    with open("database/" + name + ".json", "w") as f:
        json.dump(data, f)


def read_table(name, columns=None):
    with open("database/" + name + ".json", "r") as f:
        data = json.load(f)
    if columns is None:
        return data["rows"]
    else:
        rows = []
        for row in data["rows"]:
            new_row = {}
            for column in columns:
                if column in row:
                    new_row[column] = row[column]
            rows.append(new_row)
        return rows
