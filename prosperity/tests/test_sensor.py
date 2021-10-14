from ..components import sensor

from unittest.mock import patch
from azure.iot.device import IoTHubDeviceClient

@patch.object(IoTHubDeviceClient, 'create_from_connection_string')
@patch.object(IoTHubDeviceClient, 'connect')
def test_succesful_iot_hub_connection(connect, create_from_connection_string):
    #  mock connection string 
    create_from_connection_string.return_value = IoTHubDeviceClient
    connect.return_value = IoTHubDeviceClient

    client = sensor.iot_hub_connection()
    print(f'Connected: {client.connected}')
    assert client is IoTHubDeviceClient

# # import mockito
# # from unittest import TestCase
# # import tempfile
# # import pytest
# # from mockito import when, unstub, verify
# # import builtins
# # from . import sensor
# # from azure.iot.device import IoTHubDeviceClient



# # def test_one(self):
# #     assert 1 == 1

# # def test_setup():
# #     # instanciate iotHubDeviceClient
# #     def connected():
# #         return {"connected": True}
# #     when(IoTHubDeviceClient).create_from_connection_string("123").thenReturn({"connect": lambda x: {"connected": True} })
# #     device_client = IoTHubDeviceClient.create_from_connection_string("123")
# #     print(device_client)
# #     # force connection
# #     # mocking connect method
# #     when(IoTHubDeviceClient).connect().thenReturn(device_client)
# #     return device_client

# # def test_iot_hub_connection():
    
# #     #call function to test
# #     prosperity_client = sensor.iot_hub_connection("123")
# #     # assert successfull connection
# #     assert prosperity_client.connected == True