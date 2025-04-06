#ifndef KERNEL_H
#define KERNEL_H


void write_register(unsigned int *reg, unsigned int value);
unsigned int read_register(unsigned int reg, unsigned int mask, unsigned int shift);

void init_registers(void);

unsigned int read_cpu_usg(void);
unsigned int read_memry_usage(void);
unsigned int read_temperture(void);
unsigned int read_power_consumption(void);

#endif