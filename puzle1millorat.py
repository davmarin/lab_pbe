import sys
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, cols=20, rows=4)

user_text = sys.stdin.read().strip().split("\n")[:4] # Llegir i dividir el text
for i, line in enumerate(user_text): # Escriure les linies al LCD
    lcd.cursor_pos = (i, 0)
    lcd.write_string(line[:20]) #Escriu cada linia truncada a 20 caracters