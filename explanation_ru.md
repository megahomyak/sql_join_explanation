# Императивное объяснение JOINов в SQL


## INNER JOIN

Для каждой записи из таблицы слева ищем записи
из таблицы справа, которые подходят под условие,
и добавляем в итоговую таблицу.


## LEFT JOIN

Для каждой записи из таблицы слева ищем записи из таблицы справа, которые
подходят под условие, и добавляем в итоговую таблицу, а если таких записей не
найдено, то добавляем в итоговую таблицу одну строку, где все поля, которые
должны быть взяты из таблицы справа, будут заполнены NULLами.


## RIGHT JOIN

Для каждой записи из таблицы справа ищем записи из таблицы слева, которые
подходят под условие, и добавляем в итоговую таблицу, а если таких записей не
найдено, то добавляем в итоговую таблицу одну строку, где все поля, которые
должны быть взяты из таблицы слева, будут заполнены NULLами.


## FULL JOIN

Для каждой записи из таблицы слева ищем записи из таблицы справа, которые
подходят под условие, и добавляем в итоговую таблицу, а если таких записей не
найдено, то добавляем в итоговую таблицу одну строку, где все поля, которые
должны быть взяты из таблицы справа, будут заполнены NULLами.

Для каждой записи из таблицы справа ищем записи из таблицы слева, которые
подходят под условие, и добавляем в итоговую таблицу, если такой записи
(с использованием тех же двух строк из левой и правой таблиц соответственно)
ещё в итоговой таблице нет, а если подходящие под условие записи в таблице
слева не найдены, то добавляем в итоговую таблицу одну строку, где все поля,
которые должны быть взяты из таблицы справа, будут заполнены NULLами.
