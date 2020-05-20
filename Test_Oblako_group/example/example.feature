Feature: Checking search
@fixture.browser.chrome
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given website "http://qa-assignment.oblakogroup.ru/board/:idhaykeminyan#", '200'
  Then page include text 'Задачи','Семья','Новая задача'
  Then push button with text 'Ок'