# Разработка RESTfull приложения для поиска друга для путешествия. 

6 основных CRUD операций, которые можно реализовать для такого сервиса:

## Создание пользователя и его профиля
Эта операция позволит зарегистрироваться в системе и создать базовый профиль пользователя.

**Метод**: `POST`

**Путь**: `/users`

**Данные запроса**:
```
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password123",
  "country": "USA",
  "city": "New York"
}
```


## Поиск друзей
Эта операция позволит искать потенциальных друзей на основе различных критериев.

**Метод**: `GET`

**Путь**: `/friends/search`

**Данные запроса**:
```
?country=France&interests=cycling,hiking
```

## Подтверждение дружбы
После успешного поиска пользователь может подтвердить дружбу с найденным человеком.

**Метод**: `POST`

**Путь**: `/friendships`

**Данные запроса**:
```
{
  "user_id": 123,
  "friend_id": 456
}
```

## Получение списка друзей
Эта операция позволит получить список уже добавленных друзей пользователя.

**Метод**: `GET`

**Путь**: `/friends`

**Параметры запроса**:
```
?limit=20&offset=0
```

## Обновление профиля пользователя
Пользователи могут изменять свои данные в личном кабинете.

**Метод**: `PATCH`

**Путь**: `/users/{userId}`

**Данные запроса**:
```
{
  "country": "Canada",
  "city": "Toronto"
}
```

## Удаление аккаунта пользователя
Эта операция позволяет полностью удалить учетную запись пользователя из системы.

**Метод**: `DELETE`

**Путь**: `/users/{userId}`


Что важно:

- Не забыть про обработку ошибок и валидацию входных данных.
- Все операции работают асинхронно для улучшения производительности.
- Использование кэширования для часто запрашиваемых данных (?).
- Для сложных операций, таких как поиск друзей, нужно использовать индексирование и оптимизацию запросов.

- Используем соответствующие HTTP методы для каждой операции.
- Приложение можно расширить, добавив дополнительные возможности, такие как обзор профиля, чат между пользователями или планирование совместных мероприятий.