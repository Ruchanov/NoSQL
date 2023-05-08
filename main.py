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

# Функция обновления строки в таблице по id
def update_row(name, id, new_data):
    with open("database/" + name + ".json", "r") as f:
        data = json.load(f)
    for row in data["rows"]:
        if row.get("id") == id:
            row.update(new_data)
    with open("database/" + name + ".json", "w") as f:
        json.dump(data, f)

# Пример использования
create_table("users", ["id", "name", "age", "email"])
add_row("users", {"id": 1, "name": "John", "age": 30, "email": "john@example.com"})
add_row("users", {"id": 2, "name": "Jane", "age": 25, "email": "jane@example.com"})
delete_row("users", 1)
update_row("users", 2, {"age": 26})
