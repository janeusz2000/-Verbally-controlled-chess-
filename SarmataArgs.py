from sarmata.sarmata_client import validate_recognition_settings, create_audio_stream, print_results
from sarmata.service.sarmata_settings import SarmataSettings
from sarmata.service.sarmata_recognize import SarmataRecognizer
from address_provider import AddressProvider
from os.path import join as opjoin
import sys


class SarmataArgs:
    address = None                      # IP address and port (address:port) of a service the client will connect to.
    define_grammar = False              # Defines a new grammar to be cached by the service under ID given by `--grammar-name` option from data given by `--grammar` option.
    grammar_name = ''                   # Name (ID) of the grammar in the service's grammar cache.
    grammar = None                      # SRGS grammar file (ABNF or XML format accepted).
    max_alternatives = 3                # Maximum number of recognition hypotheses to be returned.
    mic = True                       # Use microphone as an audio source (instead of wave file).
    no_input_timeout = 2000             # MRCP v2 no input timeout [ms].
    no_match_threshold = 0.2            # Confidence acceptance threshold.
    recognition_timeout = 6000         # MRCP v2 recognition timeout [ms].
    session_id = None                   # Session ID to be passed to the service. If not specified, the service will generate a default session ID itself.
    service_settings = None             # Semicolon-separated list of key=value pairs defining settings to be sent to service via gRPC request.
    speech_complete_timeout = 500      # MRCP v2 speech complete timeout [ms].
    speech_incomplete_timeout = 1000    # MRCP v2 speech incomplete timeout [ms].
    wave = None                         # Path to wave file with speech to be recognized. Should be mono, 8kHz or 16kHz.
    result = ''

    def __init__(self, wav_filepath=None, grammar=None):
        ap = AddressProvider()
        if grammar:
            self.grammar = grammar
        if wav_filepath:
            self.wave = opjoin(wav_filepath)
        self.address = ap.get("sarmata")
