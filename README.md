### Hexlet tests and linter status:
<a href="https://codeclimate.com/github/MarfaNikitina/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a5b198ab73245bf35f42/test_coverage" /></a>
<a href="https://codeclimate.com/github/MarfaNikitina/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/a5b198ab73245bf35f42/maintainability" /></a>
[![linter check](https://github.com/MarfaNikitina/python-project-lvl2/actions/workflows/hexlet-lint.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl2/actions/workflows/hexlet-lint.yml)
[![Actions Status](https://github.com/MarfaNikitina/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl2/actions)
[![Pytest check](https://github.com/MarfaNikitina/python-project-lvl2/actions/workflows/hexlet-pytest.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl2/actions/workflows/hexlet-pytest.yml)


Проект "Вычислитель отличий"

В данном проекте представленна программа, вычисляющая различия между двумя файлами в форматах json или yml.
С помощью парсера, программа принимает на вход два файла и аргумент --format, позволяющий выбирать один из трех форматов вывода различий. 
В программе реализованы три форматтера:

1)stylish (форматтер по умолчанию)

Пример работы форматтера:

[![asciicast](https://asciinema.org/a/Q4dNcTWsPZr5IcHt8vGJZgI0w.svg)](https://asciinema.org/a/Q4dNcTWsPZr5IcHt8vGJZgI0w)


2)plain(текстовый вывод с описанием различий)

Пример работы форматтера:

[![asciicast](https://asciinema.org/a/ofHXQfLBwaNRDPrIF9Oh29DF3.svg)](https://asciinema.org/a/ofHXQfLBwaNRDPrIF9Oh29DF3)


3)json(выводит отличия в json-подобном виде)

Пример работы форматтера:

[![asciicast](https://asciinema.org/a/Jk5yYuz3zThAhNG3N7aQ3s6vu.svg)](https://asciinema.org/a/Jk5yYuz3zThAhNG3N7aQ3s6vu)


Пример вывода справки -h:
[![asciicast](https://asciinema.org/a/LwfEi5O9MP7I4qOrOTZVBxBQd.svg)](https://asciinema.org/a/LwfEi5O9MP7I4qOrOTZVBxBQd)
