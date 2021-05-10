# BabyJournalBot Async API

Библиотека для работы с [API](https://github.com/katorov/bjb-web) телеграм бота **BabyJournalBot**.


## Возможности

* [Пользователи](#пользователи)
  * [регистрация новых пользователей](#регистрация-новых-пользователей)
  * [генерация и проверка JWT-токенов](#генерация-и-проверка-JWT-токенов)

* [Журнал событий](#Журнал-событий)
  * [просмотр записи или списка записей](#просмотр-записи-или-списка-записей)
  * [добавление записей](#добавление-записей)
  * [изменение записей](#изменение-записей)
  * [удаление записей](#удаление-записей)

## Требования

* Python >= 3.8
* aiohttp>=3.7.4.post0
* requests

## Установка

* Способ №1: через pip
```bash
$ pip install git+https://github.com/katorov/bjb-api
```

* Способ №2: через клонирование репозитория
```bash
$ git clone git@github.com:katorov/bjb-api.git
$ cd bjb-api
$ python setup.py install
```

## Использование

```python
import bjb_api

bjb_api.init_session()
```

## Быстрый туториал

### Пользователи

#### Регистрация новых пользователей

```python
telegram_user_id = 7777777
await bjb_api.auth.User().register(
    username='username',
    password='password',
    first_name='Ivan',
    last_name='Ivanov',
    is_paid=True,
    team=telegram_user_id,
)
```

#### Генерация и проверка JWT-токенов

```python
access_token, refresh_token = await bjb_api.auth.JWT().create(
    username='username', 
    password='password'
)    
await bjb_api.auth.JWT().verify(access_token)
```

### Журнал событий 

Доступны все категории: 
питание, прогулки, сон, туалет, гимнастика, другие события, сводный журнал.

#### Просмотр записи или списка записей

```python
food_records, is_next_page_exist = await bjb_api.journal.FoodRecord(access_token).get_list()
sleep_record = await bjb_api.journal.SleepRecord(access_token).get(record_id=1)
```

#### Добавление записей

```python
import datetime

toilet_data = dict(category=1, dt=datetime.datetime.now())
response = await bjb_api.journal.ToiletRecord(access_token).create(
    category=toilet_data['category'],
    dt=toilet_data['dt'],
)
```

#### Изменение записей

```python
new_other_event_description = 'New description'
response = await bjb_api.journal.OtherEventRecord(access_token).update(
    record_id=1,
    description=new_other_event_description,
)
```
    
#### Удаление записей

```python
await bjb_api.journal.WalkRecord(access_token).delete(record_id=1)
```