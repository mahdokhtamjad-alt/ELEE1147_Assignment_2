//Initialization
#include "kernel.h"
#include <stdlib.h>  
#include <time.h>


unsigned int CPU_REGISTER;
unsigned int MEMORY_REGISTER;
unsigned int TEMPERATURE_REGISTER;
unsigned int POWER_REGISTER;

//Write values to a register
void write_register(unsigned int *reg, unsigned int value) 
{
    *reg = value;

}

//Read a masked and shifted value from a register
unsigned int read_register(unsigned int reg, unsigned int mask, unsigned int shift){ 
    return (reg & mask) >> shift; 
}

//Randomly initialize the registers
void init_registers() {

        TEMPERATURE_REGISTER = (unsigned int)(rand() % (8890 - 3260 + 1) + 3260);  
        POWER_REGISTER = rand() % (120 - 400 + 1) + 40;
        MEMORY_REGISTER = rand() % (32000 - 800 + 1) + 800;
        CPU_REGISTER = rand() % (100 - 10 + 1) + 10;

}

//Return the CPU usage register
unsigned int read_cpu_usage(){ 
    return CPU_REGISTER;  
}

//Return the memory usage register
unsigned int read_memory_usage() {
    return MEMORY_REGISTER; 
}

//Return the temperature register after dividing by 100
unsigned int read_temperture() {
    return TEMPERATURE_REGISTER / 100.0; 
}

//Return the power consumption register
unsigned int read_power_consumption() {
    return POWER_REGISTER;
}  
