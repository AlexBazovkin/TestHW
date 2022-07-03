from time import sleep
from pprint import pprint


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]


directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


# add_new_doc() – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

def add_new_doc():
    doc_type = 'test_document' #str(input("Введите тип документа, который хотите добавить: "))
    doc_number = 'test_number' #str(input("Введите номер документа: "))
    doc_cx_name = 'test_cx' #str(input("Введите имя указанное в документе: "))
    shelf_num = '1' #str(input(f"На какую полку поместить?"))

    documents.append(
        {'type': doc_type, 'number': doc_number, 'name': doc_cx_name}
    )

    if shelf_num in directories.keys():
        directories.setdefault(shelf_num, []).append(doc_number)
    else:
        result = "Нет такой полки"
        return result


# list_all_docs() – команда, которая выведет список всех документов;
def list_all_docs():
    for docs in documents:
        result = f'{docs["type"]} "{docs["number"]}" "{docs["name"]}"'
        return result
# print(type(list_all_docs()))


# search_cx_by_docnumber() – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def search_cx_by_docnumber(cx_input):
    result = "Не найдено. И вообще у нас ОБЕД."
    # cx_input = str(input("Введите номер документа: "))
    for dicts in documents:
        if cx_input == dicts["number"]:
            result = f"Искомый клиент: {dicts['name']}."
    return result


# search_shelf_by_docnumber() – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def search_shelf_by_docnumber(cx_input):
    result = "Нет такого документа. Или полки нет. Или желания искать..."
    # cx_input = str(input("Введите номер документа: "))
    for shlf in directories.items():
        if cx_input in shlf[1]:
            result = f"Искомый документ на {shlf[0]} полке."
    return result


def its_bender_time():
    import time
    countdown = ' 321'
    for last_seconds in countdown:
        print(last_seconds)
        time.sleep(1.5)
    result = print("""
				   KILL ALL HUMANS		  
				░░░░░░░░░▄██▄░░░░░░░░░
				░░░░░░░░░████░░░░░░░░░
				░░░░░░░░░░██░░░░░░░░░░
				░░░░░░░░░░██░░░░░░░░░░
				░░░░░░░░░░██░░░░░░░░░░
				░░░░░▄▄████████▄▄░░░░░
				░░░░██████████████░░░░
				░░░████████████████░░░
				░░░████████████████░░░
				░░░████████████████░░░
				░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░
				█░▄█░░░░░▀██▀░░░░░█▄░█
				█░█░░░██░░██░░██░░░█░█
				█░██░░░░░░██░░░░░░██░█
				▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀
				░░░████▀▀█▀▀█▀▀████░░░
				░░░██▄█▄▄█▄▄█▄▄█▄██░░░
				░░░██▄█░░█░░█░░█▄██░░░
				░░░████████████████░░░
				░░░░▀▀██████████▀▀░░░░
				  """)
    return result



# def main():
#     print("""
# Список доступных комманд:
# 1 - поиск полки по номеру документа
# 2 - поиск клиента по номеру документа
# 3 - просмотреть список всех данных
# 4 - добавить новую запись
# 5 - НЕ НАЖИМАТЬ
# q - выход
# """)
#     while True:
#         user_input = input("Введите команду: ")
#         if user_input == "1":
#             search_shelf_by_docnumber()
#         elif user_input == "2":
#             search_cx_by_docnumber()
#         elif user_input == "3":
#             list_all_docs()
#         elif user_input == "4":
#             add_new_doc()
#         elif user_input == "q":
#             break
#         elif user_input == "5":
#             its_bender_time()
#             break
#
#
# main()