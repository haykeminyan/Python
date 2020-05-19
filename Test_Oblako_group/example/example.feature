#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
@fixture.browser.chrome
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given website "http://qa-assignment.oblakogroup.ru/board/:idhaykeminyan#"
  Then page include text 'Задачи','Семья','Новая задача'
  Then push button with text 'Ок'