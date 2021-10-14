# import mockito
# from unittest import TestCase
# import tempfile
# import pytest
# from mockito import when, unstub, verify
# import builtins
# from . import sensor
# from azure.iot.device import IoTHubDeviceClient



# def test_one(self):
#     assert 1 == 1

# def test_setup():
#     # instanciate iotHubDeviceClient
#     def connected():
#         return {"connected": True}
#     when(IoTHubDeviceClient).create_from_connection_string("123").thenReturn({"connect": lambda x: {"connected": True} })
#     device_client = IoTHubDeviceClient.create_from_connection_string("123")
#     print(device_client)
#     # force connection
#     # mocking connect method
#     when(IoTHubDeviceClient).connect().thenReturn(device_client)
#     return device_client

# def test_iot_hub_connection():
    
#     #call function to test
#     prosperity_client = sensor.iot_hub_connection("123")
#     # assert successfull connection
#     assert prosperity_client.connected == True