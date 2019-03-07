#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sarmata.sarmata_client import validate_recognition_settings, create_audio_stream, print_results
from sarmata.service.sarmata_settings import SarmataSettings
from sarmata.service.sarmata_recognize import SarmataRecognizer
from address_provider import AddressProvider
from os.path import join as opjoin
import sys
import SarmataArgs
import winsound

if __name__ == '__main__':
    grammar_file = "grammars/szachyy.abnf"
    args = SarmataArgs.SarmataArgs(wav_filepath=None, grammar=grammar_file)

    settings = SarmataSettings()
    settings.process_args(args)  # load settings from cmd
    if args.grammar is not None:
        settings.load_grammar(args.grammar)

    can_define_grammar = False
    if args.define_grammar:
        if not settings.grammar_name:
            print("Bad usage. Set BOTH grammar_name and grammar file when define grammar is set True.")
            sys.exit(1)
        can_define_grammar = True

    recognizer = SarmataRecognizer(args.address)

    if can_define_grammar:
        define_grammar_response = recognizer.define_grammar(args.grammar_name, settings.grammar)
        if define_grammar_response.ok:
            if args.grammar is None:
                print("Grammar " + args.grammar_name + " removed")
            else:
                print("Grammar " + args.grammar + " defined as " + args.grammar_name)
        else:
            print("Define grammar error: " + define_grammar_response.error)

    # --------------------------
    # recognize section
    # --------------------------
    if args.wave is not None or args.mic:
        validate_recognition_settings(settings)

        with create_audio_stream(args) as stream:
            # generate id
            f_min_dif = open("min_difference.txt")
            min_dif = float(f_min_dif.read())
            f_result = open("result.txt", "w+")
            f_result.write('')
            winsound.PlaySound("ring2.wav", winsound.SND_FILENAME)
            session_id = stream.session_id()
            settings.set_session_id(session_id)
            results = recognizer.recognize(stream, settings)
            [results_speech, results_rr] = print_results(results, stream)
            result = results_speech[results_rr.index(max(results_rr))]
            if len(results_rr) >= 1:
                if results_rr.index(max(results_rr)) == 0:
                    if len(results_rr) >= 2:
                        if max(results_rr) - results_rr[1] <= min_dif:
                            result = "repeat"
                    if len(results_rr) >= 3:
                        if max(results_rr) - results_rr[2] <= min_dif:
                            result = "repeat"
            if len(results_rr) >= 2:
                if results_rr.index(max(results_rr)) == 1:
                    if max(results_rr) - results_rr[0] <= min_dif:
                        result = "repeat"
                    if len(results_rr) >= 3:
                        if max(results_rr) - results_rr[2] <= min_dif:
                            result = "repeat"
            if len(results_rr) >= 3:
                if results_rr.index(max(results_rr)) == 2:
                    if max(results_rr) - results_rr[1] <= min_dif or max(results_rr) - results_rr[0] <= min_dif:
                        result = "repeat"
            f_result.write(result)
            f_result.close()
            print(result)
