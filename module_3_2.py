extensions = ['.com', '.ru', '.net']


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    global extensions
    a = 0
    if "@" in recipient and "@" in sender:
        for ext in extensions:
            if ext not in recipient:
                a += 1
                if a == 3:
                    print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
            else:
                a = 0
                for ex in extensions:
                    if ex not in sender:
                        a += 1
                        if a == 3:
                            print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
                    else:
                        if sender == recipient:
                            print("Нельзя отправить письмо самому себе!")
                        elif sender != "university.help@gmail.com":
                            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
                        elif sender == "university.help@gmail.com":
                            print("Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)
                break
    else:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')