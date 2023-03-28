Feature: Тестирование regard.ru

  Scenario Outline: Поиск товаров на сайте

    Given открываем сайт "http://regard.ru"
    When открываем каталог <section> и <sub_section>
    When устанавливаем фильтр цена: <min_max_price> значение цены: <price> и производитель: <company>
    When проверяем кол.во найденных товаров на странице
    When копируем название первого товара и вставляем его в строку поиска
    When снова проверяем кол.во найденных товаров на странице
    When проверяем, что найденный товар соответствует товару, вставленному в строку поиска

    Examples: Поиск товара на regard.ru
      | section              | sub_section | min_max_price | price | company |
      | Периферия            | Мониторы    | max           | 25000 | Samsung |
      | Периферия            | Мыши        | min           | 400   | A4Tech  |
      | Комплектующие для ПК | Видеокарты  | max           | 50000 | ASUS    |


  # behave -запуск теста behave
  # behave -f allure_behave.formatter:AllureFormatter -o reports/ features  -формирование reports в json
  # allure serve reports/  -формирование reports в html

  # Использованные библиотеки:
  # Selenium 4.8.2
  # behave 1.2.6
  # allure-behave 2.13.1
  # allure 2.21.0





