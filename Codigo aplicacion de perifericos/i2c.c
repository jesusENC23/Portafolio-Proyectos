#include "I2C.h"

void I2C_init(void){                    //INICALIZACION DEL I2C
     I2C_port();                        //CONFIGURACION DE TERMINALES
     SSPCON |= Master_Mode_Clock;       //MODO MAESTRO CON CONTROL DE CLOCK
     SSPCON.SSPEN = 1;                  //HABILITA MODULO MSSP EN I2C
     SSPADD = SSPADD_Speed;              //VELOCIDAD DEL I2C
     SSPSTAT.SMP = 1;                   //CONTROL DE VELOCIDAD INHABILITADO
}
void I2C_port(void){                    //CONFIGURACION DE TERMINALES
     SCL_Dir = 1;                       //SALIDA DEL CLOCK
     SDA_Dir = 1;                       //ENTRADA SALIDA DE DATOS
}
void I2C_wait(void){
     while(SSPSTAT.R_W | SSPCON2.ACKEN | SSPCON2.RCEN 
         | SSPCON2.PEN | SSPCON2.RSEN | SSPCON2.SEN);
     return;
}
void I2C_start(void){
     SSPCON2.SEN = 1;
     I2C_Wait();
}
void I2C_restart(void){
     SSPCON2.RSEN = 1;
     I2C_Wait();
}
void I2C_stop(void){
     SSPCON2.PEN = 1;
     I2C_Wait();
}
void I2C_write(unsigned char Data){
     SSPBUF = Data;
     I2C_Wait();
}
unsigned char I2C_read(unsigned char Ack){
     unsigned char buffer;
     I2C_Wait();
     SSPCON2.RCEN = 1;
     I2C_Wait();
     
     buffer = SSPBUF;
     I2C_Wait();
     SSPCON2.ACKDT = Ack;
     SSPCON2.ACKEN = 1;
     return buffer;
}
