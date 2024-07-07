# Homework
In the demo, we extracted contents from two pages in notion titled "Workshop: Benefits and Perks" and "Workshop: Working hours, PTO, and Vacation". 

Repeat the same process for a third page titled "Homework: Employee handbook":
1. Modify the REST API source to extract only this page.
2. Write the output into a separate table called "homework".
3. Remember to update the table name in all cells where you connect to a lancedb table.

Now, answer the following questions:  
1. How many rows does the lancedb table "notion_pages__homework" have?
    1. 14
    2. 15
    3. 16
    4. 17

2. In the demo, we created an incremental dlt resource `rest_api_notion_incremental` that keeps track of `last_edited_time`. What value does it store after you've run your pipeline once? (Hint: you will be able to get this value by performing some aggregation function on the column `last_edited_time` of the table)
    1. Timestamp('2024-07-05 22:34:00+0000', tz='UTC') (OR "2024-07-05T22:34:00.000Z")
    2. Timestamp('2024-07-05 23:33:00+0000', tz='UTC') (OR "2024-07-05T23:33:00.000Z")
    3. Timestamp('2024-07-05 23:52:00+0000', tz='UTC') (OR "2024-07-05T23:52:00.000Z")
    4. Timestamp('2024-07-05 22:56:00+0000', tz='UTC') (OR "2024-07-05T22:56:00.000Z")



3. Find out with the help of the AI assistant: how many PTO days are the employees entitled to in a year?  
    1. 20
    2. 25
    3. 30
    4. 35