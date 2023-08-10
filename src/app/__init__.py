def update(tabla, where, co_va):
    columns_values = ", ".join([f"{column}='{value}'" for column, value in co_va.items()])
    where = [f"{column}='{value}'" for column, value in where.items()]
    where = " AND ".join(where) if len(where) > 1 else "".join(where)
    query = f"UPDATE {tabla} SET {columns_values} WHERE {where};"
    print(query)

update("users", {"id": 1}, {"name": "juan", "age": 25})