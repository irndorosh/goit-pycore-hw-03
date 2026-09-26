# ДЗ3 — NYC TLC Yellow Taxi Trip Records

**Назва датасету:** NYC TLC Yellow Taxi Trip Records

**Посилання на офіційне джерело:** https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

**Файл даних:** офіційний місячний Parquet-файл за січень 2024 — `yellow_tripdata_2024-01.parquet`, завантажений напряму з CloudFront, на який посилається сторінка TLC:
`https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet`

**Спосіб формування вибірки:** з місячного Parquet-файлу відібрано лише 11 потрібних колонок (`VendorID`, `tpep_pickup_datetime`, `tpep_dropoff_datetime`, `passenger_count`, `trip_distance`, `PULocationID`, `DOLocationID`, `payment_type`, `fare_amount`, `tip_amount`, `total_amount`), після чого взято перші 100 000 рядків файлу (`.head(100_000)`) і збережено у CSV для подальшого завантаження через `COPY FROM STDIN`.

**Кількість рядків:**
- у вихідному CSV / `staging`-таблиці: **100 000**
- у фінальній типізованій таблиці `hw3_taxi_trips` після очищення: **99 999** (1 рядок відфільтровано правилом валідації із Завдання 2)

## Як запустити

1. Відкрити `rdb_hw_03.ipynb` у Google Colab.
2. Виконати `Restart & Run All`.
3. Перша комірка встановлює й запускає PostgreSQL 16 (через `apt-get`, з fallback на випадок, якщо `pgserver` недоступний для середовища), решта — завантажує Parquet, будує staging/clean-таблиці, виконує аудит якості даних, розподіли, outlier-check і 10 DQL/EDA-запитів.

## Структура таблиць (префікс `hw3_`)

- `hw3_taxi_staging` — сирі дані, усі колонки `TEXT`.
- `hw3_taxi_trips` — типізована фінальна таблиця з `PRIMARY KEY`, `NOT NULL`, `CHECK`-обмеженнями.
