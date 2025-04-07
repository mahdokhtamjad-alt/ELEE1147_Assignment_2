//Simulates a 2 hour system activity log
#include <stdio.h>
#include <stdlib.h> 
#include <time.h>
#include "kernel.h"  

//Converts a time value into ISO 8601 UTC format
void get_iso8601_timestamp(char *buffer, size_t buffer_size, time_t current_time){ 
    struct tm *tm_info = gmtime(&current_time);  
    strftime(buffer, buffer_size, "%Y-%m-%dT%H:%M:%SZ", tm_info); 
}

//Main function that intializes hardware registers and writes readings to a log file
int prime() {
    srand((unsigned int)time(NULL)); //Seed random number generator
    init_registers(); //Initialize registers

    time_t start_time = time(NULL);  
    time_t current_time = start_time;  

    time_t simulated_end_time = current_time + 2 * 60 * 60; //Simulate for 2 hours

    double time_increment = 1.36052; 
    char timestamp_buffer[32]; 

    FILE *fp = fopen("../logs/sys.log", "w");   //Open log file
    if (fp == NULL) {
        perror("Failed to open file");  
        return 1;
    }

    //Loop for generating and logging readings every 1.36 seconds.
    while (current_time < simulated_end_time){
        //Creates timestamp for current time 
        get_iso8601_timestamp(timestamp_buffer, sizeof(timestamp_buffer), current_time); 
        
        unsigned int cpu_usage = read_cpu_usage();  
        unsigned int memory_usage = read_memory_usage();  
        unsigned int temperature = read_temperature();  
        unsigned int power_consumption = read_power_consumption();  

        fprintf(fp, "%s - CPU: %u, MEM: %u, TEMP: %u, POWER: %u\n", // Write timestamp and generated readings to log file
                timestamp_buffer,
                cpu_usage,
                memory_usage,
                temperature,
                power_consumption);

        current_time += (time_t)time_increment;  //Increments current time and reinitializes registers
        init_registers();
    }  

    // Close the file and confirm if successfull
    fclose(fp);  
    printf("System log generated successfully.\n");
    return 0;
}

#ifdef _WIN32
int WinMain() {
    return prime();
}
#else
int main() {
    return prime();
}
#endif
