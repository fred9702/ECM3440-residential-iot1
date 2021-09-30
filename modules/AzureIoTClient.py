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
        self.client = self.connect()
        self.ADC = ADC()
        self.relay = GroveRelay(5)

    def connect(connection_string):

        try:
            device_client = IoTHubDeviceClient.create_from_connection_string(self.connection_string)
            print('Connecting')
            device_client.connect()
            print('Connected')
            self.client = device_client
            return self.client
        except Exception:
            raise Exception('Unable to connect...')

    def handle_method_request(self, request):
        print("Direct method received - ", request.name)
        
        if request.name == "relay_on":
            self.relay.on()
        elif request.name == "relay_off":
            self.relay.off()

        method_response = MethodResponse.create_from_method_request(request, 200)
        self.client.send_method_response(method_response)
