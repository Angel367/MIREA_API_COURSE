import requests

api_key = "00550c51ae2251372b0cf97e57a80fac"
print("Введите название города: ")
city = input()
data = requests.get(f"http://api.weatherstack.com/current?"
                    f"access_key={api_key}&"
                    f"query={city}&")
useful_data = data.json()['current']

print(f"Температура: {useful_data['temperature']}°C"
      f"\nВлажность: {useful_data['humidity']}%"
      f"\nДавление: {useful_data['pressure']} мм рт.ст."
      f"\nВетер: {useful_data['wind_speed']} м/с"
      )
