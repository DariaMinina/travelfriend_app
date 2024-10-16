#!/bin/bash

# Определяем имя виртуального окружения
VENV_NAME=".venv"

# Создаем виртуальное окружение
python3.8 -m venv $VENV_NAME

# Активируем виртуальное окружение
source $VENV_NAME/bin/activate

# Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt

# Запускаем скрипт app.py
python app.py
