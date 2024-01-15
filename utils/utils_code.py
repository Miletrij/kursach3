from config import *
import json
from datetime import datetime
import re


def load_json_file():
    """
    Открываем список из файла
    """
    with open(OPERATIONS, encoding="utf-8") as file:
        json_user_operations = json.load(file)
    return json_user_operations


def get_executed_operations(values):
    """
    Сортируем список из выполненных операций
    """
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        elif value["state"] == "EXECUTED":
            executed_operations.append(value)
    return executed_operations


def sort_data_operations(operations):
    """
    Выводим 5 последних успешных операций и сортируем список по дате
    """
    sort_listing = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    list_operations = sort_listing[:5]
    return list_operations


def format_date(data):
    """
    Форматирование даты
    """
    data_operations = []
    for sort_data in data:
        sort_date_operations = datetime.strptime(sort_data["date"], "%Y-%m-%dT%H:%M:%S.%f")
        data_format = f"{sort_date_operations:%d.%m.%Y}"
        data_operations.append(data_format)
    return data_operations


def card_number_mask(card_numbers):
    """
    Шифруем номер карты
    """
    card_operations = []
    for card_number in card_numbers:
        if card_number["description"] == "Открытие вклада":
            card_number["from"] = f"Счет пользователя: {card_number['to'][5:]}"
        card_mask = card_number["from"].split()
        card_mask_copy = card_mask.copy()
        del card_mask_copy[-1]
        card_mask1 = re.findall("....", card_mask[-1])
        number_card = card_mask1[0], card_mask1[1][0:2] + "**", card_mask1[2].replace(card_mask1[2], "****"), card_mask1[3:]
        mask_number = " ".join(number_card[3])
        card_operations.append(f"{' '.join(card_mask_copy)} {' '.join(list(number_card[0:3]))} {mask_number}")
    return card_operations


def amount_number_mask(amount_numbers):
    """
    Шифруем номер счета
    """
    amount_mask_operation = []
    for amount_number in amount_numbers:
        format_for_check = re.findall("....", amount_number["to"])
        check_for_format = format_for_check[4:]
        number_amount = check_for_format[0].replace(check_for_format[0], "**"), check_for_format[1]
        amount_mask = "".join(list(number_amount))
        amount_mask_operation.append(amount_mask)
    return amount_mask_operation
