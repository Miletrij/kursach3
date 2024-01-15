import pytest
from utils.utils_code import *


def test_get_executed_operations():
    assert get_executed_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert get_executed_operations([{}]) == []


def test_sort_data_operations():
    assert sort_data_operations([{"date": "2019-08-26T10:50:58.294041"},
                                 {"date": "2019-07-03T18:35:29.512364"},
                                 {"date": "2018-06-30T02:08:58.425572"},
                                 {"date": "2018-03-23T10:45:06.972075"},
                                 {"date": "2019-04-04T23:20:05.206878"},
                                 {"date": "2019-03-23T01:09:46.296404"}]) == [{'date': '2019-08-26T10:50:58.294041'},
                                                                              {'date': '2019-07-03T18:35:29.512364'},
                                                                              {'date': '2019-04-04T23:20:05.206878'},
                                                                              {'date': '2019-03-23T01:09:46.296404'},
                                                                              {'date': '2018-06-30T02:08:58.425572'}]


def test_format_date():
    assert format_date([{"date": "2019-08-26T10:50:58.294041"}]) == ["26.08.2019"]


def test_card_number_mask():
    assert (card_number_mask([{"from": "Maestro 1596837868705199", "description": "Перевод организации"}]) ==
            (["Maestro 1596 83** **** 5199"]))


def test_amount_number_mask():
    assert amount_number_mask([{"to": "Счет 6468647367889477958"}]) == ["**7958"]
