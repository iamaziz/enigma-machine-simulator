# CREDIT: generated by GPT-4
import streamlit as st
from enigma_machine import EnigmaMachine  # Assuming the EnigmaMachine class is in enigma_machine.py

# style - hide footer and menu
style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """
st.markdown(style, unsafe_allow_html=True)

# Set up the web app's title and introductory text.
st.title("Enigma Machine Simulator")
st.write("""
This app simulates a very simplified version of the historical Enigma machine.
Set the initial rotor settings and input a message to see the encoded results.
""")

# Create columns for the rotor settings so they can be side by side.
col1, col2, col3 = st.columns(3)  # Use the newer 'columns' layout

# Create a number input (a counter) for each rotor in each column.
# These will ensure users can only input numbers, and we limit them to valid rotor positions (0-25).
rotor1 = col1.number_input("Rotor 1 Setting", min_value=0, max_value=25, value=0)
rotor2 = col2.number_input("Rotor 2 Setting", min_value=0, max_value=25, value=0)
rotor3 = col3.number_input("Rotor 3 Setting", min_value=0, max_value=25, value=0)

# User input for the message to encode.
message = st.text_area("Message to encode:", value="Hello, World!", height=100)

# The message is encoded as soon as the user types, based on the current settings.
if message:  # Check if the message is not empty.
    # Initialize the Enigma machine with the given settings.
    enigma = EnigmaMachine([rotor1, rotor2, rotor3])
    encoded_message = enigma.encode_message(message)

    # Display the encoded message in a code box for easy copying.
    st.caption("Encoded Message")
    st.write(encoded_message)  # This will display the message in a more readable format (without the code box

# Instructions to run remain the same. Users can execute 'streamlit run app.py' in the terminal.


# enigma description
with st.expander("Enigma Machine Description"):
    """
## How the Enigma Machine Works

The Enigma machine, developed in the early 20th century, was used primarily by the Germans during World War II for encrypting communications. This electro-mechanical apparatus allowed an operator to type in a message and scramble it, so it appeared as a completely different set of characters, according to the machine's current configuration.

### Basic Principles

1. **Rotors**: The machine had a series of rotors (three in our simulation, although the original had more options). Each rotor was a disc with the 26 letters of the alphabet arranged around it, and it could be set to a starting position. As each letter was typed, the rotors would move, altering the electrical circuit and hence the resulting letter.

2. **Scrambling**: When a key was pressed, the electrical signal would go through the rotors, and each rotor would change the signal's path. This meant that even if the same letter was typed twice in a row, it could be encoded differently each time, depending on the machine's configuration and the rotors' movement.

3. **Reflector**: After passing through the rotors, the signal reached a "reflector," sending it back through the rotors again, providing another layer of scrambling.

4. **Decoding**: The process was reversible. If the receiving party had an Enigma machine and knew the original settings, they could type the coded message and see the plain text.

In our simplified simulator, we capture the essence of the rotor mechanism. You can set initial positions for each rotor and type messages to see how they would be encoded. For educational purposes and simplicity, our model doesn't simulate all the historical machine's complexities, like the plugboard or different rotor wirings.

> Source _GPT-4_
"""