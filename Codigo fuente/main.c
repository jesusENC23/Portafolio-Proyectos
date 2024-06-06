/*
 * dtmffffff.c
 *
 * Created: 22/03/2023 08:20:05 p. m.
 * Author : nombr
 */ 

#include <avr/io.h>
#define F_CPU 1000000UL
#include <util/delay.h>
#include <avr/interrupt.h>

void ini_LCD(void);
void FS_LCD(void);
void DC_LCD(void);
void EMS_LCD(void);
void CD_LCD(void);
void RH_LCD(void);
void E_LCD(void);
void ini_int(void);
unsigned char contador=0;


ISR(INT0_vect){					//subrutina para el vector de interrupcion externa 0
	unsigned char dato;
	dato=PINC;
	contador++;
	if(dato==10){
		dato=dato+0x26;
	}
	else{
		dato=dato+0x30;
	}
	PORTD |= (1<<PD7);
	PORTB = dato;				//mandamos el dato al puerto completo
	E_LCD();
	PORTD &= ~(1<<PD7);
	if(contador==16){
		PORTD &= ~(1<<PD7);
		PORTB = 0xC0;
		E_LCD();
		_delay_ms(1);
	}
	else if(contador==32){
		PORTD &= ~(1<<PD7);
		PORTB = 0x80;
		E_LCD();
		_delay_ms(1);
		CD_LCD();
		contador=0;
	}
}
int main(void){
	// Inicializacion de las entradas y salidas
	DDRB=0xFF;									//Puerto completo como salida
	DDRD=(1<<PD7)|(1<<PD6);										//PD7 y 6 como salida
	DDRD &= ~(1<<PD2);
	DDRC =0x00;
	ini_LCD();
	ini_int();
	unsigned char mensaje[] = "DTMF";				//mensaje a imprimir
	unsigned char i = 0;
	while(mensaje[i]){
		PORTD |= (1<<PD7);
		PORTB = mensaje[i];				//mandamos el dato al puerto completo
		E_LCD();
		i++;
		PORTD &= ~(1<<PD7);
	}
	_delay_ms(1000);
	CD_LCD();
	sei();
	while(1);
}
void ini_LCD(void){
	PORTB = 0x30;
	E_LCD();
	PORTB = 0x30;
	E_LCD();
	PORTB = 0x30;
	E_LCD();
	FS_LCD();
	DC_LCD();
	EMS_LCD();
	CD_LCD();
	RH_LCD();
}
void FS_LCD(void){
	PORTB = 0x38;
	E_LCD();
}
void DC_LCD(void){
	PORTB = 0x0C;
	E_LCD();
}
void EMS_LCD(void){
	PORTB = 0x06;
	E_LCD();
}
void CD_LCD(void){
	PORTB = 0x01;
	E_LCD();
}
void RH_LCD(void){
	PORTB = 0x02;
	E_LCD();
}
void E_LCD(void){
	_delay_ms(1);
	PORTD |= (1<<PD6);
	_delay_ms(1);
	PORTD &= ~(1<<PD6);
	_delay_ms(1);
}
void posf1_LCD(void){
	PORTB = 0x80;
	E_LCD();
	_delay_ms(2);
}
void ini_int(void){
	EICRA = (1<<ISC01)|(1<<ISC00); //interrupcion por flanco de subida de la int0
	EIMSK |= (1<<INT0);
}