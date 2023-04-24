#include <iostream>
#include <time.h>
#include <string.h>

bool * primes_sieve(int limit);
int  primes_sieve(int * &arr ,bool * barr, int limit);
char * to_string(int num);
template <typename T>
char len(T *);

int main(int argc, char * argv[]){
	clock_t time = clock();
	//-----------------------------------------

	int limit = atoi(argv[1]);
	bool * primes = primes_sieve(limit);
	int * primeS;
	int size = primes_sieve(primeS,primes,limit);
	char digits[3] = {'0','1','2'};
	char  *prime;
	char  prime_s[10];
	int counter = 0;
	int c = 0;
	char chr;
	int ind[10] = {0};
	a:
	while(counter < 8){
        for(int j = 0; j < size; j++){
			for(int i = 0; i < 3; i++){
				for(int a = 0; a < 10; a++)prime_s[a] = ind[a] = 0;
				prime = to_string(primeS[j]);
				c = 0;
				for( int iter = 0; iter < len(prime);iter++){
					if( digits[i] == prime[iter]){
						ind[c++] = iter+'0';
					}
				}
				if(c  != 3)
					continue;
				chr = digits[i];
				counter = 0;
				while(chr - '0' - counter < 5 && chr-'0' < 10){
					strcpy(prime_s,prime);
					for(int w = 0; w < len(ind); w++)
						prime_s[ind[w]-'0'] = chr;
					if(primes[atoi(prime_s)]){
						counter += 1;
						}
                    chr += 1;

				}
				if(counter > 7)
                    goto a;
				delete[] prime;
			}
		}
	}
    std::cout << prime << '\n';
    delete[] primes;
    delete[] primeS;
	//-----------------------------------------
	std::cout << (clock()-time)*1000.f/CLOCKS_PER_SEC << " miliseconds elapsed";
	return 0;
}
template <typename T>
char len(T * str){
	char i = 0;
	while(str[i] != 0)i++;
	return i;
}

char * to_string(int num){
	int i  =0;
	int cn = num;
	while(cn > 0){
		cn/=10;
		i++;
		}
	char * str = new char[i+1];
	str[i] = '\0';
	for(int j = i-1; j >= 0; j--){
		str[j] = '0' + num%10;
		num /=10;
		}
	return str;
}

bool * primes_sieve(int limit){
	bool  * primes = new bool[limit];
	for(int i = 0; i < limit; i++)
		primes[i]= 1;
	primes[0] = primes[1] = 0;
	for(int i = 0; i < limit; i++){
		if(primes[i])
			for(int j = 2*i; j < limit; j += i)
				primes[j]=0;
	}
	return primes;
};

int primes_sieve(int * &arr,bool *barr,int limit){
	int size=0;
	for(int i =0; i < limit; i++)
		if(barr[i]) size++;
	arr = new int[size];
	int j = 0;
	for(int i = 0; i < limit; i++)
		if(barr[i])
			arr[j++] = i;
	return size;
}

