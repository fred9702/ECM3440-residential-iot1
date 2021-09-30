#import app
import unittest
import tempfile
import pytest
from mockito import when, unstub, verify
import builtins
from module.AzureIoTClient import AzureIoTClient

def test_one():
    assert 1 == 1

def test_mock():
    when(myimport).ADC().thenReturn("")

def test_connection():
    #assert connection works
    #AzureIoTClient.connect() does not return None
    connection_string = "connects"

    when(AzureIOTClient().connect()).thenReturn('AzureIoTClient')
    verify(builtins).print("Connected")
    assert AzureIoTClient(connection_string).connect() is not None