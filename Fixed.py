import vk_api
import sqlite3 as sql
import time
import random
import datetime
import json
import wikipedia #Модуль Википедии
import pyowm #погода
now = datetime.datetime.now()
connection = sql.connect("user.sqlite", check_same_thread=False)

q = connection.cursor()

q.execute('''CREATE TABLE user_info
(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Name Varchar (100),
User_ID INTEGER,
Balance INTEGER,
Ownment Varchar(1000)
)
''')

connection.commit()
connection.close()


token = "3b1e3582fae1fac52667913b382db90fb670a045c528b9d92f4acaca821e90ab6692e9f6ca85d9768c6e8"

vk = vk_api.VkApi(token=token)
vk._auth_token()

wikipedia.set_lang("RU")

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": True,
    "buttons": [

    [get_button(label="Профиль", color="positive")],
    [get_button(label="Магазин", color="negative")],
    [get_button(label="Школа", color="primary")],
    [get_button(label="Игры", color="primary")],
    [get_button(label="Инструкция", color="primary")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))



profile = {
    "one_time": True,
    "buttons": [

    [get_button(label="Меню", color="positive")],
    ]
}

profile = json.dumps(profile, ensure_ascii=False).encode('utf-8')
profile = str(profile.decode('utf-8'))



school = {
    "one_time": True,
    "buttons": [

    [get_button(label="Меню", color="positive")],
    [get_button(label="гдз", color="primary")],
    [get_button(label="дз", color="negative")],

    ]
}

school = json.dumps(school, ensure_ascii=False).encode('utf-8')
school = str(school.decode('utf-8'))


shop = {
    "one_time": False,
    "buttons": [

    [get_button(label="Меню", color="default")]

    ]
}

shop = json.dumps(shop, ensure_ascii=False).encode('utf-8')
shop = str(shop.decode('utf-8'))


gdz = {
    "one_time": True,
    "buttons": [

    [get_button(label="Гдз русский", color="positive")],
    [get_button(label="Гдз инглиш", color="negative")],
    [get_button(label="Гдз Алгебра", color="primary")],
    [get_button(label="Гдз Геометрия", color="default")],
    [get_button(label="Меню", color="default")]

    ]
}

gdz = json.dumps(gdz, ensure_ascii=False).encode('utf-8')
gdz = str(gdz.decode('utf-8'))


gdz1 = {
    "one_time": True,
    "buttons": [

    [get_button(label="гдз", color="positive")],
    [get_button(label="меню", color="negative")],
    ]
}

gdz1 = json.dumps(gdz1, ensure_ascii=False).encode('utf-8')
gdz1 = str(gdz1.decode('utf-8'))






while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 200, "filter": "unanswered"})
        if messages["count"] <= 100:
            id = messages['items'][0]['last_message']['peer_id']
            body = messages['items'][0]['last_message']['text']

                            #=========================================Школа==================================================#

            if body.lower() == "школа":
                vk.method("messages.send", {"peer_id": id, "message": "1.🎓Домашка🎓 - дз\n 2. 📝гдз📝 - гд\n 3. Вики *текст* - найти на википедии.", "keyboard": school, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "дз":
                vk.method("messages.send", {"peer_id": id, "message": "Пожалуйста, " + user_name + """,
                    Я хызы. Поинтересуйся у одноклассников.""", "keyboard": school, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "гдз":
                vk.method("messages.send", {"peer_id": id, "message": "Выбери предмет:\n 1. русский \n 2. инглиш\n 3. Алгебра\n 4. Геометрия.", "keyboard": gdz, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "гдз русский":
                vk.method("messages.send", {"peer_id": id, "message": "Лови, https://gdz.ru/class-8/russkii_yazik/trostencova-8/", "keyboard": gdz1, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "гдз инглиш":
                vk.method("messages.send", {"peer_id": id, "message": "Лови, https://gdz.ru/class-8/english/spotlight-workbook/ ( рабочая тетрадь ). https://gdz.ru/class-8/english/reshebnik-spotlight-8-angliyskiy-v-fokuse-vaulina-yu-e/ ( учебник).", "keyboard": gdz1, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "гдз алгебра":
                vk.method("messages.send", {"peer_id": id, "message": "Лови, https://gdz.ru/class-8/algebra/makarychev-8/", "keyboard": gdz1, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "гдз геометрия":
                vk.method("messages.send", {"peer_id": id, "message": "Лови, https://gdz.ru/class-7/geometria/atanasyan-7-9/", "keyboard":gdz1, "random_id": random.randint(1, 2147483647)})
            
            

                            #=========================================Магазинчик==================================================#
            elif body.lower() == "магазин":
                vk.method("messages.send", {"peer_id": id, "message": "Разделы магазина:\n🚙 Транспорт: \n🚗 Машины\n🛥 Яхты\n 🛩 Самолеты\n 🚁 Вертолеты\n \n🏘 Недвижимость:\n 🏠 Дома\n 🌇 Квартиры\n \n📌 Остальное:\n 📱 Телефоны\n\n❓ Для покупки введите «товар [ID]»", "keyboard": shop, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "машины":
                vk.method("messages.send", {"peer_id": id, "message": "🚗Автомобили: \n=============================\n🔸(ID: 1) Renault Logan - 500.000₽ \n 🔸(ID: 2) MAZDA MX-6 - 150.000₽\n 🔸(ID: 3) ВАЗ (Lada) 2131 - 200.000₽\n 🔸(ID: 4) Skoda Rapid - 1.000.000₽\n=============================\n ❓ Для покупки введите «товар [ID]»", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "яхты":
                vk.method("messages.send", {"peer_id": id, "message": "🛥Яхты:\n=============================\n 🔸(ID: 5) PRINCESS 82MY - 700.000₽\n 🔸(ID: 6) SUNSEEKER 34M - 1.400.000₽\n 🔸(ID: 7) AZIMUT 103S - 2.600.000₽\n 🔸(ID: 8) RIVA 68 EGO - 10.000.000\n=============================\n ❓ Для покупки введите «товар [ID]» ", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "самолеты":
                vk.method("messages.send", {"peer_id": id, "message": "✈Самолеты: \n=============================\n🔸(ID: 9) FALCON 7X - 11.000.000₽\n 🔸(ID: 10) GLOBAL 500 - 15.000.000₽\n 🔸(ID: 11) GULFSTREAM G550 - 20.000.000₽\n 🔸(ID: 12) CHALLENGER 605 - 27.000.000₽\n=============================\n ❓ Для покупки введите «товар [ID]»", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "вертолеты":
                vk.method("messages.send", {"peer_id": id, "message": "🚁Вертолеты: \n=============================\n🔸(ID: 13) AW109 POWER BELL 430 - 12.000.000₽\n 🔸(ID: 14) AIRBUS HELICOPTERS H120 - 16.000.000₽\n 🔸(ID: 15) ROBINSON R44 - 19.000.000₽\n 🔸(ID: 16) RAVEN I - 23.000.000₽\n=============================\n ❓ Для покупки введите «товар [ID]»", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "дома":
                vk.method("messages.send", {"peer_id": id, "message": "🏠Дома: \n=============================\n🔸(ID: 17) Домик в деревне - 600.000₽\n 🔸(ID: 18) Коттедж - 2.000.000₽\n 🔸(ID: 19) Дом на берегу моря - 10.000.000₽\n 🔸(ID: 20) Кремль - 21.000.000₽\n=============================\n ❓ Для покупки введите «товар [ID]»", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "телефоны":
                vk.method("messages.send", {"peer_id": id, "message": "📱Телефоны: \n=============================\n🔸(ID: 21) NOKIA 3310 - 3000₽\n 🔸(ID: 22) Samsung Galaxy J5 - 20.000₽\n 🔸(ID: 23) MEIZU M6 - 30.000₽\n 🔸(ID: 24) IPHONE XS MAX - 100.000₽\n=============================\n ❓ Для покупки введите «товар [ID]»", "random_id": random.randint(1, 2147483647)})
            
                    #=========================================Малозначимые==================================================#
            elif body.lower() == "инструкция":
                vk.method("messages.send", {"peer_id": id, "message": """
                Приветсвую. Я - развлекательный бот. Ты можешь спросить у меня домашку(дз), если возникнут сложности я всегда помогу (гдз).
                Насчёт игр, в самом начале ты никто, у тебя 0 рублей и никакого имущества.
                Чтобы заработать первые рубли поиграй в кости(кубик) как только заработаешь несколько рублей - иди в казино.
                Когда заработаешь достаточно денег сходи в магазин. Это был краткий гайд, надеюсь ты всё понял.
                Приятной игры! """, "keyboard": profile, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "игры":
                vk.method("messages.send", {"peer_id": id, "message": "Казино [сумма] \n Кубик [грань] ", "keyboard": profile, "random_id": random.randint(1, 2147483647)})


                    #=========================================Полезности==================================================#

            elif body.lower() == "погода":
                owm = pyowm.OWM('e70ed4cad57ec06b11cd54469fbd487f', language = "ru")  # You MUST provide a valid API key
                observation = owm.weather_at_place("Тамбов")
                w = observation.get_weather()
                temperature = w.get_temperature('celsius')['temp']
                speed = w.get_wind()['speed']
                vk.method("messages.send", {"peer_id": id, "message": "Погода в Тамбове:\n Температура воздуха: " + str(temperature) + " градусов цельсия." +  "\n Скорость ветра: " + str(speed) + " метров в секунду" + "\nСтатус: " + w.get_detailed_status(), "keyboard": profile, "random_id": random.randint(1, 2147483647)})
                if temperature <10:
                    vk.method("messages.send", {"peer_id": id, "message": "На улице очень холодно. Одевайся в тёплую одежду.", "random_id": random.randint(1, 2147483647)})
                elif temperature <20:
                    vk.method("messages.send", {"peer_id": id, "message": "На улице прохладно. Одевайся потеплее.", "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": "Температура норм, одевай что угодно!", "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "время":
                hour = now.strftime("%H")
                minutes = now.strftime("%M")
                seconds = now.strftime("%S")
                hour2 = int(hour) + 3
                vk.method("messages.send", {"peer_id": id, "message": "Текущее время: " + str(hour2) +":" + str(minutes) + ":" + str(seconds) + "!", "random_id": random.randint(1, 2147483647)})

            elif "вики" in body.lower():
                realty6 = str(body.lower().split("вики")[1])
                vk.method("messages.send", {"peer_id": id, "message": "Вот, что я нашла:\n" + str(wikipedia.summary(realty6)), "random_id": random.randint(1, 2147483647)})     
            



                    #=================================Работа с Sqlite3===================================#
            elif body.lower() == "начать" or body.lower() == "помощь" or body.lower() == "меню":
                connection = sql.connect("user.sqlite", check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = '%s'" % (id))
                result = q.fetchall()
                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance, Ownment) VALUES ('%s', '%s', '%s', '%s')" % (
                        user_name,
                        id, 0, ""))
                    connection.commit()
                    connection.close()
                else:
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    print(result)
                    user_name = result[0][1]
                vk.method("messages.send", {"peer_id": id, "message": user_name + """, мои возможности:
                Профиль.
                Игры.
                Магазин.
                Школа.
                Инструкция.

                 """, "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})


            elif body.lower() == "баланс":
                connection = sql.connect("user.sqlite", check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                balance = result[0][3]
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Ваш баланс: " + str(balance) + "₽", "random_id": random.randint(1, 2147483647)})

            elif "кубик" in body.lower():
                cube = random.randint(1, 6)
                user_cube = str(body.lower()[-1])
                user_win = random.randint(100, 1000)
                connection = sql.connect("user.sqlite", check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                      id, 0))
                    connection.commit()
                    connection.close()
                else:
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    print(result)
                    user_name = result[0][1]
                    if user_cube == str(cube):
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": user_name + ", вы угадали! 😯 Выйгрыш " + str(
                                                        user_win) + "₽", "random_id": random.randint(1, 2147483647)})
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                        result = q.fetchall()
                        q.execute(
                            "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (result[0][3] + user_win, id))
                        connection.commit()
                        connection.close()

                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": user_name + ", вы проиграли! Выпало число " + str(
                                                        cube) + " 😔", "random_id": random.randint(1, 2147483647)})
            elif "казино" in body.lower():
                connection = sql.connect('user.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                      id, 0))
                    connection.commit()
                    connection.close()
                else:
                    kazino = random.randint(1, 2)
                    try:
                        rate = int(body.lower().split("казино ")[-1])
                        if result[0][3] >= rate:
                            if kazino == 1:
                                coefficient = random.randint(1, 3)
                                if coefficient == 1:
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(money) +
                                                                                                            rate * 2, id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send",
                                              {"peer_id": id, "message": "Вы выиграли " + str(rate * 2) + "!", "random_id": random.randint(1, 2147483647)})
                                elif coefficient == 2:
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(money) +
                                                                                                            rate * 3, id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send",
                                              {"peer_id": id, "message": "Вы выиграли " + str(rate * 3) + "!", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(money) +
                                                                                                            rate * 7, id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send",
                                              {"peer_id": id, "message": "Вы выиграли " + str(rate * 7) + "!", "random_id": random.randint(1, 2147483647)})
                            elif kazino == 2:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Вы проиграли " + str(rate) + ":(", "random_id": random.randint(1, 2147483647)})
                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                q = connection.cursor()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (result[0][3] - rate, id))
                                connection.commit()
                                connection.close()
                        else:
                            vk.method("messages.send",
                          {"peer_id": id, "message": "Недостаточно средств!", "random_id": random.randint(1, 2147483647)})
                    except:
                        vk.method("messages.send", {"peer_id": id, "message": "Введите корректную сумму ставки!", "random_id": random.randint(1, 2147483647)})
            



                        #==========================================Магазинчик========================================================#

            elif "товар" in body.lower():
                try:
                    connection = sql.connect('user.sqlite', check_same_thread=False)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if len(result) == 0:
                        user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                        user_name = user_info[0]["first_name"]
                        print("Time to добавить юзера")
                        q.execute(
                            "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                          id, 0))
                        connection.commit()
                        connection.close()
                    else:
                        realty = int(body.lower().split("товар")[1])
                        if realty == 1:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 500000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "1,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 500000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Renault Logan!🚘", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("1,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 500000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Renault Logan!🚘", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 2:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 150000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "2,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 150000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили MAZDA MX-6🚘", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("2,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 150000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили MAZDA MX-6🚘", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 3:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 200000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "3,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 200000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили ВАЗ (Lada) 2131🚘", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("3,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 200000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили ВАЗ (Lada) 2131🚘", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 4:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 1000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "4,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 1000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Skoda Rapid🚘", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("4,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 1000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Skoda Rapid🚘", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 5:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 700000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "5,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 700000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили PRINCESS 82MY", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("5,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 700000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили PRINCESS 82MY", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 6:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 1400000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "6,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 1400000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили SUNSEEKER 34M", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("6,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 1400000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили SUNSEEKER 34M", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 7:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 2600000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "7,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 2600000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили AZIMUT 103S", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("7,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 2600000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили AZIMUT 103S", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 8:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 10000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "8,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 10000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили RIVA 68 EGO", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("8,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 10000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили RIVA 68 EGO", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 9:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 11000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "9,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 11000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили FALCON 7X", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("9,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 11000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили FALCON 7X", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 10:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 15000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "10,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 15000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили GLOBAL 500", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("10,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 15000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили GLOBAL 500", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 11:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 20000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "11,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 20000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили GULFSTREAM G550", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("11,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 20000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили GULFSTREAM G550", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 12:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 27000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "12,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 27000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили CHALLENGER 605", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("12,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 27000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили CHALLENGER 605", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 13:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 12000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "13,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 12000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили AW109 POWER BELL 430", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("13,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 12000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили AW109 POWER BELL 430", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 14:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 16000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "14,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 16000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили AIRBUS HELICOPTERS H120", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("14,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 16000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили AIRBUS HELICOPTERS H120", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 15:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 19000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "15,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 19000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили ROBINSON R44", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("15,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 19000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили ROBINSON R44", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 16:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 23000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "16,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 23000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили RAVEN I", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("16,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 23000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили RAVEN I", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 17:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 600000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "17,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 600000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили домик в деревне", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("17,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 600000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили домик в деревне", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 18:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 2000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "18,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 2000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили коттедж", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("19,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 2000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили коттедж", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 19:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 10000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "19,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 10000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили дом на берегу моря", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("19,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 10000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили дом на берегу моря", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 20:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 21000000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "20,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 21000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Кремль", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("20,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 21000000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Кремль", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 21:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 3000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "21,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 3000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили NOKIA 3310", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("21,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 3000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили NOKIA 3310", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 22:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 20000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "22,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 20000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Samsung Galaxy J5", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("22,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 20000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили Samsung Galaxy J5", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 23:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 30000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "23,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 30000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили MEIZU  M6", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("23,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 30000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили MEIZU M6", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 24:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 100000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "24,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 100000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили IPHONE XS MAX", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("24,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 100000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили IPHONE XS MAX", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                except:
                    vk.method("messages.send", {"peer_id": id, "message": "Введите корректный id недвижимости!", "random_id": random.randint(1, 2147483647)})

                #=========================================Админочка==========================================================#

            
            elif "+деньги" in body.lower():
                try:
                    connection = sql.connect('user.sqlite', check_same_thread=False)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if len(result) == 0:
                        user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                        user_name = user_info[0]["first_name"]
                        print("Time to добавить юзера")
                        q.execute(
                            "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                          id, 0))
                        connection.commit()
                        connection.close()
                    else:
                        realty2 = int(body.lower().split("+деньги")[1])
                        if realty2 != 0:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            if user_name == "Ярослав" or user_name == "Павел":
                                q.execute(
                                    "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money + realty2,
                                                                                                      id))
                                connection.commit()
                                connection.close()
                                vk.method("messages.send", {"peer_id": id, "message": str(realty2) + "₽" + " Зачислено на счёт!", "random_id": random.randint(1, 2147483647)})

                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Вы не администратор!", "random_id": random.randint(1, 2147483647)})
                except:
                    vk.method()

            elif body.lower() == "!админ":
                if user_name == "Ярослав" or user_name == "Павел":
                    vk.method("messages.send", {"peer_id": id, "message": "Приветствую, " + user_name + "." + """
                    Возможности Администратора:
                    +деньги[сумма] - выдать себе деньги

                    P.s админ панель в разработке.""", "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": "Вы не администратор!", "random_id": random.randint(1, 2147483647)})



               




            elif body.lower() == "профиль":
                connection = sql.connect('user.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()

                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                      id, 0))
                    connection.commit()
                    connection.close()
                else:
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    user_id = result[0][0]
                    name = result[0][1]
                    balance = result[0][3]
                    ownment = result[0][4]
                    ownment_message = ""
                    if ownment != None:
                        ownment = ownment.split(",")
                        ownment = ownment[:-1]
                        for own in ownment:


                            if int(own) == 1:
                                ownment_message += "🚘Машина:  Renault Logan\n"
                            elif int(own) == 2:
                                ownment_message += "🚘Машина: MAZDA MX-6\n"
                            elif int(own) == 3:
                                ownment_message += "🚘Машина: ВАЗ (Lada) 2131\n"
                            elif int(own) == 4:
                                ownment_message += "🚘Машина: Skoda Rapid\n"
                            elif int(own) == 5:
                                ownment_message += "🛥Яхта: PRINCESS 82MY\n"
                            elif int(own) == 6:
                                ownment_message += "🛥Яхта: SUNSEEKER 34M\n"
                            elif int(own) == 7:
                                ownment_message += "🛥Яхта: AZIMUT 103S\n"
                            elif int(own) == 8:
                                ownment_message += "🛥Яхта: RIVA 68 EGO\n"
                            elif int(own) == 9:
                                ownment_message += "✈ Самолет: FALCON 7X\n"
                            elif int(own) == 10:
                                ownment_message += "✈ Самолет: GLOBAL 500\n"
                            elif int(own) == 11:
                                ownment_message += "✈ Самолет: GULFSTREAM G550\n"
                            elif int(own) == 12:
                                ownment_message += "✈ Самолет: CHALLENGER 605\n"
                            elif int(own) == 13:
                                ownment_message += "🚁 Вертолет: AW109 POWER BELL 430\n"
                            elif int(own) == 14:
                                ownment_message += "🚁 Вертолет: AIRBUS HELICOPTERS H120\n"
                            elif int(own) == 15:
                                ownment_message += "🚁 Вертолет: ROBINSON R44\n"
                            elif int(own) == 16:
                                ownment_message += "🚁 Вертолет: RAVEN I\n"
                            elif int(own) == 17:
                                ownment_message += "🏠 Дом: домик в деревне\n"
                            elif int(own) == 18:
                                ownment_message += "🏠 Дом: коттедж\n"
                            elif int(own) == 19:
                                ownment_message += "🏠 Дом: дом на берегу моря\n"
                            elif int(own) == 20:
                                ownment_message += "🏠 Дом: Кремль\n"
                            elif int(own) == 21:
                                ownment_message += "📱 Телефон: NOKIA 3310\n"
                            elif int(own) == 22:
                                ownment_message += "📱 Телефон: Samsung Galaxy J5\n"
                            elif int(own) == 23:
                                ownment_message += "📱 Телефон: MEIZU M6\n"
                            elif int(own) == 24:
                                ownment_message += "📱 Телефон: IPHONE XS MAX\n"




                    vk.method("messages.send", {"peer_id": id,
                                                "message": user_name + ", твой профиль:\n\n" + "🔎ID: " + str(user_id)
                                                + "\n💰Денег: " + str(balance)+ " ₽" +
                                                           "\n\n🔑Ваши владения:\n " + ownment_message, "keyboard": profile, "random_id": random.randint(1, 2147483647)})


    except:
        time.sleep(1)