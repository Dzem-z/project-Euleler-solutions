#include <iostream>
#include <math.h>
#include <time.h>
#define SIZE 1000000000 / 3 + 2

long int gcd(long int num1, long int num2){
	long int b = num1;
	while(num2 > 0){
		num1 = num2;
		num2 = b % num2;
		b = num1;
	}
	return b;
};

int main(){
	double s = 0;
	double area = 0;
	clock_t time = clock();
	long int perimeters = 0;
	int n = 0;
	int m = 0;
	long int c = 0;
	n = 1;
	m = 2;
	while(m*m + 1 < SIZE){
		if(n >= m){
			n = m%2;
			m += 1;
		}
		c = m*m + n*n;
		if(c >= SIZE)
			n = m;			
		else{
			if(gcd(m,n) == 1){
				long int a = m*m - n*n;
				long int b = 2*m*n;
				if(abs(2*a - c) == 1)
					perimeters += 2*a + 2*c;
				if(abs(2*b - c) == 1)
					perimeters += 2*b + 2*c;
				}
			n += 2;	
		}
		
	}
	std::cout << perimeters << std::endl;
	std::cout << "time: " << (clock() - time)*1.0/CLOCKS_PER_SEC << std::endl;
	return 0;
}
