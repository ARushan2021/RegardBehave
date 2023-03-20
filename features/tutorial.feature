

#Укажем что это за фича
Feature: First test
#Укажем имя сценария (в одной фиче может быть несколько)
  Scenario: Open site
#И используем наши шаги.
    Given open website http://regard.ru
    When open subsection Периферия and subsection Мониторы
    When put the filter on min price: 10000 and company: Huawei
