import csv
import datetime


# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением
# заметок.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату / время создания или последнего изменения
# заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат(разделение полей рекомендуется делать через точку
# с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры
# запуска программы(команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как - то
# ещё, на усмотрение студента.


def load_notes():
    try:
        with open('notes.csv', 'r') as f:
            reader = csv.reader(f)
            fieldnames = next(reader)
            notes = []
            for row in reader:
                note = {}
                for i, field in enumerate(fieldnames):
                    if field == 'id':
                        note[field] = int(row[i])
                    else:
                        note[field] = row[i]
                notes.append(note)
            return notes
    except FileNotFoundError:
        return []


def save_notes():
    with open('notes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'title', 'body', 'created', 'modified'])
        for note in notes:
            writer.writerow([note['id'], note['title'], note['body'], note['created'], note['modified']])


def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modified = created
    current_id = 0
    if notes:
        for note in notes:
            current_id = note['id']
    note = {'id': current_id + 1, 'title': title, 'body': body, 'created': created, 'modified': modified}
    notes.append(note)
    print("Заметка создана")


def edit_note():
    note_id = int(input("Введите id заметки, которую хотите отредактировать: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        print(f"Редактирование заметки {note['title']}:")
        print(f"Текущее содержание: {note['body']}")
        body = input("Введите новый текст заметки: ")
        modified = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note.update({'body': body, 'modified': modified})
        print("Заметка отредактирована")
    else:
        print("Заметка не найдена")


def delete_note():
    note_id = int(input("Введите id заметки, которую хотите удалить: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        notes.remove(note)
    else:
        print("Заметка не найдена")


def list_notes():
    if notes:
        for note in notes:
            print(f"ID: {note['id']}, заголовок: {note['title']}, дата создания: {note['created']}")
    else:
        print("Список заметок пуст")


def filter_notes_by_date():
    date = input("Введите дату в формате 'YYYY-MM-DD': ")
    filtered_notes = [note for note in notes if note['created'].startswith(date) or note['modified'].startswith(date)]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}, заголовок: {note['title']}, дата создания: {note['created']}")
    else:
        print("Заметки не найдены")


notes = load_notes()

while True:
    print("Выберите действие:")
    print("1. Создать заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Список заметок")
    print("5. Найти заметки по дате")
    print("6. Выход")
    choice = input()
    if choice == "1":
        create_note()
        save_notes()
    elif choice == "2":
        edit_note()
        save_notes()
    elif choice == "3":
        delete_note()
        save_notes()
    elif choice == "4":
        list_notes()
    elif choice == "5":
        filter_notes_by_date()
    elif choice == "6":
        break
    else:
        print("Некорректный ввод")
