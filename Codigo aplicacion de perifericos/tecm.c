#include "TecMatricial.h"

void INI_TM() {
    A_D = 0;
    PULLUP_PORT = 0xFF;          //puerto b como entrada
    CONFIG_REG &= 0x7F;          //activar pull ups
    ON_REG = 0x0F;               //activar Pull Ups 0-3
    }

unsigned char TM_tecla(){
     unsigned char tecla = IDLE;
     ROWB1E = 0; //fila 0 como salida
     ROWB1  = 0;
     switch(TM_PORT&0x0F) {
         case 0x07: tecla = '1'; break;
         case 0x0B: tecla = '2'; break;
         case 0x0D: tecla = '3'; break;
         case 0x0E: tecla = 'A'; break;
     }
     ROWB1E = 1; //fila 0 como entrada

     ROWB2E = 0; //fila 1 como salida
     ROWB2  = 0;
     switch(TM_PORT&0x0F) {
         case 0x07: tecla = '4'; break;
         case 0x0B: tecla = '5'; break;
         case 0x0D: tecla = '6'; break;
         case 0x0E: tecla = 'B'; break;
     }
     ROWB2E = 1; //fila 1 como entrada

     ROWB3E = 0; //fila 2 como salida
     ROWB3  = 0;
     switch(TM_PORT&0x0F) {
         case 0x07: tecla = '7'; break;
         case 0x0B: tecla = '8'; break;
         case 0x0D: tecla = '9'; break;
         case 0x0E: tecla = 'C'; break;
    }
    ROWB3E = 1; //fila 2 como entrada

    ROWB4E = 0; //fila 3 como salida
    ROWB4  = 0;
    switch(TM_PORT&0x0F) {
       case 0x07: tecla = '*'; break;
       case 0x0B: tecla = '0'; break;
       case 0x0D: tecla = '#'; break;
       case 0x0E: tecla = 'D'; break;
    }
    ROWB4E = 1; //fila 3 como entrada
    return tecla;
}
unsigned char TM_POLLING(void){
    unsigned char tecla;
    do{
       tecla=TM_tecla();
    }while(tecla == IDLE);
    while(TM_tecla() != IDLE);
    return tecla;
}
void TM_NTOUCH(void){
    while(TM_tecla()!= IDLE);
}