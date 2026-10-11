ИНФОРМАТИКА — СТАТИЧЕСКИЙ УЧЕБНЫЙ САЙТ

Для запуска откройте index.html. Интернет и сервер не нужны.

СТРУКТУРА
index.html       — главная страница
styles.css       — ЕДИНСТВЕННЫЙ общий файл стилей
data.js          — названия разделов и уроков (из 4 таблиц КТП)
10class/base/lesson1/{lection.html, practice.html, homework.html}
10class/prof/lesson1/{lection.html, practice.html, homework.html}
11class/base/lesson1/{lection.html, practice.html, homework.html}
11class/prof/lesson1/{lection.html, practice.html, homework.html}
ege/task1/{type1.html, type2.html}
ege/task2/type1.html

Все страницы lection.html, practice.html, homework.html и type*.html намеренно пустые:
внутри body нет ни заданий, ни текстов — можно вписывать свои материалы.
Каждая страница уже подключает ../../styles.css по корректному относительному пути.

На главной страницы собраны ровно те уроки и названия разделов,
которые указаны в четырёх предоставленных таблицах КТП. Повторяющиеся
темы не удалялись: это отдельные уроки со своими папками.

ЕГЭ: созданы только task1 и task2 с теми типами файлов, которые показаны на скриншоте,
поскольку названия или перечень других типов заданий не были предоставлены.
Для нового типа создайте ege/taskN/typeM.html и добавьте его в data.js.
