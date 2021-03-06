import gc
import machine

from wifi import wifi_connect
from api import api_send
from logs import logs_error
from measures import Measures
from settings import WIFI_SSID, WIFI_PASSWORD, COUNT_FOR_AVERAGE, SENDING_DELTA


wdt = machine.WDT(timeout=180000)

try:
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)
    while True:
        measures = Measures(COUNT_FOR_AVERAGE, SENDING_DELTA)
        data = measures.get_averaged_measures()
        del(measures)
        gc.collect()
        api_send(data)
        wdt.feed()
        gc.collect()
except Exception as e:
    logs_error(str(e))
