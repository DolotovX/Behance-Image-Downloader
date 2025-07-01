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


## Обучение и расширение функционала

### Как добавить новую категорию проекта

Чтобы добавить поддержку новой категории проекта (например, "portfolio", "design", "photography" и др.) необходимо:

1. Добавить ключевые слова для категории в список ключевых слов в коде. Например:

```python
portfolio_keywords = ["portfolio", "design", "photography"]
```
2. Добавить проверку наличия этих ключевых слов в названии проекта и указать новую папку для сохранения:
```python
elif any(keyword in project_slug for keyword in portfolio_keywords):
    target_folder = os.path.join("downloads", "portfolio")
```

### Установка зависимостей:

```bash
pip install selenium requests

