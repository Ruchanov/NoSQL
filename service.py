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


def read_table(name, columns=None, filter_by=None, sort_by=None, sort_order="asc"):
    with open("database/" + name + ".json", "r") as f:
        data = json.load(f)
    rows = data["rows"]
    if filter_by is not None:
        rows = [row for row in rows if all(val in row.values() for val in filter_by.values())]
    if sort_by is not None:
        reverse = sort_order.lower() == "desc"
        rows = sorted(rows, key=lambda row: row.get(sort_by), reverse=reverse)
    if columns is None:
        return rows
    else:
        rows = [{col: row[col] for col in columns if col in row} for row in rows]
        return rows

