weather = {
    "city": "Москва", 
    "temterature": 20
    }
print(weather["city"])
weather["temterature"] = weather["temterature"] - 5
print(weather)
print(weather.get("country"))
print(weather.get("country", "Россия"))
weather["date"] = "27.05.2019"
print(len(weather))