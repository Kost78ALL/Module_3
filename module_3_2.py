def send_email(message, recipient, *, sender = 'university.help@gmail.com', ends_mail = None):
	if ends_mail == None:
		ends_mail = ['.com', '.ru', '.net']
	#print(recipient.find('@'))
	if recipient.find('@') == -1 or sender.find('@') == -1:
		#print(recipient.find('@'))
		#print(sender.find('@'))
		print("Невозможно отправить письмо с адреса",sender,'на адрес',recipient)
		return
	all_test = 1
	for i in range(len(ends_mail)):
		r_test = int(bool(recipient.endswith(ends_mail[i-1])))
		s_test = int(bool(sender.endswith(ends_mail[i-1])))
		if s_test > 0 or s_test >0:
			all_test += 1
	if all_test < 2:
			print("Невозможно отправить письмо с адреса",sender,'на адрес',recipient)
			return
	if sender == recipient:
		print('Нельзя отправить письмо самому себе!')
		return
	elif sender == 'university.help@gmail.com':
		print('Письмо успешно отправлено с адреса',sender,'на адрес',recipient,'.')
		return
	elif sender != 'university.help@gmail.com':
		print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса',sender,' на адрес',recipient,'.')
		return

send_email('Это сообщение для проверки связи', '79052688528@uandex.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')