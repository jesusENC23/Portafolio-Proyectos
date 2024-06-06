#define DB0      0              //BITS DEL BUS DE DATOS
#define DB1      1              //
#define DB2      2              //
#define DB3      3              //
#define DB4      4              //
#define DB5      5              //
#define DB6      6              //
#define DB7      7              //
#define ID       1              //INCREMENT/DECREMENT MODE
#define SH       0              //ENTERE SHIFT ON/OFF
#define BLK      0              //BLINK ON/OFF
#define CUR      1              //CURSOR ON/OFF
#define DSP      2              //DISPLAY ON/OFF
#define F        2              //MATRIX
#define NL       3              //N LINES
#define B_BUSY   7              //BIT BUSY FLAG
#define RS       0              //REGISTER SELECT
#define RW       1              //READ/WRITE
#define E        2              //BIT ENABLE
#define SC       3              //DESPLAZAMIENTO DEL DISPLAY Y CURSOR
#define RL       2              //IZQUIERDA DERECHA
#define DataBusE  TRISD
#define CtrlBusE  TRISE
#define DataBus  PORTD
#define CtrlBus  PORTE

void INI_LCD(void);
void configuracion(void);
void RESET_LCD(void);
void CONFIG_SET(void);
void DISPLAY_ON_OFF(void);
void ENTRY_MODE_SET(void);
void CLEAR_DISPLAY(void);
void SET_DDRAM(unsigned char DIRR);
void SET_DDRAM_WRITE(unsigned char DIRR, unsigned char *String_Dir);
void SET_DDRAM_WRITECHAR(unsigned char DIRR, unsigned char CHARR);
void SET_DDRAM_BCD_WRITE(unsigned char DIRR, unsigned int DATA);

void ENABLE(void);
void ENABLEW(unsigned char DataTOWrite);
