#include <stdio.h>


void main(){
    int x=4,y=12;
    int z=y;
    y=0;
while(z!=0){
    z=x%y;
    x=y;
    y=z;
}
printf("y is %d \n",y);
return 0;
}