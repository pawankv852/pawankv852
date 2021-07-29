from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins_data=[D4,D5,D6,D7]
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=20, rows=4, pin_rs=1, pin_e=7, pins_data=[8,25,24,23], pin_backlight=18)

lcd.cursor_pos = (1,0)
lcd.write_string("Hello Human :)")
#lcd.clear()

while True:
 time.sleep(2)
 lcd.backlight_enabled = False
 #lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))   
 #lcd.cursor_pos = (1, 0)
 #lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))
 #lcd.write_string(u'Hello Human :)')
 time.sleep(2)
 lcd.backlight_enabled = True
