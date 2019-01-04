Row header: Base 0, size 10                              
---------------------------                              
                                                         
0      Row format specifier                              
1      Time in seconds                                   
2 - 9  Reserved                                          
                                                         
Temperature controller values: Base = 10, size 60        
-------------------------------------------------        
                                                         
0 - 11     Temperature readout, Zone 1 to 12             
12, 13     Thermocouple cold junction temperature        
14         Aux thermocouple readout - 1                  
15         Aux thermocouple readout - 2                  
                                                         
16 - 27    Temperature setpoint, Zone 1 to 12            
28 - 31    Reserved                                      
                                                         
32 - 43    Heater power, Zone 1 to 12                    
44 - 47    Reserved                                      
                                                         
48         Furnace mains -- 0: OFF,  1: ON               
49         Furnace lid   -- 0: OPEN, 1: CLOSED           
                                                         
50 - 59    Reserved                                      
                                                         
MFC 1 values: Base 70, size 15                           
--------------------------------                         
                                                         
0         MFC 1 gas index                                
1         MFC 1 flow readout in SI unit (cu.m/sec)       
2         MFC 1 flow readout in SCCM                     
3         MFC 1 flow setpoint in SI unit (cu.m/sec)      
4         MFC 1 flow setpoint in SCCM                    
5         MFC 1 inlet pressure in SI unit (Pascal)       
6         MFC 1 inlet pressure in PSI                    
7         MFC 1 status       -- 0 : OFF, 1 : ON          
8         MFC 1 flush status -- 0 : OFF, 1 : ON          
9 - 14    MFC 1 reserved                                 
                                                         
MFC 2 values: Base 85,  size 15                          
MFC 3 values: Base 100, size 15                          
MFC 4 values: Base 115, size 15                          
MFC 5 values: Base 130, size 15                          
MFC 6 values: Base 145, size 15                          
MFC 7 values: Base 160, size 15                          
MFC 8 values: Base 175, size 15                          
--------------------------------                         
                                                         
Chassis controller values: Base 190, size 15             
--------------------------------------------             
                                                         
0        Pirani readout in SI unit (Pascal)              
1        Pirani readout in mbar                          
2        Aux pressure in SI unit (Pascal)                
3        Aux pressure in PSI                             
4        Vacuum pump -- 0 : OFF, 1 : ON                  
5        Purge       -- 0 : OFF, 1 : ON                  
6 - 14   Reserved                                        
