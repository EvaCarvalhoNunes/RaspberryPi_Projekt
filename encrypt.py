# /home/pi/enigma-venv --> virtual enviroment
# Run the script: python3 /home/pi/Desktop/decrypt.py

from enigma.machine import EnigmaMachine

# Set up the Enigma machine
machine = EnigmaMachine.from_key_sheet(
    rotors='II IV V',
    reflector='B',
    ring_settings='01 01 01',
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
)

# Set the initial position of the Enigma rotors
machine.set_display('FNZ')

# Encrypt the text 'BFR' and store it as msg_key
msg_key = machine.process_text('BFR')
print(f"Encrypted message key: {msg_key}")

# Encrypt a plaintext
plaintext = "RASPBERRYPI"
ciphertext = machine.process_text(plaintext)
print(f"Ciphertext: {ciphertext}")

