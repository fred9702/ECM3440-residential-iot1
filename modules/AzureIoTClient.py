from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

class AzureIoTClient():

    def __init__(self, connection_string) -> None:
        self.connection_string = connection_string

    def connect(connection_string):

        try:
            device_client = IoTHubDeviceClient.create_from_connection_string(self.connection_string)
            print('Connecting')
            device_client.connect()
            print('Connected')
            return device_client.connect()
        except Exception:
            raise Exception('Unable to connect...')
