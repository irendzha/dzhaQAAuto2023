import pytest
from modules.common.database import Database

import sqlite3


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()    
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

# Individual task 1
@pytest.mark.database
def test_check_all_products():
    db = Database()
    products = db.get_all_products()

    print(products)

# Individual task 2
@pytest.mark.database
def test_user_insert():
    db = Database()
    db.insert_user(3, 'Iryna', 'Tarasa Shevchenka str, 3', 'Zaporizhzhia', '69000', 'Ukraine')
    water_qnt = db.get_user_address_by_name('Iryna')

    assert water_qnt[0][0] == 'Tarasa Shevchenka str, 3'

# Individual task 3
@pytest.mark.database
def test_user_delete():
    db = Database()    
    db.insert_user(99, 'тестове імʼя', 'тестова вулиця', 'тестове місто', '9999', 'тестова країна')
    db.delete_user_by_id(99)
    adrs = db.get_user_address_by_name('тестова вулиця')

    assert len(adrs) == 0

# Individual task 4
@pytest.mark.database
def test_check_user_address():
    db = Database()
    user = db.get_user_address_by_id(3)

    assert user[0][0] == 'Tarasa Shevchenka str, 3'

# Individual task 5
@pytest.mark.database
def test_user_address_update():
    db = Database()
    db.update_user_address_by_id(3, 'Shevchenka blvd, 20')
    user_address = db.get_user_address_by_id(3)

    assert user_address[0][0] == 'Shevchenka blvd, 20'

# Individual task 6
@pytest.mark.database
def test_detailed_user():
    db = Database()
    users = db.get_detailed_user_by_id(3)
    print("Покупці", users)

    # Check structure of data
    assert users[0][0] == 3
    assert users[0][1] == 'Iryna'
    assert users[0][2] == 'Shevchenka blvd, 20'
    assert users[0][3] == 'Zaporizhzhia'
    assert users[0][4] == '69000'
    assert users[0][5] == 'Ukraine'

# Individual task 7
@pytest.mark.database
def test_update_user_id_to_string():
    try:
        db = Database()
        db.update_user_id_to_string(3, 'three')
    except sqlite3.IntegrityError as e: 
        e == 'datatype mismatch'
