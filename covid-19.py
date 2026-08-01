import requests
import time
from winotify import Notification

def get_covid_data():
    url = "https://disease.sh/v3/covid-19/all"
    r = requests.get(url)
    data = r.json()

    return data

def show_notification(data):
    toast = Notification(
        app_id="COVID Tracker",
        title="COVID-19 Global Update",
        msg=(
            f"Cases: {data['cases']}\n"
            f"Deaths: {data['deaths']}\n"
            f"Recovered: {data['recovered']}"
        ),
        duration="short"
    )

    toast.show()

def run():
    while True:
        try:
            data = get_covid_data()
            show_notification(data)

        except Exception as e:
            print("Error:", e)

        time.sleep(3600)  # ⏰ 60 minutes

run()