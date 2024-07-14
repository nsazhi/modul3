def send_email(message, recipient, *,sender='university.help@gmail.com'):
    message_info = [message, recipient, sender]
    mails = ['.com', '.ru', '.net']
    for i in message_info:
        for j in range(1, len(message_info)):
            is_mail = True
            if '@' not in message_info[j]:
                is_mail = False
                break
            for k in mails:
                    if k not in message_info[j]:
                        is_mail = False
                        continue
                    else:
                        is_mail = True
                        break
            if is_mail:
                continue
        if is_mail:
            if sender == recipient:
                print('Нельзя отправить письмо самому себе!')
                break
            if 'university.help@gmail.com' in sender:
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                break
            if 'university.help@gmail.com' not in sender:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
                break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print('=======================')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print('=======================')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print('=======================')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')