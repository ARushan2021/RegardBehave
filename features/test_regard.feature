#Укажем что это за фича
Feature: First test
#Укажем имя сценария (в одной фиче может быть несколько)
  Scenario Outline: Seach in regard.ru

#И используем наши шаги.
    Given open website http://regard.ru
    When open subsection <section> and subsection <sub_section>
    When put the filter on min price: <min_price> and company: <company>
    When assert count products on the page
    When the first product found in the search
    When assert count products on the page 2
    When assert first seach product

    Examples: Electronics
      | section   | sub_section |min_price|company|
      | Периферия | Мониторы    |1000     |Samsung|
      | Периферия | Мыши        |400      |A4Tech |
      | Комплектующие для ПК | Видеокарты        |5000      |ASUS |






