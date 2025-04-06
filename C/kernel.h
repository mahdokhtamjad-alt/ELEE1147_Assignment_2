//Header for register operations
#ifndef KERNEL_H
#define KERNEL_H

//Basic low-level operations
void write_register(unsigned int *reg, unsigned int value); //Writes a value to a register
unsigned int read_register(unsigned int reg, unsigned int mask, unsigned int shift); //Reads the masked and shifted value from register

//System initialization
void init_registers(void); //Initializes all registers with random values

//Functions for retrieving data readings
unsigned int read_cpu_usg(void); //Returns CPU usage
unsigned int read_memry_usage(void); //Returns memory usage
unsigned int read_temperture(void); //Returns temperature 
unsigned int read_power_consumption(void); //Returns power consumption

#endif