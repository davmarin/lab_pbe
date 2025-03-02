import sys
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, cols=20, rows=4) # Inicialitza el display
user_text = sys.stdin.read().strip() # Llegeix l'string de l'usuari

lcd.write_string(user_text) # Escriu directament l'string al display LCD