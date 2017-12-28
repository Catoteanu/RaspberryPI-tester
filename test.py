#!/usr/bin/python

from gpiozero import LED, Button 	#import din libratie gpiozero obiecte LED si Button
from time import sleep				#import din librarie time functie sleep

b1=Button(3)			# definire buton de control b1 pe pin 3
b2=Button(17)			# definire buton de control b2 pe pin 17
gb2=LED(27)				# definire led verde gb2 pe pin 27
rb2=LED(22)				# definire led rosu rb2 pe pin 22
b3=Button(10)			# definire buton de control b3 pe pin 10
gb3=LED(9)				# definire led verde gb3 pe pin 9
rb3=LED(8)				# definire led rosu rb3 pe pin 8
b4=Button(5)			# definire buton de control b4 pe pin 5
gb4=LED(6)				# definire led verde gb4 pe pin 6
rb4=LED(13)				# definire led rosu rb4 pe pin 13

sleep(5)				# definire timp de intarziere de 5 secunde

while True:				# declaratie de executie a buclei atata timp cat condititiile urmatoare sunt adevarate
	if b1.is_pressed:				# declaratia 1 daca butonul de control b1 este presat si intrat in starea logic 1
		if b2.is_pressed:			# declaratia 2 daca butonul de control b2 este presat si intrat in starea logic 1
				gb2.on()			# declaratia de setarea a ledului gb.2 pe starea logic 1
				rb2.off()			# declaratia de setarea a ledului rb.2 pe starea logic 0
		else:						# declaratia 3 daca butonul de control b2 nu este presat si este intrat in starea logic 0
				gb2.off()			# declaratia de setarea a ledului gb2 pe starea logic 0
				rb2.on()			# declaratia de setarea a ledului gb2 pe starea logic 1
		if b3.is_pressed:			# declaratia 4 daca butonul de control b3 este presat si intrat in starea logic 1
				gb3.on()			# declaratia de setarea a ledului gb.3 pe starea logic 1
				rb3.off()			# declaratia de setarea a ledului rb.3 pe starea logic 0
		else:						# declaratia 5 daca butonul de control b3 nu este presat si este intrat in starea logic 0
				gb3.off()			# declaratia de setarea a ledului gb3 pe starea logic 0
				rb3.on()			# declaratia de setarea a ledului gb3 pe starea logic 1
		if b4.is_pressed:			# declaratia 6 daca butonul de control b4 este presat si intrat in starea logic 1
				gb4.on()			# declaratia de setarea a ledului gb.4 pe starea logic 1
				rb4.off()			# declaratia de setarea a ledului rb.4 pe starea logic 0
		else:						# declaratia 7 daca butonul de control b4 nu este presat si este intrat in starea logic 0
				gb4.off()			# declaratia de setarea a ledului gb4 pe starea logic 0
				rb4.on()			# declaratia de setarea a ledului gb4 pe starea logic 1
	else:							# declaratia 8 daca butonul de control b1 nu este presat si este intrat in starea logic 0
		gb2.off()					# declaratia de setarea a ledului gb2 pe starea logic 0
		gb3.off()					# declaratia de setarea a ledului gb3 pe starea logic 0
		gb4.off()					# declaratia de setarea a ledului gb3 pe starea logic 0
		rb2.off()					# declaratia de setarea a ledului rb2 pe starea logic 0
		rb3.off()					# declaratia de setarea a ledului rb3 pe starea logic 0
		rb4.off()					# declaratia de setarea a ledului rb4 pe starea logic 0
		
if b1.is_pressed and b2.is_pressed and b3.is_pressed and b4.is_pressed:		# declaratia 9 daca b1 si b2 si b3 si b4 sunt presate si setate pe logic 1
		import serial														# import libraria serial

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)			# definire port serial cu caracteristicile de setare / cale/viteza de transmitere/timp

while True:									# declaratie de executie a buclei atata timp cat condititiile urmatoare sunt adevarate
    port.write("\r\n<K200,A>") 		# declaratia de transmitere a codului de triger pentru scanerul hardware conectat pe portul serial ttyUSB0
    rcv = port.read(30)						# declaratia de citire a codului de 30 de biti receptionat de la scanarul conectat pe portul serial ttyUSB0
	
	import MySQLdb										# import libraria mysqldb
conn = MySQLdb.connect(host= "localhost",				# declaratia conexiune cu server-ul mysql, cu parametri host - user - parola - numele bazei de date
                  user="operator",
                  passwd="secret",
                  db="database_name")
x = conn.cursor()							# declaratie de definire a clasei cursor

try:					# declaratie de executie
			# declararea de executare a comenzii sql de inserarea a rcv = codul matriceal citit pe portul serial, si a confirmarii 'PASS' a unitatii testate, 
			# in baza de date aferenta in coloana ID_unit si coloana de status
   x.execute("""INSERT INTO TABLE_test_screw (ID_unit, status) VALUES (%s,%s)""",(rcv,'PASS'))
   conn.commit()			# declaratie de executare
except:						# declaratie pentru tratarea exceptie la eroare	
   conn.rollback()			# declaratie de returnare la valorile initiale a executiei de INSERT in caz de erori

conn.close()				# declaratie de inchidere a conexiunii cu serverul mysql

	import gc 				# import libraria gc
gc.collect()				# declaratie de executie a comenzii de verificare a vechilor conexiuni mysql si a inchiderii lor daca nu au fost inchise din diverse erori



	
	