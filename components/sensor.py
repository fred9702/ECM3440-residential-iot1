import time
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
from counterfit_connection import CounterFitConnection


adc = ADC()
relay = GroveRelay(5)

def counterfit_connection():
    CounterFitConnection.init('127.0.0.1', 5000)

def iot_hub_connection(connection_string): 
    device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

    print('Connecting')
    print(device_client + "test version")
    device_client.connect()
    print('Connected')
    return device_client


def handle_method_request(request):
    print("Direct method received - ", request.name)

    if request.name == "relay_on":
        relay.on()
    elif request.name == "relay_off":
        relay.off()

    method_response = MethodResponse.create_from_method_request(request, 200)
    device_client.send_method_response(method_response)

def read_adc():
        soil_moisture = adc.read(0)
        print("Soil moisture:", soil_moisture)

        message = Message(json.dumps({'soil_moisture': soil_moisture}))
        device_client.send_message(message)

def main(): 
    device_client.on_method_request_received = handle_method_request
    while True:
        read_adc()
        time.sleep(10)

if __name__ == "__main__":
    counterfit_connection()
    connection_string = 'HostName=anyaiothub.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=QRoksSHbOVbgt0BHz+xJdyzrMqsq1ht8n/Y8pif8mvs='
    device_client = iot_hub_connection(connection_string)
    main()