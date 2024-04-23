import mysql.connector # бібліотека для роботи з MySQL

def execute_show(query):
    if True:
        db_connection = mysql.connector.connect( 
            host="localhost",
            user="root",
            password="904496Vfrc",
            database="abdc_6"
        )     # Встановлення з'єднання з базою даних

        cursor = db_connection.cursor() # об'єкт cursor для виконання SQL-запитів в базі даних через з'єднання
        cursor.execute(query) # виконання SQL-запиту

        column_names = [column[0] for column in cursor.description]     # Отримання імен стовпців з об'єкта cursor.description
        
        max_lengths = [len(column) for column in column_names]     # Знайдіть найбільшу довжину для кожного стовпця
        
        results = cursor.fetchall()    # Отримання всіх рядків результатів виконання запиту

    # Знайдіть максимальну довжину для кожного стовпця в результатах
        for row in results:
            for i, value in enumerate(row):
                max_lengths[i] = max(max_lengths[i], len(str(value))) # максимальна довжина для кожного стовпця 

    # Виведення назв стовпців
        for i, column_name in enumerate(column_names):
            print(column_name.ljust(max_lengths[i]), end="\t") # Вирівнювання назв стовпців

        print()  # Пустий рядок між навзвами таблиць та даними

    # Виведення результатів з табулюванням
        for row in results:
            for i, value in enumerate(row):
                print(str(value).ljust(max_lengths[i]), end="\t") # Вирівнювання даних
            print()  # Перехід до нового рядка
    
    # Закриття курсора та з'єднання
        cursor.close()
        db_connection.close()
    # except mysql.connector.Error as error:
    # print("Помилка при виконанні запиту:", error)

def execute_save(query):
    
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="904496Vfrc",
            database="abdc_6",
            autocommit=True
        )

        cursor = db_connection.cursor()
        cursor.execute(query)

        print("Дані успішно додані до бази даних.")
        
        cursor.close()
        db_connection.close()

    except mysql.connector.Error as error:
        print("Помилка при виконанні запиту:", error)

def exxxpert():
    print("Виберіть запит: ")
    print("Напиши 1, щоб показати табличку")
    print("Напиши 2, щоб показати стуктуру таблички ")
    print("Напишіть 3, щоб показало вивід запиту з використанням масок та математичних дій")
    print("Напишіть 4, щоб показало відфільтровані значення, де офісний номер більший за певне число")
    print("Напишіть 5, щоб показало відфільтровані значення, де офісний номер рівний певному числу")
    print("Напишіть 6, щоб показало відфільтровані значення, де офісний номер менший за певне число")
    print("Напишіть 7, щоб показало відфільтроване значення, де офісний номер належить певному діапазону")
    print("Напишіть 8, щоб показало вивід запиту з використанням оператора and")
    print("Напишіть 9, щоб показало вивід запиту з використанням оператора or")
    print("Напишіть 10, щоб показало вивід запиту з використанням оператора not")
    print("Напишіть 11, щоб показало вивід запиту, що сортує офісний номер(за зростанням)")
    print("Напишіть 12, щоб показало вивід запиту, що сортує офісний номер(за спаданням)")
    print("Напишіть 13, щоб додати новий рядок у таблицю")
    print("Напишіть 14, щоб оновити дані у певному стовпці і рядку")
    print("Напишіть 15, щоб ввести свій запит")
    print("Напишіть 16, щоб видалити рядок з таблиці")
    print("Напишіть 17, щоб вийти")

    choise = input("Choose: ")
    match choise:
        case "1":
            query = "select * from exxxpert"
            execute_show(query)
        case "2":
            query = "desc exxxpert"
            execute_show(query)
        case "3":
            query = "select office_number + 5 as new_number from exxxpert;"
            execute_show(query)
        case "4":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from exxxpert where office_number > {number}"
            execute_show(query)
        case "5":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from exxxpert where office_number = {number}"
            execute_show(query)
        case "6":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from exxxpert where office_number < {number}"
            execute_show(query)
        case "7":
            number_1 = input("Введіть першу межу фільтрування: ")
            number_2 = input("Введіть другу межу фільтрування: ")
            query = f"select * from exxxpert where office_number between {number_1} and {number_2}"
            execute_show(query)
        case "8":
            value_1 = input("Введіть офісний номер: ")
            value_2 = input("Введіть спеціалізацію: ")
            query = f"select * from exxxpert where office_number = {value_1} and specialization = '{value_2}'"
            execute_show(query)
        case "9":
            value_1 = input("Введіть офісний номер: ")
            value_2 = input("Введіть спеціалізацію: ")
            query = f"select * from exxxpert where office_number = {value_1} or specialization = '{value_2}'"
            execute_show(query)
        case "10":
            value_1 = input("Введіть офісні номера, які не треба виводити: ")
            query = f"select * from exxxpert where office_number not in({value_1})"
            execute_show(query)
        case "11":
            query = "select * from exxxpert order by office_number asc"
            execute_show(query)
        case "12":
            query = "select * from exxxpert order by office_number desc"
            execute_show(query)
        case "13":
            value_1 = input("Введіть персональний номер: ")
            value_2 = input("Введіть ПІБ: ")
            value_3 = input("Введіть спеціалізацію: ")
            value_4 = input("Введіть адресу: ")
            value_5 = input("Введіть номер телефону: ")
            value_6 = input("Введіть офісний номер: ")
            query = f"insert into exxxpert (personal_number, S_M_P, specialization, addres, phone_number, office_number) " \
            f"VALUES ('{value_1}', '{value_2}', '{value_3}', '{value_4}', '{value_5}', '{value_6}');"
            execute_save(query)
        case "14":
            choise = input("Дані якої колонки хочете оновити?: ")
            new_value = input("Введіть нове значення: ")
            id = input("Введіть значення id в рядку, де хочете оновити дані: ")
            query = f"update exxxpert set {choise} = '{new_value}' where id = {id};"
            execute_save(query)
        case "15":
            query = input("Введіть ваш запит: ")
            execute_show(query)
        case "16":
            id = input("Введіть ваш id: ")
            query = f"delete from exxxpert where id = {id}"
            execute_save(query)
        case "17":
            menu_yes_no()

def MedicalRecords():
    print("Виберіть запит: ")
    print("Напиши 1, щоб показати табличку")
    print("Напиши 2, щоб показати стуктуру таблички ")
    print("Напишіть 3, щоб показало вивід запиту з використанням масок та математичних дій")
    print("Напишіть 4, щоб показало відфільтровані значення, де номер запису більший за певне число")
    print("Напишіть 5, щоб показало відфільтровані значення, де номер запису рівний певному числу")
    print("Напишіть 6, щоб показало відфільтровані значення, де номер запису менший за певне число")
    print("Напишіть 7, щоб показало відфільтроване значення, де номер запису належить певному діапазону")
    print("Напишіть 8, щоб показало вивід запиту з використанням оператора and")
    print("Напишіть 9, щоб показало вивід запиту з використанням оператора or")
    print("Напишіть 10, щоб показало вивід запиту з використанням оператора not")
    print("Напишіть 11, щоб показало вивід запиту, що сортує номер запису(за зростанням)")
    print("Напишіть 12, щоб показало вивід запиту, що сортує номер запису(за спаданням)")
    print("Напишіть 13, щоб додати новий рядок у таблицю")
    print("Напишіть 14, щоб оновити дані у певному стовпці і рядку")
    print("Напишіть 15, щоб ввести свій запит")
    print("Напишіть 16, щоб видалити рядок з таблиці")
    print("Напишіть 17, щоб вийти")

    choise = input("Choose: ")
    match choise:
        case "1":
            query = "select * from MedicalRecords"
            execute_show(query)
        case "2":
            query = "desc MedicalRecords"
            execute_show(query)
        case "3":
            query = "select record_id + 5 as new_record_id from MedicalRecords;"
            execute_show(query)
        case "4":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from MedicalRecords where record_id > {number}"
            execute_show(query)
        case "5":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from MedicalRecords where record_id = {number}"
            execute_show(query)
        case "6":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from MedicalRecords where record_id < {number}"
            execute_show(query)
        case "7":
            number_1 = input("Введіть першу межу фільтрування: ")
            number_2 = input("Введіть другу межу фільтрування: ")
            query = f"select * from MedicalRecords where record_id between {number_1} and {number_2}"
            execute_show(query)
        case "8":
            value_1 = input("Введіть номер запису: ")
            value_2 = input("Введіть стать: ")
            query = f"select * from MedicalRecords where record_id = {value_1} and gender = '{value_2}'"
            execute_show(query)
        case "9":
            value_1 = input("Введіть номер запису: ")
            value_2 = input("Введіть стать: ")
            query = f"select * from MedicalRecords where record_id = {value_1} or gender = '{value_2}'"
            execute_show(query)
        case "10":
            value_1 = input("Введіть номера запису, які не треба виводити: ")
            query = f"select * from MedicalRecords where record_id not in({value_1})"
            execute_show(query)
        case "11":
            query = "select * from MedicalRecords order by record_id asc"
            execute_show(query)
        case "12":
            query = "select * from MedicalRecords order by record_id desc"
            execute_show(query)
        case "13":
            value_1 = input("Введіть ПІБ: ")
            value_2 = input("Введіть стать: ")
            value_3 = input("Введіть дату народження(у форматі рік-місяць-дата: ) ")
            value_4 = input("Введіть адресу: ")
            value_5 = input("Введіть номер телефону: ")
            query = f"insert into MedicalRecords (full_name, gender, birth_date, address, phone_number) " \
            f"VALUES ('{value_1}', '{value_2}', '{value_3}', '{value_4}', '{value_5}');"
            execute_save(query)
        case "14":
            choise = input("Дані якої колонки хочете оновити?: ")
            new_value = input("Введіть нове значення: ")
            id = input("Введіть значення id в рядку, де хочете оновити дані: ")
            query = f"update MedicalRecords set {choise} = '{new_value}' where record_id = {id};"
            execute_save(query)
        case "15":
            query = input("Введіть ваш запит: ")
            execute_show(query)
        case "16":
            id = input("Введіть ваш id: ")
            query = f"delete from MedicalRecords where record_id = {id}"
            execute_save(query)
        case "17":
            menu_yes_no()

def RegistrationJournal():
    print("Виберіть запит: ")
    print("Напиши 1, щоб показати табличку")
    print("Напиши 2, щоб показати стуктуру таблички ")
    print("Напишіть 3, щоб показало вивід запиту з використанням масок та математичних дій")
    print("Напишіть 4, щоб показало відфільтровані значення, де вартість послуги більшf за певне число")
    print("Напишіть 5, щоб показало відфільтровані значення, де вартість послуги рівниа певному числу")
    print("Напишіть 6, щоб показало відфільтровані значення, де вартість послуги менша за певне число")
    print("Напишіть 7, щоб показало відфільтроване значення, де вартість послуги належить певному діапазону")
    print("Напишіть 8, щоб показало вивід запиту з використанням оператора and")
    print("Напишіть 9, щоб показало вивід запиту з використанням оператора or")
    print("Напишіть 10, щоб показало вивід запиту з використанням оператора not")
    print("Напишіть 11, щоб показало вивід запиту, що сортує вартість послуги(за зростанням)")
    print("Напишіть 12, щоб показало вивід запиту, що сортує вартість послуги(за спаданням)")
    print("Напишіть 13, щоб додати новий рядок у таблицю")
    print("Напишіть 14, щоб оновити дані у певному стовпці і рядку")
    print("Напишіть 15, щоб ввести свій запит")
    print("Напишіть 16, щоб видалити рядок з таблиці")
    print("Напишіть 17, щоб вийти")

    choise = input("Choose: ")
    match choise:
        case "1":
            query = "select * from RegistrationJournal"
            execute_show(query)
        case "2":
            query = "desc RegistrationJournal"
            execute_show(query)
        case "3":
            query = "select service_cost * 2 as new_service_cost from RegistrationJournal;"
            execute_show(query)
        case "4":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from RegistrationJournal where service_cost > {number}"
            execute_show(query)
        case "5":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from RegistrationJournal where service_cost = {number}"
            execute_show(query)
        case "6":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from RegistrationJournal where service_cost < {number}"
            execute_show(query)
        case "7":
            number_1 = input("Введіть першу межу фільтрування: ")
            number_2 = input("Введіть другу межу фільтрування: ")
            query = f"select * from RegistrationJournal where service_cost between {number_1} and {number_2}"
            execute_show(query)
        case "8":
            value_1 = input("Введіть номер прийому: ")
            value_2 = input("Введіть номер лікаря: ")
            query = f"select * from RegistrationJournal where visit_number = {value_1} and specialist_id = '{value_2}'"
            execute_show(query)
        case "9":
            value_1 = input("Введіть номер прийому: ")
            value_2 = input("Введіть номер лікаря: ")
            query = f"select * from RegistrationJournal where visit_number = {value_1} or specialist_id = '{value_2}'"
            execute_show(query)
        case "10":
            value_1 = input("Введіть номера прийому, які не треба виводити: ")
            query = f"select * from RegistrationJournal where visit_number not in({value_1})"
            execute_show(query)
        case "11":
            query = "select * from RegistrationJournal order by service_cost asc"
            execute_show(query)
        case "12":
            query = "select * from RegistrationJournal order by service_cost desc"
            execute_show(query)
        case "13":
            value_1 = input("Введіть номер пацієнта(існуюче): ")
            value_2 = input("Введіть номер спеціаліста(існуюче): ")
            value_3 = input("Введіть номер прийому: ")
            value_4 = input("Введіть дату прийому: ")
            value_5 = input("Введіть причину звернення: ")
            value_6 = input(" Введіть діагноз: ")
            value_7 = input("Введіть лікування: ")
            value_8 = input("Введіть вартість послуги: ")
            query = f"insert into RegistrationJournal (patient_id, specialist_id, visit_number, visit_date, complaints, diagnosis, treatment, service_cost) " \
            f"VALUES ('{value_1}', '{value_2}', '{value_3}', '{value_4}', '{value_5}', '{value_6}', '{value_7}', '{value_8}');"
            execute_save(query)
        case "14":
            choise = input("Дані якої колонки хочете оновити?: ")
            new_value = input("Введіть нове значення: ")
            id = input("Введіть значення id в рядку, де хочете оновити дані: ")
            query = f"update RegistrationJournal set {choise} = '{new_value}' where registration_id = {id};"
            execute_save(query)
        case "15":
            query = input("Введіть ваш запит: ")
            execute_show(query)
        case "16":
            id = input("Введіть ваш id: ")
            query = f"delete from RegistrationJournal where registration_id = {id}"
            execute_save(query)
        case "17":
            menu_yes_no()

def ReferralJournal():
    print("Виберіть запит: ")
    print("Напиши 1, щоб показати табличку")
    print("Напиши 2, щоб показати стуктуру таблички ")
    print("Напишіть 3, щоб показало вивід запиту з використанням масок та математичних дій")
    print("Напишіть 4, щоб показало відфільтровані значення, де  айді спеціаліста, що провів процедуру більший за певне число")
    print("Напишіть 5, щоб показало відфільтровані значення, де  айді спеціаліста, що провів процедуру рівний певному числу")
    print("Напишіть 6, щоб показало відфільтровані значення, де  айді спеціаліста, що провів процедуру менший за певне число")
    print("Напишіть 7, щоб показало відфільтроване значення, де  айді спеціаліста, що провів процедуру належить певному діапазону")
    print("Напишіть 8, щоб показало вивід запиту з використанням оператора and")
    print("Напишіть 9, щоб показало вивід запиту з використанням оператора or")
    print("Напишіть 10, щоб показало вивід запиту з використанням оператора not")
    print("Напишіть 11, щоб показало вивід запиту, що сортує  айді спеціаліста, що провів процедуру(за зростанням)")
    print("Напишіть 12, щоб показало вивід запиту, що сортує  айді спеціаліста, що провів процедуру(за спаданням)")
    print("Напишіть 13, щоб додати новий рядок у таблицю")
    print("Напишіть 14, щоб оновити дані у певному стовпці і рядку")
    print("Напишіть 15, щоб ввести свій запит")
    print("Напишіть 16, щоб видалити рядок з таблиці")
    print("Напишіть 17, щоб вийти")

    choise = input("Choose: ")
    match choise:
        case "1":
            query = "select * from ReferralJournal"
            execute_show(query)
        case "2":
            query = "desc ReferralJournal"
            execute_show(query)
        case "3":
            query = "select date_add(procedure_date, interval 5 day) as new_date FROM ReferralJournal;"
            execute_show(query)
        case "4":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from ReferralJournal where performing_specialist_id > {number}"
            execute_show(query)
        case "5":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from ReferralJournal where performing_specialist_id = {number}"
            execute_show(query)
        case "6":
            number = input("Введіть число для фільтрації: ")
            query = f"select * from ReferralJournal where performing_specialist_id < {number}"
            execute_show(query)
        case "7":
            number_1 = input("Введіть першу межу фільтрування: ")
            number_2 = input("Введіть другу межу фільтрування: ")
            query = f"select * from ReferralJournal where performing_specialist_id between {number_1} and {number_2}"
            execute_show(query)
        case "8":
            value_1 = input("Введіть  айді спеціаліста, що провів процедуру: ")
            value_2 = input("Введіть айді пацієнта: ")
            query = f"select * from ReferralJournal where performing_specialist_id = {value_1} and patient_id = '{value_2}'"
            execute_show(query)
        case "9":
            value_1 = input("Введіть  айді спеціаліста, що провів процедуру: ")
            value_2 = input("Введіть айді пацієнта: ")
            query = f"select * from ReferralJournal where performing_specialist_id = {value_1} or patient_id = '{value_2}'"
            execute_show(query)
        case "10":
            value_1 = input("Введіть  айді спеціалістів, що провели процедури, які не треба виводити: ")
            query = f"select * from ReferralJournal where performing_specialist_id not in({value_1})"
            execute_show(query)
        case "11":
            query = "select * from ReferralJournal order by performing_specialist_id asc"
            execute_show(query)
        case "12":
            query = "select * from ReferralJournal order by performing_specialist_id desc"
            execute_show(query)
        case "13":
            value_1 = input("Введіть назву процедури: ")
            value_2 = input("Введіть айді пацієнта(існуюче): ")
            value_3 = input("Введіть айді спеціаліста, що направив(існуюче): ")
            value_4 = input("Введіть айді спеціаліста, що провів процедуру(існуюче): ")
            value_5 = input("Введіть дату процедури: ")
            value_6 = input("Введіть результат: ")
            query = f"insert into ReferralJournal (procedure_analysis_name, patient_id, referring_specialist_id, performing_specialist_id, procedure_date, results) " \
            f"VALUES ('{value_1}', '{value_2}', '{value_3}', '{value_4}', '{value_5}', '{value_6}');"
            execute_save(query)
        case "14":
            choise = input("Дані якої колонки хочете оновити?: ")
            new_value = input("Введіть нове значення: ")
            id = input("Введіть значення id в рядку, де хочете оновити дані: ")
            query = f"update ReferralJournal set {choise} = '{new_value}' where referral_id = {id};"
            execute_save(query)
        case "15":
            query = input("Введіть ваш запит: ")
            execute_show(query)
        case "16":
            id = input("Введіть ваш id: ")
            query = f"delete from ReferralJournal where referral_id = {id}"
            execute_save(query)
        case "17":
            menu_yes_no()

def menu_yes_no():
    print("Хочете продовжити?")
    print("Напишіть 1, щоб продовжити")
    print("Напишіть 2, щоб вийти")
    choise = input("Введіть ваш запит:")
    match choise:
        case "1":
            start_menu()
        case "2":
            exit()

def menu_user_choise():
    choise = input("Ваш вибір: ")
    match choise:
        case "1":
            exxxpert()
        case "2":
            MedicalRecords()
        case "3":
            RegistrationJournal()
        case "4":
            ReferralJournal()
        case "5":
            query = "show tables"
            execute_show(query)
        case "6":
            exit()

def start_menu():
    print("Напиши 1, щоб перейти до меню запитів з табличкою exxxpert")
    print("Напиши 2, щоб перейти до меню запитів з табличкою MedicalRecords")
    print("Напиши 3, щоб перейти до меню запитів з табличкою RegistrationJournal")
    print("Напиши 4, щоб перейти до меню запитів з табличкою ReferralJournal")
    print("Напиши 5, щоб побачити список усіх таблиць")
    print("Напиши 6, щоб вийти з програми")
    menu_user_choise()

def main():
    start_menu()
    while True:
        menu_yes_no()
if __name__ == "__main__":

    main()