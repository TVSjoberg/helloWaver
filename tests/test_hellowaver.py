from hellowaver import *

def test_wave_once():
    a = HelloWaver('a')
    assert a.ask_to_wave()

def test_wave_twice():
    b = HelloWaver('b')
    b.ask_to_wave()
    assert not b.ask_to_wave()
