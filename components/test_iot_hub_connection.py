from . import sensor

from unittest.mock import patch
from azure.iot.device import IoTHubDeviceClient

@patch.object(IoTHubDeviceClient, 'create_from_connection_string')
@patch.object(IoTHubDeviceClient, 'connect')
def test_succesful_iot_hub_connection(connect, create_from_connection_string):
    #  mock connection string 
    create_from_connection_string.return_value = IoTHubDeviceClient
    connect.return_value = {"connected": True}
    assert sensor.iot_hub_connection(123) is IoTHubDeviceClient

