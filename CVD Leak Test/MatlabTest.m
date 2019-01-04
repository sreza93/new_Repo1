x = 0:0.1:10;
y1 = sin(2*x);
y2 = 10*cos(2*x);

     % add fourth plot in 2 x 2 grid
yyaxis left          % plot against left y-axis  
plot(x,y1)
ylabel('values')
yyaxis right         % plot against right y-axis
plot(x,y2)
title('Subplot 4')
xlabel('time')
ylabel ('values1')
legend('Temp','pressure')
