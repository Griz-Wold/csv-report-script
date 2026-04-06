# CSV Report Script

Скрипт для обработки CSV-файлов с данными студентов и формирования отчета.

## Возможности

- Обработка одного или нескольких CSV-файлов
- Поддержка отчета "median-coffee"
- Вывод результата в консоль в виде таблицы

![Run example](https://github.com/Griz-Wold/csv-report-script/blob/main/screenshots/run_example.png)

## Технологии

- Python
- argparse
- csv
- statistics
- tabulate
- pytest

![Pytest result](https://github.com/Griz-Wold/csv-report-script/blob/main/screenshots/pytest_result.png)

## Использование

```bash
python main.py --files file1.csv file2.csv --report median-coffee
