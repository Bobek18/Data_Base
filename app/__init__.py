import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os
import sys

print(sys.path)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)
    create_database()  # Викликаємо функцію створення бази даних
    create_tables(app)  # Створюємо таблиці
    populate_data()  # Населяємо базу даних
    return app

def create_database():
    # Підключення до MySQL без вказівки бази даних
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='123123123'
    )
    cursor = connection.cursor()
    # Створення бази даних, якщо вона ще не існує
    cursor.execute("CREATE DATABASE IF NOT EXISTS smartwatchesdb")
    cursor.close()
    connection.close()

def create_tables(app):
    with app.app_context():
        # Створюємо всі таблиці, визначені в SQLAlchemy моделях
        db.create_all()

def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists('data.sql'):
        # Підключення до вже створеної бази даних
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='123123123',
            database='smartwatchesdb'  # Використовуємо правильну назву бази даних
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()
        cursor.close()
        connection.close()
