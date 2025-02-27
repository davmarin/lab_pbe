import sys
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27, cols=20, rows=4) #Configuracio del LCD

print("Escribe el texto (pulsa Ctrl+D para enviar a la pantalla):") #Llegir multiples linies fins escriure un ctrl+D
user_text = sys.stdin.read().strip()  #Llegir fins fi darxiu EOF i strip() elimina espais extra

lines = user_text.split("\n")  #Dividir per linies i repartirles com lusuari les escriu
formatted_lines = [line[:20] for line in lines]  #Limitar cada linia a 20 caracters

lcd.clear() #Clenea la pantalla

for i, line in enumerate(formatted_lines[:4]): #Mostrar maxim 4 linies a lLCD
    lcd.cursor_pos = (i, 0)
    lcd.write_string(line)

print("Texto mostrado en la pantalla.")
