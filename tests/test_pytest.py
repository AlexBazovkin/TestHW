import pytest
from main import search_cx_by_docnumber, search_shelf_by_docnumber, list_all_docs, add_new_doc, directories, documents


FIXTURE_SEARCH_CX = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов")
]


@pytest.mark.parametrize("cx_input, result", FIXTURE_SEARCH_CX)
def test_search_cx_by_docnumber(cx_input, result):
    assert search_cx_by_docnumber(cx_input) == f"Искомый клиент: {result}."


FIXTURE_SEARCH_SHELF = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('5455 028765', '1'),
    ('10006', '2')
]


@pytest.mark.parametrize("cx_input, result", FIXTURE_SEARCH_SHELF)
def test_search_shelf_by_docnumber(cx_input, result):
    assert search_shelf_by_docnumber(cx_input) == f"Искомый документ на {result} полке."


FIXTURE_WRONG_INPUT = [None, '1', '', 'Glory to Arstotzka!']


@pytest.mark.parametrize("cx_input", FIXTURE_WRONG_INPUT)
def test_search_shelf_by_docnumber_wrong_input(cx_input):
    assert search_shelf_by_docnumber(cx_input) == "Нет такого документа. Или полки нет. Или желания искать..."


def test_list_all_docs():
    assert type(list_all_docs()) == str
    assert len(list_all_docs()) > 0


def test_add_new_doc():
    add_new_doc()
    assert 'test_document' in documents[-1]['type']
    assert 'test_number' in documents[-1]['number']
    assert 'test_cx' in documents[-1]['name']
    assert '1' in directories.keys()
