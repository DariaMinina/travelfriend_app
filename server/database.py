import psycopg2
from psycopg2 import OperationalError, ProgrammingError, InterfaceError
import json

class PostgreSQLHandler:
    def __init__(self, config: dict):
        self.config = config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                **self.config
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except OperationalError as err:
            if err.args[0] == 1045:
                print('Неверный логин и пароль, повторите подключение')
                return None
            if err.args[0] == 2003:
                print('Неверно введен порт или хост для подключения к серверу')
                return None
            if err.args[0] == 1049:
                print('Такой базы данных не существует')
                return None
        except UnicodeEncodeError as err:
            print('Были введены символы на русском языке')
            return None
        except InterfaceError as err:
            print(err)
            return err
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_value:
            if exc_value.args[0] == 'Курсор не был создан':
                print('Курсор не создан')
            elif exc_value.args[0] == 1064:
                print('Синтаксическая ошибка в запросе!')
                self.connection.commit()
                self.connection.close()
            elif exc_value.args[0] == 1146:
                print('Ошибка в запросе! Такой таблицы не существует.')
                self.connection.commit()
                self.connection.close()
            elif exc_value.args[0] == 1054:
                print('Ошибка в запросе! Такого поля не существует.')
                self.connection.commit()
                self.connection.close()
            exit(1)
        else:
            self.connection.commit()  # фиксация транзакции, изменение запроса
            self.cursor.close()
            self.connection.close()
            return True

    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_value:
            if exc_value.args[0] == 'Курсор не был создан':
                print('Курсор не создан')
            elif exc_value.args[0] == 1064:
                print('Синтаксическая ошибка в запросе!')
                self.connection.commit()
                self.connection.close()
            elif exc_value.args[0] == 1146:
                print('Ошибка в запросе! Такой таблицы не существует.')
                self.connection.commit()
                self.connection.close()
            elif exc_value.args[0] == 1054:
                print('Ошибка в запросе! Такого поля не существует.')
                self.connection.commit()
                self.connection.close()
            exit(1)
        else:
            self.connection.commit()  # фиксация транзакции, изменение запроса
            self.cursor.close()
            self.connection.close()
            return True
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                **self.config
            )
            print("Подключение к базе данных успешно установлено")
            return True
        except OperationalError as e:
            print(f"Ошибка подключения: {str(e)}")
            return False
        
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Подключение закрыто")
        
    def execute_query(self, query, params=None):
        if not self.connection:
            print("Не подключено к базе данных")
            return None
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                
                columns = [col[0] for col in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]

                return results
        except OperationalError as e:
            print(f"Ошибка выполнения запроса: {str(e)}")
            self.connection.rollback()
            return None
        except ProgrammingError as e:
            print(f"Ошибка синтаксиса SQL: {str(e)}")
            self.connection.rollback()
            return None
        
        return None

    def load_data(self, table_name, data):
        print('data.keys(): ....', data.keys(), 'data.values(): ....', data.values(),)
        query = f"""
        INSERT INTO {table_name} (id, {', '.join(data.keys())})
        VALUES (default, {','.join(['%s'] * len(data))})
        """
        
        try:
            with self.connection.cursor() as cursor:
                print(query)
                cursor.execute(query, tuple(data.values()))
                # for item in data.values():
                #     print(item)
                    #cursor.execute(query, str(item))
            
            self.connection.commit()
            print(f"Данные успешно загружены в таблицу {table_name}")
            return True
        except OperationalError as e:
            print(f"Ошибка при загрузке данных: {str(e)}")
            self.connection.rollback()
            return False
        
        return True
    
    
    def update_data(self, table_name, data, user_id):

        update_columns = []
        set_statements = []

        for column, value in data.items():
            update_columns.append(column)
            set_statements.append(f'{column} = ?')

        update_query = f"""
        UPDATE {table_name}
        SET {', '.join(set_statements)}
        WHERE id = {user_id}
        """

        try:
            with self.connection.cursor() as cursor:
                
                # Подставляем значения в запрос
                for _, (column, value) in enumerate(data.items()):
                    update_query = update_query.replace(column + ' = ?', f"{column} = '{value}'")
    
                cursor.execute(update_query)
            
            self.connection.commit()
            print(f"Данные успешно загружены в таблицу {table_name}")
            return True
        except OperationalError as e:
            print(f"Ошибка при загрузке данных: {str(e)}")
            self.connection.rollback()
            return False
        
        return True
    

    def delete_user(self, table_name, user_id):
        
        query = f"""
        DELETE FROM {table_name}
        WHERE id = {user_id}
        """
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
            self.connection.commit()
            print(f"Пользователь успешно удален из таблицы {table_name}")
            return True
        except OperationalError as e:
            print(f"Ошибка при загрузке данных: {str(e)}")
            self.connection.rollback()
            return False
        
        return True