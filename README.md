# Шуліка О. КМ-83. Комп'ютерний практикум 3

## Досягнення цілей КП
Створенний веб-застосунок представляє собою редактор сутностей диллерів та їх місць торгівлі. Для простоти і наглядності
сутність диллер має лише атрибут name, а місце продажу лише атрибут address. Використовуючи функціонал SQLAlchemy, були реалізованні операції зчитування данних,
редагування та видалення існуючих, запис нових данних. Тобто реалізовані усі CRUD операції.

Сутність Dealership має зв'язок один до багатьох з сутністю Saleplace, тому було отримано навички роботи з вкладенними колекціями сутностей. За допомогою функціоналу 
SQLAlchemy була уникнута проблема "N+1 select".

При виконанні роботи було помічено, як зростає складність і кількість коду застосунку при спробах додати ще один рівень абстракції між ORM і бізнес-моделю данних, для
збереження persistence леєру.

## Інструкція по розгортанню

Для розгортання створенного застосунку на сервісі Heroku, був створенний Procfile, який містить необхідну конфігурацію аплікації.
Тому для розгортання данного застосунку достатньо зробити форк цього репозиторію та під'єднати свій GitHub профіль до Heroku профіля і виконати деплой.

## Посилання на розгорнуту систему
Доступна за [посиланням](https://db-course-cp3.herokuapp.com/).

## Діаграма сутність-зв'язок

Доступна за [посиланням](https://drive.google.com/file/d/1PjE7hFobGJbUjjM5H1ZJQuava5Wn7GbE/view?usp=sharing).
