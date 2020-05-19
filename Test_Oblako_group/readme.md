# Тестовое задание сайта https://qa-assignment.tumblr.com/
# Автоматическое тестирование 
Ресурсы для изучения:  
    1. [Документация behave](https://behave.readthedocs.io/en/latest/)  
    2. [Selenium cheat sheet](http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/)  
    3. [Установка docker](https://docs.docker.com/engine/install/ubuntu/)  
    4. [Установка docker-compose](https://docs.docker.com/compose/install/)  
    5. [Что такое доккер](https://proglib.io/p/docker/)  

## Что нужно сделать:

    - Проанализировать тест-кейсы, полученные в первой части
    - Выявить кейсы, которые подходят под автоматизацию
    - Загрузить тестовый проект (https://gitlab.com/oblakogroup-public/qa-assignment-template)
    - Настроить среду разработки, установить python, selenium и behave
    - Реализовать автоматизацию тест кейсов, полученных в п.2.
    - Предоставить результат в виде проекта с реализованными тестами.

## Условия:

    - Проект должен запускаться при помощи docker
    - Проект должен храниться на гите

## Результаты необходимо высылать на почту qa-assignment@oblakogroup.ru с темой письма “QA-2 Alexey Ivanov”,  в теле письма также нужно указать адрес страницы, на которой производили тестирование.


## Тестировался сайт http://qa-assignment.oblakogroup.ru/board/:idhaykeminyan#
## Запуск докера при помощи:
1. sudo docker build -t my-python-app .
2. sudo docker run my-python-app python3 /test.py


### P.S было выяснено при автоматическом тестировании, что объёмные текстовые заметки выходят за рамки окна.
<!-- ![Image description]('file:///home/haykeminyan/%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8/Screenshot(15).png') -->