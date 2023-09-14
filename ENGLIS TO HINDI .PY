# Import the necessary modules
from googletrans import Translator, LANGUAGES
import PySimpleGUI as sg

# Create a Translator object
translator = Translator()

def translate_text():
    # Get the text from the text entry field
    message = values['-IN-']
    
    # Get the selected language from the dropdown
    lang = values['-DROP-']
    
    # Use the translate method for the translation
    translation = translator.translate(message, dest=lang)
    
    # Set the result in the result label
    window['-OUT-'].update(translation.text)

# Define the window layout
layout = [
    [sg.Input(key='-IN-', size=(25, 1))],
    [sg.Drop(values=list(LANGUAGES.keys()), key='-DROP-', size=(25, 1))],
    [sg.Button('Translate', bind_return_key=True)],
    [sg.Output(size=(60, 20), key='-OUT-')]
]

# Create the window
window = sg.Window('Translator', layout)

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'Translate':
        translate_text()

window.close()
