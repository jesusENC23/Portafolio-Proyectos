#include "LCD.h"
#include "I2C.h"
#include "TecMatricial.h"

unsigned char Seg   = 0x00;
unsigned char Min   = 0x33;
unsigned char Hour  = 0x00;
unsigned char Day   = 0x03;
unsigned char Date  = 0x5;
unsigned char Month = 0x12;
unsigned char Year  = 0x23;
unsigned char TDay  = 0x00;
unsigned char TeclaP= 0x00;
unsigned int  Temp =  0x00;
unsigned int aux=0x00;


static char LABEL1[]={"           20   \n"};
static char LABEL3[]={"Modificar H o F?\n"};
static char LABEL4[]={"1. Hora 2. Fecha\n"};
static char LABEL5[]={"Tecla no valida \n"};
unsigned char tempvec[5];

void I2C_DS1307W(void);                 //ESCRITURA EN RTC
void I2C_DS1307R(void);                 //LECTURA EN RTC
void Ini_RTC(void);                     //INICIALIZAMOS RTC
void Proceso(unsigned char press);      //MENU DE CAMBIO DE PROCESOS
void MENU_CAMBIO(void);
void CAMBIO_HORA(void);                 //CAMBIO DE HORA
void CAMBIO_FECHA(void);                 //CAMBIO DE FECHA
void PWM_CONF(void);
void PWM_DUTY(int duty_c);
void PWM_T(int periodo);
void VELOCIDAD_MOTOR(void);
void LM75_T(void);
void RS_232INIT(void);
void COM_SERIAL(void);

void main(){
     INI_LCD();
     I2C_init();
     Ini_RTC();
     INI_TM();
     RS_232INIT();
     PWM_CONF();
     PWM_T(256);
     while(1){
          do{
          I2C_DS1307R();
          LM75_T();
          TeclaP = TM_tecla();
          }while(TeclaP==0x00);
          delay_ms(100);
          Proceso(TeclaP);
     }
}
void interrupt(){
     if(PIR1.RCIF){
           CtrlBus|=(1<<RS);
           DataBus=RCREG;
           CtrlBus|=(1<<E);
           delay_ms(2);
           CtrlBus&=~(1<<E);
           delay_ms(2);
           CtrlBus&=~(1<<RS);
           if(RCREG=='*'){
                CtrlBus&=~(1<<RS);
                DataBus=0x01;
                CtrlBus|=(1<<E);
                delay_ms(2);
                CtrlBus&=~(1<<E);
                delay_ms(2);
           }
           delay_ms(300);
     }
}
void COM_SERIAL(void){
     volatile unsigned char AUXLABEL1[]={"Temperatura:\n"};
     char cont=0;
     CLEAR_DISPLAY();
     CtrlBus&=~(1<<RS);
     DataBus=0x80;
     CtrlBus|=(1<<E);
     delay_ms(2);
     CtrlBus&=~(1<<E);
     delay_ms(2);
     do{
          INTCON.GIE = 1;            //Habilitación global de las Interrupciones
          if(TM_POLLING()== '1'){
               cont=0;
               while(AUXLABEL1[cont] !='\n'){
                    TXREG=AUXLABEL1[cont];
                    while(!PIR1.TXIF);
                    while(!PIR1.TXIF);
                    cont++;
               }
               cont=0;
               while(tempvec[cont] !='\n'){
                    TXREG=tempvec[cont];
                    while(!PIR1.TXIF);
                    while(!PIR1.TXIF);
                    cont++;
               }
          }
          else{
          TXREG=TM_POLLING();
          }
     }while(TM_POLLING()!='D');
     INTCON.GIE = 0;
     return;
}
void Proceso(unsigned char press){
     switch(press){
         case 'A': MENU_CAMBIO();       break;
         case 'B': VELOCIDAD_MOTOR();   break;
         case 'C': COM_SERIAL();        break;
     }
}
void LM75_T(void){
     I2C_start();
     I2C_write(LM75_W);
     I2C_write(0x00);
     I2C_restart();
     I2C_write(LM75_R);
     Temp = I2C_read(ACK)<<8;
     Temp |= I2C_read(NACK);
     I2C_stop();
     Temp = (Temp>>5)/8;
     tempvec[0]='T';
     tempvec[1]=((Temp%1000)/100)+'0';
     tempvec[2]=(((Temp%1000)%100)/10)+'0';
     tempvec[3]=(((Temp%1000)%100)%10)+'0';
     tempvec[4]='\n';
     SET_DDRAM_WRITE(0xC9,&tempvec);
}
void VELOCIDAD_MOTOR(){
     volatile unsigned char AUXLABEL1[]={"VELOCIDAD(%):\n"};
     unsigned char digito;
     unsigned int dutycicle;
     CLEAR_DISPLAY();
     SET_DDRAM_WRITE(0x80,&AUXLABEL1);
     digito = TM_POLLING();
     dutycicle = (digito - '0')*100;
     SET_DDRAM_WRITECHAR(0xC0,digito);
     digito = TM_POLLING();
     dutycicle += (digito - '0')*10;
     SET_DDRAM_WRITECHAR(0xC1,digito);
     digito = TM_POLLING();
     dutycicle += digito - '0';
     SET_DDRAM_WRITECHAR(0xC2,digito);
     PWM_DUTY(dutycicle*10);
     delay_ms(500);
     CLEAR_DISPLAY();
}
void MENU_CAMBIO(void){
     SET_DDRAM_WRITE(0x80, &LABEL3);
     SET_DDRAM_WRITE(0xC0, &LABEL4);
     TeclaP = TM_POLLING();
     switch(TeclaP){
         case '1': CAMBIO_HORA();       break;
         case '2': CAMBIO_FECHA();      break;
         default:
             CLEAR_DISPLAY();
             SET_DDRAM_WRITE(0x80, &LABEL5);
             delay_ms(500);
         break;
     }
}
void CAMBIO_HORA(void){                 //CAMBIO DE HORA
    volatile unsigned char AUXLABEL1[]={"HORA:\n"};
    volatile unsigned char AUXLABEL2[]={"MINUTO:\n"};
    volatile unsigned char AUXLABEL3[]={"SEGUNDO:\n"};
    unsigned char digito;
    CLEAR_DISPLAY();
    SET_DDRAM_WRITE(0x80,&AUXLABEL1);
    digito = TM_POLLING();
    Hour = (digito - '0')<<4;
    SET_DDRAM_WRITECHAR(0xC0,digito);
    digito = TM_POLLING();
    Hour |= (digito - '0');
    SET_DDRAM_WRITECHAR(0xC1,digito);
    delay_ms(500);
    CLEAR_DISPLAY();
    SET_DDRAM_WRITE(0x80, &AUXLABEL2);
    digito = TM_POLLING();
    Min = (digito - 0x30)<<4;
    SET_DDRAM_WRITECHAR(0xC0, digito);
    digito = TM_POLLING();
    Min |= (digito - 0x30);
    SET_DDRAM_WRITECHAR(0xC1, digito);
    delay_ms(500);
    CLEAR_DISPLAY();
    SET_DDRAM_WRITE(0x80, &AUXLABEL3);
    digito = TM_POLLING();
    Seg = (digito - '0')<<4;
    SET_DDRAM_WRITECHAR(0xC0, digito);
    digito = TM_POLLING();
    Seg |= (digito - '0');
    SET_DDRAM_WRITECHAR(0xC1, digito);
    delay_ms(500);
    CLEAR_DISPLAY();
    I2C_DS1307W();
}
void CAMBIO_FECHA(void){                //CAMBIO DE FECHA
    volatile unsigned char AUXLABEL1[]={"DIA(S):\n"};
    volatile unsigned char AUXLABEL2[]={"DIA(N):\n"};
    volatile unsigned char AUXLABEL3[]={"MES:\n"};
    volatile unsigned char AUXLABEL4[]={"ANIO:\n"};
    unsigned char digito;
    CLEAR_DISPLAY();
    SET_DDRAM_WRITE(0x80,&AUXLABEL1);
    digito = TM_POLLING();
    Day = (digito - '0')<<4;
    SET_DDRAM_WRITECHAR(0xC0,digito);
    digito = TM_POLLING();
    Day |= (digito - '0');
    SET_DDRAM_WRITECHAR(0xC1,digito);
    delay_ms(500);
    CLEAR_DISPLAY();
    SET_DDRAM_WRITE(0x80, &AUXLABEL2);
    digito = TM_POLLING();
    Date = (digito - 0x30)<<4;
    SET_DDRAM_WRITECHAR(0xC0, digito);
    digito = TM_POLLING();
    Date |= (digito - 0x30);
    SET_DDRAM_WRITECHAR(0xC1, digito);
    delay_ms(500);
    CLEAR_DISPLAY();
    SET_DDRAM_WRITE(0x80, &AUXLABEL3);
    digito = TM_POLLING();
    Month = (digito - '0')<<4;
    SET_DDRAM_WRITECHAR(0xC0, digito);
    digito = TM_POLLING();
    Month |= (digito - '0');
    SET_DDRAM_WRITECHAR(0xC1, digito);
    delay_ms(500);
    CLEAR_DISPLAY();
    SET_DDRAM_WRITE(0x80, &AUXLABEL4);
    digito = TM_POLLING();
    Year = (digito - '0')<<4;
    SET_DDRAM_WRITECHAR(0xC0, digito);
    digito = TM_POLLING();
    Year |= (digito - '0');
    SET_DDRAM_WRITECHAR(0xC1, digito);
    delay_ms(500);
    CLEAR_DISPLAY();
    I2C_DS1307W();
}
void Ini_RTC(void){
    I2C_DS1307W();
}
void I2C_DS1307W(void){                 //ESCRITURA EN RTC
     I2C_start();
     I2C_write(DS1307_W);
     I2C_write(0x00);
     I2C_write(Seg);
     I2C_write(Min);
     I2C_write(Hour);
     I2C_write(Day);
     I2C_write(Date);
     I2C_write(Month);
     I2C_write(Year);
     I2C_stop();
}
void I2C_DS1307R(void){                 //LECTURA EN RTC
     I2C_start();
     I2C_write(DS1307_W);
     I2C_write(0x00);
     I2C_restart();
     I2C_write(DS1307_R);
     Seg   = I2C_read(ACK);
     Min   = I2C_read(ACK);
     Hour  = I2C_read(ACK);
     Day   = I2C_read(ACK);
     Date  = I2C_read(ACK);
     Month = I2C_read(ACK);
     Year  = I2C_read(NACK);
     I2C_stop();
     aux=(Date&0xF0)>>4;
     Label1[4] = (aux&0x0F) + '0';
     aux=Date&0x0F;
     Label1[5]=(aux&0x0F) + '0';
     aux=(Year&0xF0)>>4;
     Label1[13]=(aux&0x0F) + '0';
     aux=Year&0x0F;
     Label1[14]=(aux&0x0F) + '0';
     switch(Day){
          case 1: Label1[0] = 'D'; Label1[1] = 'o'; Label1[2] = 'm'; break;
          case 2: Label1[0] = 'L'; Label1[1] = 'u'; Label1[2] = 'n'; break;
          case 3: Label1[0] = 'M'; Label1[1] = 'a'; Label1[2] = 'r'; break;
          case 4: Label1[0] = 'M'; Label1[1] = 'i'; Label1[2] = 'e'; break;
          case 5: Label1[0] = 'J'; Label1[1] = 'u'; Label1[2] = 'e'; break;
          case 6: Label1[0] = 'V'; Label1[1] = 'i'; Label1[2] = 'e'; break;
          case 7: Label1[0] = 'S'; Label1[1] = 'a'; Label1[2] = 'b'; break;
     }
     switch(Month){
          case 0x01: Label1[7] = 'E'; Label1[8] = 'n'; Label1[9] = 'e'; break;
          case 0x02: Label1[7] = 'F'; Label1[8] = 'e'; Label1[9] = 'b'; break;
          case 0x03: Label1[7] = 'M'; Label1[8] = 'a'; Label1[9] = 'r'; break;
          case 0x04: Label1[7] = 'A'; Label1[8] = 'b'; Label1[9] = 'r'; break;
          case 0x05: Label1[7] = 'M'; Label1[8] = 'a'; Label1[9] = 'y'; break;
          case 0x06: Label1[7] = 'J'; Label1[8] = 'u'; Label1[9] = 'n'; break;
          case 0x07: Label1[7] = 'J'; Label1[8] = 'u'; Label1[9] = 'l'; break;
          case 0x08: Label1[7] = 'A'; Label1[8] = 'g'; Label1[9] = '0'; break;
          case 0x09: Label1[7] = 'S'; Label1[8] = 'e'; Label1[9] = 'p'; break;
          case 0x10: Label1[7] = 'O'; Label1[8] = 'c'; Label1[9] = 't'; break;
          case 0x11: Label1[7] = 'N'; Label1[8] = 'o'; Label1[9] = 'v'; break;
          case 0x12: Label1[7] = 'D'; Label1[8] = 'i'; Label1[9] = 'c'; break;
     }
     SET_DDRAM_WRITE(0x80,&LABEL1);
     SET_DDRAM_WRITECHAR(0xC2,':');
     SET_DDRAM_WRITECHAR(0xC5,':');
     SET_DDRAM_BCD_WRITE(0x84,Date);
     SET_DDRAM_BCD_WRITE(0x8D,Year);
     SET_DDRAM_BCD_WRITE(0xC0,Hour);
     SET_DDRAM_BCD_WRITE(0xC3,Min);
     SET_DDRAM_BCD_WRITE(0xC6,Seg);

}
void PWM_CONF(void){
     CCP1CON.P1M1 = 0;                   //PWM Single Output, P1A modulada, P1B, P1C y P1D como I/O
     CCP1CON.P1M0 = 0;
     CCP1CON.CCP1M3 = 1;                 //Modo PWM P1A, P1B, P1C y P1D activas en Alto
     CCP1CON.CCP1M2 = 1;
     T2CON.T2CKPS1 = 1;
     //PREESCALA DE TIMER 2 1:1
     PIR1.TMR2IF = 0;                    //Limpieza de Bandera de Interrupción de Timer 2
     T2CON.TMR2ON=1;                     //Activación de Timer 2
     TRISC.RC2 = 0;                      //Pin 2 del Puerto C (RC2) activada como Salida
}
void PWM_DUTY(int duty_c){
     CCP1CON |= ((duty_c&0x0003)<<4);    //De 0 a 1023 partes equivalentes de 0 a 1023
     CCPR1L = duty_c>>2;                //Fo = 4MHz  Se considera Preescala de TMR2 1:1
}
void PWM_T(int periodo){
     PR2 = (periodo-1);
}
void RS_232INIT(void){
     TXSTA.SYNC = 0;            //EUSART en Modo Asíncrono
     TXSTA.BRGH = 1;            //EUSART en Baja Velocidad
     BAUDCTL.BRG16 = 0;         //Generador de 8 bits para Baudrate
     SPBRG = 25;                //2400 Bits/segundo, BaudRate = 2400
     RCSTA.SPEN = 1;            //Habilita TX y RX como terminales del puerto serial
     RCSTA.CREN = 1;            //Habilita recepción
     TXSTA.TXEN = 1;            //Habilitación de la Recepción
     PIE1.RCIE = 1;             //Habilitación de la Interrupción por Recepción
     INTCON.PEIE = 1;           //Habilitación de la Interrupción por Periférico

}