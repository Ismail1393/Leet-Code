#include <stdio.h>
#include <math.h>
int c[8];
printf("Enter the values ");
for (i=0;i<8;i++){
    scanf("%d", &c[i])
}
if(c[0] == c[2] && c[1] == c[7] && c[6] == c[4] && c[3] == c[5]){
        int l1, l2;
        l1 = pow((pow(c[2]-c[0],2)+pow(c[3]-c[1],2) ),0.5);
        l2 = pow((pow(c[4]-c[2],2)+pow(c[5]-c[3],2) ),0.5);
        if (l1 == l2){
            printf("its a square");
        }
        else printf("its a rectangle");
else 
    printf("its a quadtrilater");
        
}