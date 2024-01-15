#include <iostream>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
using namespace std;



int fe(int x){
	int f = x-34;
	return f;
}

int find_x(){
	int count=0;
	int x = rand();
	srand(time(NULL));
	int	f = fe(x); 
	while(f != 0 and count<100000000000){
		x = rand()%100000000;
		f = fe(x);
		count++;
		if(f == 0){
			return x;
		}
	}

}
int main(){
	int x = find_x();
	cout <<pow(3,1.0/3.0) <<endl;
	return 0;
}
