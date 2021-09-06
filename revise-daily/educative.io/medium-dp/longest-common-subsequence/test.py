import time
import requests

def devices(query, threshold, date):

    params = {}
    params["status"] = query
    for page_no in range(5):
        params["page"] = page_no
        r = requests.get(url="https://jsonmock.hackerrank.com/api/iot_devices/search", params=params)

        data = r.json()
        time_from, time_until = get_time_range(date)
        print(time_from, time_until)

        results = []
        for device_info in data["data"]:
            if int(device_info["timestamp"]) >= int(time_from) and int(device_info["timestamp"]) <= int(time_until):
                print(device_info)
                results.append(device_info)

    return len(results)


def get_time_range(date):
    month_year = date.split("-")

    date_time = f'01.{month_year[0]}.{month_year[1]} 0:0:0'
    pattern = '%d.%m.%Y %H:%M:%S'
    time_from = int(time.mktime(time.strptime(date_time, pattern)))
    time_until = time_from + 2592000
    return time_from*1000, time_until*1000


if __name__=="__main__":
    devices("STOP", 23, "04-2019")

