----------------------LeakTest22072018.py-----------------------

Qrystal Recipe ver. 1.0
0	Event begin time: 0:00:00	 Event name: System Init
1	Event begin time: 0:00:00	 Event name: CHSSCON Pump On
2	Event begin time: 0:03:00	 Event name: CHSSCON Pump Off
3	Event begin time: 0:03:00	 Event name: MFC Flush On	 Channel: 2
4	Event begin time: 0:05:00	 Event name: MFC Flush Off	 Channel Index: 2
5	Event begin time: 0:05:00	 Event name: CHSSCON Pump On
6	Event begin time: 0:08:00	 Event name: CHSSCON Pump Off
7	Event begin time: 0:08:00	 Event name: MFC Flush On	 Channel: 2
8	Event begin time: 0:10:00	 Event name: MFC Flush Off	 Channel Index: 2
9	Event begin time: 0:10:00	 Event name: CHSSCON Pump On
10	Event begin time: 0:40:00	 Event name: CHSSCON Pump Off
End of recipe
Number of events:  11
Total duration  :  0:40:00


-----------------LeakTest22072018_2.py-----------------------

Qrystal Recipe ver. 1.0
0	Event begin time: 0:00:00	 Event name: System Init
1	Event begin time: 0:00:00	 Event name: TCON Init Ramps
2	Event begin time: 0:00:00	 Event name: CHSSCON Pump On
3	Event begin time: 0:00:00	 Event name: TCON Mains Switch On
4	Event begin time: 0:00:00	 Event name: TCON Linear Ramp	 Zone indx list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]	 Final T: 1273.15	 Duration: 3000
5	Event begin time: 0:00:00	 Event name: MFC Flow Rate	 Channel Index: 2	 Flow rate: 20
6	Event begin time: 0:50:00	 Event name: TCON Linear Ramp	 Zone indx list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]	 Final T: 1273.15	 Duration: 600
7	Event begin time: 1:00:00	 Event name: MFC Flow Rate	 Channel Index: 2	 Flow rate: 0
8	Event begin time: 1:00:00	 Event name: TCON Mains Switch Off
End of recipe
Number of events:  9
Total duration  :  1:00:00
