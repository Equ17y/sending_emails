import smtplib
import os 
from dotenv import load_dotenv

load_dotenv()
friend_name = "Алексей"
my_name = "Антон"
website = 'https://dvmn.org/profession-ref-program/sobol.tosha/TOnJT/'
email_from = os.environ['login']
email_to = os.environ['login']
password = os.environ['password']
email_subject = "Приглашение!"

letter = """From: {email_from}
To: {email_to}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

formatted_letter = letter.format(
email_from=email_from,
email_to=email_to,
subject=email_subject
).replace("%friend_name%", friend_name) \
.replace("%my_name%", my_name) \
.replace("%website%", website)
 
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(email_from, password)
server.sendmail(email_from,email_to, formatted_letter.encode("UTF-8"))
server.quit()
