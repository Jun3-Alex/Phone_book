import csv

filename = 'contacts.csv'
contacts = []

def load_contacts(filename):
  with open(filename, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      contact = {'Имя': row['Имя'], 
                 'Фамилия': row['Фамилия'],
                 'Номер телефона': row['Номер телефона']}
      contacts.append(contact)

def save_contacts(filename):
  fields = ['Имя', 'Фамилия', 'Номер телефона']
  with open(filename, 'w', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields) 
    writer.writeheader()
    for contact in contacts:
      writer.writerow(contact)

def add_contact(filename):
  name = input("Введите имя: ")
  surname = input("Введите фамилию: ")  
  phone = input("Введите номер телефона: ")
  
  contact = {'Имя': name, 'Фамилия': surname, 'Номер телефона': phone}
  contacts.append(contact)
  save_contacts(filename)
  
  print("Контакт добавлен")

def search_contacts(query):
  results = []
  for contact in contacts:
    if query in contact['Имя'] or query in contact['Фамилия']:
      results.append(contact)
  return results

def print_contacts(contacts):
  if not contacts:
    print("Контакты не найдены")
    return
  
  for i, contact in enumerate(contacts):
    print(f"Контакт {i+1}")
    print(f"Имя: {contact['Имя']}")
    print(f"Фамилия: {contact['Фамилия']}")
    print(f"Телефон: {contact['Номер телефона']}")
    print()

def change_contact(contacts):
  query = input("Введите имя или фамилию для поиска: ")
  results = search_contacts(query)
  
  if not results:
    print("Контакт не найден")
    return  
  print_contacts(results)
  
  index = int(input("Введите индекс контакта для редактирования: ")) - 1
  
  if 0 <= index < len(results):  
    contact = results[index]
    
    field = input("Какое поле изменить (Имя, Фамилия, Номер телефона): ")
    value = input(f"Введите новое значение для {field}: ")  
    contact[field] = value
    
    save_contacts(filename)
    print("Контакт изменен")
  else:
    print("Неверный индекс контакта")

def delete_contact():
  query = input("Введите имя или фамилию для поиска: ")
  results = search_contacts(query)

  if not results:
    print("Контакт не найден")
    return

  print_contacts(results)

  index = int(input("Введите индекс контакта для удаления: ")) - 1

  if 0 <= index < len(results):
    contact = results[index]
    contacts.remove(contact)
    save_contacts(filename)
    print("Контакт удален")

  else:
    print("Неверный индекс контакта")

def show_menu():
  print("\nМеню:")
  print("1. Показать все контакты")
  print("2. Добавить новый контакт")
  print("3. Поиск контакта")
  print("4. Редактировать контакт")
  print("5. Удалить контакт") 
  print("6. Выйти из программы")



def option(filename):
  
  load_contacts(filename)

  while True:
    show_menu()
    option = input("Выберите действие: ")

    match option:
      case "1":
        print_contacts(contacts)
      case "2":
        add_contact(filename)  
      case "3":
        query = input("Введите имя или фамилию для поиска: ")
        results = search_contacts(query)
        print_contacts(results)
      case "4":  
        change_contact(contacts)
      case "5":
        delete_contact()
      case "6":
        print("Выход")
        break
      case _:
        print("Неверный ввод")
option(filename)

