import requests
import pandas as pd

city=["Kolkata","Delhi","Mumbai","Chennai","Bengaluru","Patna","Ranchi"]
api_key="REPLACE_WITH_YOUR_API_KEY"

data_fresh=[]

for i in city:
  temp={}
  url=f"https://api.openweathermap.org/data/2.5/weather?q={i}&appid={api_key}&units=metric"

  response=requests.get(url)
  data=response.json()

  temp["city"]=i
  temp["weather_main"]=data["weather"][0]["main"]
  temp["weather_description"]=data["weather"][0]["description"]
  temp["temp(degree C)"]=data["main"]["temp"]
  temp["temp_min(degree C)"]=data["main"]["temp_min"]
  temp["temp_max(degree C)"]=data["main"]["temp_max"]
  temp["pressure(hPa)"]=data["main"]["pressure"]
  temp["humidity(%)"]=data["main"]["humidity"]
  temp["wind_speed(meter/sec)"]=data["wind"]["speed"]
  temp["country"]=data["sys"]["country"]
  data_fresh.append(temp)
  temp={}

df=pd.DataFrame(data_fresh)
pd.set_option("display.max_columns",None)
df.to_csv(r"C:\Users\risha\Desktop\weather_data.csv", index=False)
print("Weather data saved to weather_data.csv")