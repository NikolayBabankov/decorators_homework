from decorator import decorator_parameter

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
@decorator_parameter('perf.log')
def names_doc(documents_list):
  number = input("Введите номер документа: ")
  names_doc = ''
  for doc in documents_list:
    if doc["number"] == number:
      names_doc = doc["name"]
      break
  return names_doc

@decorator_parameter('perf.log')
def numbers_directories(directories_list):
  number = input("Введите номер документа: ")
  number_dic = 0
  for key,value in directories_list.items():
    for num_dic in value:
      if num_dic == number:
        number_dic = key
        break
  return number_dic

@decorator_parameter('perf.log')
def list_document(document_list):
  print("Список всех документов в базе:")
  for doc in document_list:
    print(doc["type"], ' ',doc["number"], ' ', doc["name"])
  
@decorator_parameter('perf.log')
def add_new_doc(documents_list,directories_list):
  new_doc = {"type": "", "number": "", "name": ""}
  new_doc["type"] = input("Введите названия документа: ")
  new_doc["number"] = input("Введите номер документа: ")
  new_doc["name"] = input("Введите своё имя: ")
  directories_number = input("Введите номер полки куда положить этот документ: ")
  if directories_number in directories_list.keys():
    documents_list.append(new_doc)
    for key, value in directories_list.items():
      if key == directories_number:
        directories_list[key].append(new_doc["number"])
    return documents_list, directories_list
  else:
    str_net = "Полки с таким номером не существует"
    return str_net


def main(dc, di):
  while True:
    user_input = input('Введите команду: ')
    if user_input == 'p':
      print(f"Документ принадлежит : {names_doc(dc)}")
    elif user_input == 's':
      print(f"Документ находится на полке: {numbers_directories(di)}")
    elif user_input == 'l':
      list_document(dc)
    elif user_input == 'a':
      print(add_new_doc(dc,di))
    elif user_input == 'q':
      print('До свидания!')
      break

main(documents,directories)

