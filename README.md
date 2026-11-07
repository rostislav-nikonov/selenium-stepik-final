# Итоговый проект по Selenium и Python

Тесты учебного магазина Stepik с использованием Page Object. Нужны Python 3.10+ и Google Chrome. Selenium Manager автоматически подбирает ChromeDriver.

Создайте виртуальное окружение:

```shell
python -m venv .venv
```

Активируйте его: в Windows командой `.venv\Scripts\Activate.ps1`, в Linux и macOS командой `source .venv/bin/activate`. Для MSYS Python в Windows путь другой: `.venv/bin/Activate.ps1`.

Установите зависимости и запустите тесты для проверки итогового задания:

```shell
python -m pip install -r requirements.txt
python -m pytest -v --tb=line --language=en -m need_review --headless
```

Все тесты:

```shell
python -m pytest -v --tb=short --language=en --headless
```

Параметр `--headless` запускает Chrome без видимых окон. Каждый тест получает чистый профиль и закрывает браузер после завершения.

Для отдельного Chrome for Testing можно задать переменные окружения `CHROME_BINARY` с путём к браузеру и `CHROMEDRIVER` с путём к драйверу. Если они не заданы, используется установленный Chrome и Selenium Manager.

Версии pytest и Selenium обновлены для совместимости с современными Python и Chrome. Структура Page Object, названия тестов и метка `need_review` соответствуют заданию курса.

Три случая помечены как ожидаемые падения: неверное название товара при `offer7`, ожидание отсутствия сообщения после добавления товара и ожидание исчезновения этого сообщения. Тесты зарегистрированного пользователя создают учебные аккаунты. У магазина нет функции их удаления.
