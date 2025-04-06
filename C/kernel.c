#include "kernel.h"
#include <stdlib.h>  
#include <time.h>

unsigned int CPU_REGISTER;
unsigned int MEMORY_REGISTER;
unsigned int TEMPERATURE_REGISTER;
unsigned int POWER_REGISTER;

void write_register(unsigned int *reg, unsigned int value) 
{
    *reg = value;

}
unsigned int read_register(unsigned int reg, unsigned int mask, unsigned int shift){ 
    return (reg & mask) >> shift; 
}

void init_registers() {

        TEMPERATURE_REGISTER = (unsigned int)(rand() % (8890 - 3260 + 1) + 3260);  
        POWER_REGISTER = rand() % (120 - 400 + 1) + 40;
        MEMORY_REGISTER = rand() % (32000 - 800 + 1) + 800;
        CPU_REGISTER = rand() % (100 - 10 + 1) + 10;

}


unsigned int read_cpu_usage(){ 
    return CPU_REGISTER;  
}

unsigned int read_memory_usage() {
    return MEMORY_REGISTER; 
}

unsigned int read_temperture() {
    return TEMPERATURE_REGISTER / 100.0; 
}

unsigned int read_power_consumption() {
    return POWER_REGISTER;
}  
