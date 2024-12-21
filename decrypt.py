# /home/pi/enigma-venv --> virtual enviroment
# Run the script: python3 /home/pi/Desktop/decrypt.py

from enigma.machine import EnigmaMachine

# Set up the Enigma machine with initial settings
machine = EnigmaMachine.from_key_sheet(
    rotors='II IV V',                # Rotor configuration
    reflector='B',                   # Reflector type
    ring_settings='01 01 01',        # Ring settings
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'  # Plugboard connections
)

# Decrypt the text 'PWE' and store it as msg_key
machine.set_display('AAA')  # Initial rotor positions
msg_key = machine.process_text('PWE')  # Decrypt the message key
print(f"Decrypted message key: {msg_key}")

# Set the new start position of the Enigma rotors to the decrypted message key
machine.set_display(msg_key)

# Decrypt a ciphertext
ciphertext = 'YJPYITREDSYUPIU'  # Example ciphertext
plaintext = machine.process_text(ciphertext)  # Decrypt the ciphertext
print(f"Decrypted plaintext: {plaintext}")

