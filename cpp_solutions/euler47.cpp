#include <iostream>
#include <time.h>
int * primes_sieve(int limit);

int main(int argc,char ** argv){
	time_t time = clock();
	int * c = primes_sieve(atoi(argv[1]));
	int *l = new int[atoi(argv[1])];
	for(int i = 0; i < atoi(argv[1]); i++)
		l[i]=0;
	for(int i =0; c[i] != 0; i++){
		int s = c[i];
		while(s<atoi(argv[1])){
			l[s]++;
			s+=c[i];
		}
	}
	int count=0;
	int i = 0;
	while( i < atoi(argv[1]) && count <4)
	{
		if(l[i++] == 4)
			count++;
		else 
			count=0;
	}
	std::cout <<i-4 << '\n'<< float(clock()-time)/CLOCKS_PER_SEC*1000  << " miliseconds";
	return 0;
}

int * primes_sieve(int limit){
	bool *a = new bool[limit];
	int *b = new int[limit];
	for(int i = 0; i < limit; i++)
		{
		a[i] = 1;
		b[i] = 0;
	}
	a[0] = a[1] = 0;
	for(int i = 2;i < limit; i++)
	{
		if(a[i]){
			int j = 2 * i;
			while(j < limit){
				a[j]=0;
				j+=i;
			}
		}
	}
	int j = 0;
	for(int i = 0; i < limit; i++)
		if(a[i]){
			b[j++]=i;
		}
	return b;
	}
	
