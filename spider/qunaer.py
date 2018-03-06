import requests


url = "http://hotels.ctrip.com/hotel/441351.html#ctm_ref=hod_hp_hot_dl_n_2_1"

response = requests.get(url)

print(response)