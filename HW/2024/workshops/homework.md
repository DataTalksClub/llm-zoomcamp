### Домашнє завдання

У демонстрації ми витягли вміст з двох сторінок у Notion під назвою "Workshop: Benefits and Perks" та "Workshop: Working hours, PTO, and Vacation".

Повторіть цей процес для третьої сторінки під назвою "Homework: Employee handbook":
1. Змініть джерело REST API для витягу тільки цієї сторінки.
2. Запишіть результат у окрему таблицю під назвою "homework".
3. Не забудьте оновити назву таблиці у всіх комірках, де ви підключаєтесь до таблиці lancedb.

Тепер дайте відповіді на наступні запитання:
1. Скільки рядків має таблиця lancedb "notion_pages__homework"?
    1. 14
    2. 15
    3. 16
    4. 17

Q1: 17

2. У демонстрації ми створили інкрементальний ресурс dlt `rest_api_notion_incremental`, який відстежує `last_edited_time`. 
Яке значення він зберігає після одноразового запуску вашого пайплайну? 
(Підказка: ви зможете отримати це значення, виконавши деяку агрегатну функцію на стовпці `last_edited_time` таблиці)
    1. Timestamp('2024-07-05 22:34:00+0000', tz='UTC') (або "2024-07-05T22:34:00.000Z")
    2. Timestamp('2024-07-05 23:33:00+0000', tz='UTC') (або "2024-07-05T23:33:00.000Z")
    3. Timestamp('2024-07-05 23:52:00+0000', tz='UTC') (або "2024-07-05T23:52:00.000Z")
    4. Timestamp('2024-07-05 22:56:00+0000', tz='UTC') (або "2024-07-05T22:56:00.000Z")
Q2: 2024-07-08 15:35:00+00:00
```python
import lancedb

# Підключаємося до LanceDB
db = lancedb.connect(".lancedb")

# Відкриваємо таблицю
dbtable = db.open_table("notion_pages___employee_handbook")

# Перетворюємо таблицю в pandas DataFrame
df = dbtable.to_pandas()

# Виконуємо агрегатну функцію, наприклад, знаходимо максимальне значення last_edited_time
last_edited_time = df['last_edited_time'].max()

print(last_edited_time)
# output 2024-07-08 15:35:00+00:00
'''

3. Дізнайтесь за допомогою AI-асистента: скільки днів PTO мають право отримати співробітники на рік?
    1. 20
    2. 25
    3. 30
    4. 35
Q3: 20
You: How many PTO days are employees entitled to receive per year?
Assistant: You are entitled to receive [20 days] per year as paid time off (PTO). Your PTO accrual begins the day you join our company and you receive 1.7 days per month. You can take your PTO at any time after your first week with us, but we encourage you to use it throughout the year. If you leave our company before using all of your earned PTO, we will compensate accrued PTO with your final paycheck according to local law. 
These holidays are considered “off-days” for most employees. Non-exempt employees will receive their regular hourly rate with a premium for working on a holiday. Exempt employees will be granted an additional day of PTO that they must take within 12 months after the holiday.
If you need to work on a holiday, inform your manager or HR three days in advance.'