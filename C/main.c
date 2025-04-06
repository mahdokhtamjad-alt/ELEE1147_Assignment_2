#include <stdio.h>
#include <stdlib.h> 
#include <time.h>
#include "kernel.h"  


void get_iso8601_timestamp(char *buffer, size_t buffer_size, time_t current_time){ 
    struct tm *tm_info = gmtime(&current_time);  
    strftime(buffer, buffer_size, "%Y-%m-%dT%H:%M:%SZ", tm_info); 
}

int prime() {
    srand((unsigned int)time(NULL)); 
    init_registers(); 

    time_t start_time = time(NULL);  
    time_t current_time = start_time;  

    time_t simulated_end_time = current_time + 2 * 60 * 60;

    double time_increment = 1.36052; 
    char timestamp_buffer[32]; 

    FILE *fp = fopen("../logs/sys.log", "w");
    if (fp == NULL) {
        perror("Failed to open file");  
        return 1;
    }

    while (current_time < simulated_end_time){ 
        get_iso8601_timestamp(timestamp_buffer, sizeof(timestamp_buffer), current_time); 
        
        unsigned int cpu_usage = read_cpu_usage();  
        unsigned int memory_usage = read_memory_usage();  
        unsigned int temperature = read_temperature();  
        unsigned int power_consumption = read_power_consumption();  

        fprintf(fp, "%s - CPU: %u, MEM: %u, TEMP: %u, POWER: %u\n",
                timestamp_buffer,
                cpu_usage,
                memory_usage,
                temperature,
                power_consumption);

        current_time += (time_t)time_increment;  
        init_registers();
    }  

    fclose(fp);  
    printf("System log generated successfully.\n");
    return 0;
}