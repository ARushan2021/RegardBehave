#Укажем что это за фича
Feature: First test
#Укажем имя сценария (в одной фиче может быть несколько)
  Scenario Outline: Seach in regard.ru

#И используем наши шаги.
    Given открываем сайт http://regard.ru
    When открываем каталог, в каталоге <section> и <sub_section>
    When устанавливаем фильтр минимальная цена: <min_price> и производитель: <company>
    When проверяем кол.во найденных товаров на странице
    When копируем название первого товара и вставляем его в строку поиска
    When снова проверяем кол.во найденных товаров на странице
    When проверяем, что найденный товар соответствует, товару вставили встроку поиска

    Examples: Electronics
      | section   | sub_section |min_price|company|
      | Периферия | Мониторы    |1000     |Samsung|
      | Периферия | Мыши        |400      |A4Tech |
      | Комплектующие для ПК | Видеокарты        |50000000      |ASUS |


  # behave -i test_regard.feature  -запуск теста behave
  # behave -f allure_behave.formatter:AllureFormatter -o reports/ features  -формирование reports в json
  # allure serve reports/  -формирование reports в html

  # Использованные библиотеки:
  # Selenium 4.8.2
  # behave 1.2.6
  # allure-behave 2.13.1
  # allure 2.21.0





