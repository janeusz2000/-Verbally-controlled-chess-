#!/usr/bin/env python3
# coding=utf-8

from tribune.call_synthesize import call_synthesize
from address_provider import AddressProvider

if __name__ == '__main__':
    # Config:
    output_wave_file = "test.wav"
    ap = AddressProvider()
    address = ap.get("tribune")
    sampling_rate = 44100
    input_text = "Test."

    call_synthesize(address, input_text, output_wave_file, sampling_rate)
