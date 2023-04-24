#include <iostream>
#include <math.h>
#include <time.h>
#define SIZE 1000000000 / 3 + 2
int main(){
	long double s = 0;
	long double area = 0;
	clock_t time = clock();
	long int perimeters = 0;
	for(int i = 2; i < SIZE; i++){
		s = (3 * i + 1)/2.0;
		area = sqrt(s * (s - i) * (s - i) * (s - i -1));
		if( (long long int)area == area){
			//std::cout << "perimeter: " << 2*s << " area: " << area << std::endl;
			if(s <= 5*10e+8)
				perimeters += 2*s;
		}
		s = (3 * i - 1)/2.0;
		area = sqrt(s * (s - i) * (s - i) * (s - i + 1));
		if( (long long int)area == area){
			//std::cout << "perimeter: " << 2*s << " area: " << area << std::endl;
			if(s <= 5*10e+8)
				perimeters += 2*s;
		}
	}
	std::cout << perimeters << std::endl;
	std::cout << "time: " << (clock() - time)*1.0/CLOCKS_PER_SEC << std::endl;
	return 0;
}
