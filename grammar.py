import speech_recognition as sr

# Collect audio sample
r = sr.Recognizer()
captcha_a = sr.AudioFile('myfile.wav')
with captcha_a as source:
    audio = r.record(source)

# Attempt to convert the speech to text
try:
    print(r.recognize_sphinx(audio, grammar='letters.gram'))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
	
	
# Dependencies
import speech_recognition as sr
import os
import pocketsphinx as ps

# Manually point to the grammar file
grammar = 'letters.gram'
try:
    # Point to the model files
    language_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pocketsphinx-data", "en-US")
    acoustic_parameters_directory = os.path.join(language_directory, "acoustic-model")
    language_model_file = os.path.join(language_directory, "language-model.lm.bin")
    phoneme_dictionary_file = os.path.join(language_directory, "pronounciation-dictionary.dict")

    # Create a decoder object with our custom parameters
    config = ps.Decoder.default_config()
    config.set_string("-hmm",
                      acoustic_parameters_directory)  # set the path of the hidden Markov model (HMM) parameter files
    config.set_string("-lm", language_model_file)
    config.set_string("-dict", phoneme_dictionary_file)
    config.set_string("-logfn", os.devnull)  # <--- Prevents you from seeing the actual bug!!!
    decoder = ps.Decoder(config)

    # Convert grammar
    grammar_path = os.path.abspath(os.path.dirname(grammar))
    grammar_name = os.path.splitext(os.path.basename(grammar))[0]
    fsg_path = "{0}/{1}.fsg".format(grammar_path, grammar_name)
    if not os.path.exists(fsg_path):  # create FSG grammar if not available
        jsgf = ps.Jsgf(grammar)
        rule = jsgf.get_rule("{0}.{0}".format(grammar_name))
        fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
        fsg.writefile(fsg_path)
        print('Successful JSFG to FSG conversion!!!')

    # Pass the fsg file into the decoder
    decoder.set_fsg(grammar_name, fsg)  # <--- BUG IS HERE!!!

except Exception as e:
    print('Ach no! {0}'.format(e))
finally:
    os.remove('search.fsg')  # Remove again to help prove that the grammar to fsg conversion isn't at fault
