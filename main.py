import requests
import time
import matplotlib.pyplot as plt

api_key = "ce8c8c95485e0c07bb277e1172325c78"

print(requests.get(f"http://api.currencylayer.com/list?access_key={api_key}").json()['currencies'])
time.sleep(2)
first_request = requests.get(f"http://api.currencylayer.com/historical?"
                             f"access_key={api_key}&"
                             f"source=USD&"
                             f"currencies=EUR, GBP, JPY&"
                             f"date=2018-02-22")


print(first_request.json())
useful_data = first_request.json()['quotes']

print(f"================================\n"
      f"Доллар к Евро: {useful_data['USDEUR']}\n"
      f"Доллар к Фунту Стерлингу: {useful_data['USDGBP']}\n"
      f"Доллар к Йенам: {useful_data['USDJPY']}\n")


def generate_date():
    from datetime import datetime, timedelta

    start_date = datetime(2016, 2, 25)
    end_date = datetime(2017, 2, 21)

    current_date = start_date
    date_list = []

    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return date_list


course = {}
time.sleep(3)
for date in generate_date():
    second_request = requests.get(f"http://api.currencylayer.com/historical?"
                                  f"access_key={api_key}&"
                                  f"source=USD&"
                                  f"currencies=EUR&"
                                  f"date={str(date)}")
    print(second_request.json())
    time.sleep(1)
    course[date] = second_request.json()['quotes']['USDEUR']

dates = list(course.keys())
values = list(course.values())


plt.figure(figsize=(10, 6))  # Размер графика
plt.plot(dates, values, marker='o', linestyle='-', color='b', markersize=6)  # Построение графика

plt.xlabel('Дата')
plt.ylabel('Значение')
plt.title('График значений по датам')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
