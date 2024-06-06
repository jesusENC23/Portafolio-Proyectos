#include "LCD.h"
unsigned char DB;
void INI_LCD(void){
     configuracion();
     RESET_LCD();
     CONFIG_SET();
     ENABLE();
     DISPLAY_ON_OFF();
     ENABLE();
     CLEAR_DISPLAY();
     ENABLE();
     ENTRY_MODE_SET();
     ENABLE();
}
void configuracion(void){            //INICIALIZACION DEL PUERTO PARA EL LCD
     ANSEL=0;
     CtrlBus &= (0<<RS|0<<RW|0<<E);
     DataBus=0x30;
     CtrlBusE &= (0<<RS|0<<RW|0<<E);
     DataBusE=0;
}
void RESET_LCD(void){                //FUNCION DE RESET E INICIALIZACION LCD
     delay_ms(50);
}
void CONFIG_SET(void){               //CONFIGURACION DEL LCD
/*
RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
 0 0   0  0    1   1   NL  F   *   *
 NL=0 MODO 1 LINEA     F=0 MATRIZ DE 5X7
 NL=1 MODO 2 LINEAS    F=1 MATRIZ DE 5X10
*/
     DB = (1<<DB5)|(1<<DB4)|(1<<NL);
}
void DISPLAY_ON_OFF(void){          //ACTIVACION DEL LCD
/*
RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
 0 0   0  0    0   0   1  DSP CUR BLK
 DSP=0 DISPLAY OFF  CUR=0 CURSOR OFF BLK=0 BLINK OFF
 DSP=1 DISPLAY ON   CUR=1 CURSOR ON  BLK=1 BLINK ON
*/
     DB = (1<<DB3)|(1<<DSP);
     //DB = (1<<DB3)|(1<<DSP)|(1<<CUR)|(1<<BLK);
}
void ENTRY_MODE_SET(void){         //MOVIMIENTO DEL CURSOR
/*
RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
 0 0   0   0   0   0   0   1   ID  SH
 ID=0 DECREMENT MODE     SH=0 ENTIRE SHIFT OFF
 ID=1 INCREMENT MODE     SH=1 ENTIRE SHIFT ON
*/
     DB = (1<<DB2)|(1<<ID);//|(1<<NL);
}
void CLEAR_DISPLAY(void){         //LIMPIAR DISPLAY
/*
RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
 0 0   0   0   0   0   0   0   0   1
*/
     CtrlBus&=~(1<<RS);
     DB = 0x01;
     ENABLE();
}
void SET_DDRAM(unsigned char DIRR){            //DIRECCION DE INICIO DE LA SEGUNDA LINEA
/*
RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
 0 0   1   1   0   0   0   0   0   0
*/
     DB = DIRR;
}
void SET_DDRAM_WRITE(unsigned char DIRR, unsigned char *String_Dir){
     DB = DIRR;
     ENABLE();
     CtrlBus|=(1<<RS);
     while(*String_Dir !='\n'){
          DB=*(String_Dir++);
          ENABLEW(DB);
     }
     CtrlBus&=~(1<<RS);
}
void SET_DDRAM_WRITECHAR(unsigned char DIRR, unsigned char CHARR){
     CtrlBus&=~(1<<RS);
     DB = DIRR;
     ENABLE();
     CtrlBus|=(1<<RS);
     DB=CHARR;
     ENABLEW(DB);
     CtrlBus&=~(1<<RS);
}
void SET_DDRAM_BCD_WRITE(unsigned char DIRR, unsigned int DATA){
     unsigned char i=0,BUFFER[3]={'0','0','\n'};
     CtrlBus&=~(1<<RS);
     DB = DIRR;
     ENABLE();
     BUFFER[0]+=(DATA&0xF0)>>4;
     BUFFER[1]+=DATA&0x0F;
     CtrlBus|=(1<<RS);
     while(BUFFER[i] !='\n'){
          DB=BUFFER[i];
          ENABLEW(DB);
          i++;
     }
     CtrlBus&=~(1<<RS);
}
void ENABLE(void){             //HABILITACION DEL DISPLAY
     DataBus=DB;
     CtrlBus|=(1<<E);
     delay_ms(2);
     CtrlBus&=~(1<<E);
     delay_ms(2);
}
void ENABLEW(unsigned char DataTOWrite){             //HABILITACION DEL DISPLAY
     DataBus=DataTOWrite;
     CtrlBus|=(1<<E);
     delay_ms(2);
     CtrlBus&=~(1<<E);
     delay_ms(2);
}
