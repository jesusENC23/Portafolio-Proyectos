#include "DELAY.h"

void Delay_mls(uint32_t nCount){
	nCount = nCount*(Ktiempo_ms-KTiempo_adj);
	Delay_t(nCount);
}	
void Delay_t(uint32_t nCount){
	for(; nCount!=0; nCount--);
}