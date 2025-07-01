# Behance Image Downloader

Скрипт на Python для автоматического скачивания изображений из проектов Behance в высоком разрешении с категоризацией по типу проекта.

---

## Описание

Этот скрипт:

- Запрашивает у пользователя ссылку на проект Behance.
- Определяет категорию проекта по ключевым словам в названии (corporate, ecommerce, mobile).
- Загружает страницу проекта в браузере Chrome в режиме headless.
- Находит все релевантные изображения проекта.
- Скачивает их в папку `downloads` с подкаталогами `corporate`, `ecommerce` или `mobile` в зависимости от категории.
- Именует файлы по шаблону `<название_проекта>_image_<номер>.<расширение>`.

---

## Требования

- Python 3.7 и выше
- [Selenium](https://selenium-python.readthedocs.io/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (версия должна соответствовать установленному Chrome)
- Библиотека requests

Установка зависимостей:

```bash
pip install selenium requests
