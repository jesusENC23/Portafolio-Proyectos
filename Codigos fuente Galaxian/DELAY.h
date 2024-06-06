#include "stdint.h"
#include "stm32f4xx.h"
#define Ktiempo_ms (SystemCoreClock/16000)
#define KTiempo_adj (Ktiempo_ms-4000)

void Delay_mls(uint32_t nCount); 
void Delay_t(uint32_t nCount);
