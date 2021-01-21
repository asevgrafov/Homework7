# Homework7

**ЭкспрессКурьер**

Для командного проекта по приложению для службы курьерской доставки вам выпала задача написать асинхронное веб-приложение.
Ваша часть приложения работает с уникальными номерами доставок и статусами и делает две вещи: 

1) по post-запросу записывает/обновляет запись в таблице в бд.
2) по get-запросу выдаёт список всех текущих доставок.
3) В таблице достаточно хранить только уникальный идентификатор доставки и статус.
4) Статус может быть трёх типов: обрабатывается, выполняется, доставлено.
5) Уникальный идентификатор состоит из маленьких латинских букв и цифр и его длина от 2 до 5 символов.
   
**Требования:**

1) Написать приложения в соответствии с описанием
2) Валидировать тела post-запроса по json-схеме
3) Приложить locust-файл в котором есть сценарии обращения по post и get запросам

**Роуты:**

```GET  /order - получение списка всех заказов``

``POST /orders - создание/изменение заказа```