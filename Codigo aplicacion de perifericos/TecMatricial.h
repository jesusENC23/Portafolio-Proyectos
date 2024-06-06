#define PULLUP_PORT     TRISB
#define CONFIG_REG      OPTION_REG
#define ON_REG          WPUB
#define A_D             ANSELH
#define IDLE            0xFF
#define TM_PORT         PORTB
#define ROWB1E          TRISB.RB7
#define ROWB2E          TRISB.RB6
#define ROWB3E          TRISB.RB5
#define ROWB4E          TRISB.RB4
#define ROWB1           PORTB.RB7
#define ROWB2           PORTB.RB6
#define ROWB3           PORTB.RB5
#define ROWB4           PORTB.RB4

void INI_TM(void);
unsigned char TM_tecla(void);
unsigned char TM_POLLING(void);
void TM_NTOUCH(void);

