#import app
import unittest
import tempfile
import pytest
from mockito import when, unstub, verify
import builtins

def test_one():
    assert 1 == 1

def test_mock():
    when(myimport).ADC().thenReturn("")