from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()

    query = ("select products.product_id, products.name, products.um_id, products.price_per_unit, um.um_name FROM products inner join um on products.um_id=um.um_id")

    cursor.execute(query)

    response = []

    for (product_id, name, um_id, price_per_unit, um_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'um_id': um_id,
                'price_per_unit': price_per_unit,
                'um_name': um_name
            }
        )

   # print(product_id, name, um_id, price_per_unit, um_name)

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
            "(name, um_id, price_per_unit) "
            "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['um_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_new_product(connection, {
        'product_name': 'jackfruit',
        'um_id': '1',
        'price_per_unit': '1000'
    }))