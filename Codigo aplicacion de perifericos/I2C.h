/*
--------------------------------------------------------------------------------
Driver I2C
Jesus Emmanuel Niño Castillo 221800201
--------------------------------------------------------------------------------
*/
//Asignacion de terminales y puertos
#define SCL_Dir            TRISC.RC3
#define SDA_Dir            TRISC.RC4
#define SCL                PORTC.RC3
#define SDA                PORTC.RC4

//BITS DE CONFIGURACION
#define Slave_Mode_10bits_SS        0x0F //I2C SLAVE MODE, 10 BITS ADDRS + START +STOP
#define Slave_Mode_7bits_SS         0x0E //I2C SLAVE MODE, 7 BITS ADDRS + START +STOP
#define Master_Mode_Firmware        0x0E //I2C MASTER MODE, FIRMWARE CONTROLLED MASTER MODE(SLAVE_IDLE)
#define Master_Mode_Clock           0x08 //I2C MASTER MODE, CLOCL DEFINIDO EN SSPADD
#define Slave_Mode_10bits           0x07 //I2C SLAVE MODE, 10 BITS ADDRS
#define Slave_Mode_7bits            0x06 //I2C SLAVE MODE, 7 BITS ADDRS

//VELOCIDAD DE I2C
#define FOSC             4000000 //hz
#define I2C_SPEED        100000  //hz

#define SSPADD_Speed     ((FOSC/(4*I2C_SPEED))-1) //VELOCIDAD DEL I2C

//DIRECCION DEL DS1307
#define DS1307_ID     0x68 //DIRECCION DEL CHIP
#define R             1    //READ
#define W             0    //WRITE
#define DS1307_R      ((DS1307_ID<<1)+R) //LECTURA DEL DS1307
#define DS1307_W      ((DS1307_ID<<1)+W) //ESCRITURA DEL DS1307

//DIRECCION DEL LM75B
#define LM75_ID      0x48
#define RLM75        1    //READ
#define WLM75        0    //WRITE
#define LM75_R      ((LM75_ID<<1)+R) //LECTURA DEL DS1307    // ACKNOWLEDGE
#define LM75_W      ((LM75_ID<<1)+W) //ESCRITURA DEL DS1307  #define ACK  0        //ACKNOWLEDGE ACK = 0, RECIBIDO

// ACKNOWLEDGE
#define ACK  0        //ACKNOWLEDGE ACK = 0, RECIBIDO
#define NACK 1        //NO ACKNOWLEDGE ACK = 1

void I2C_init(void);
void I2C_port(void);
void I2C_wait(void);
void I2C_start(void);
void I2C_restart(void);
void I2C_stop(void);
void I2C_write(unsigned char Data);
unsigned char I2C_read(unsigned char Ack);
