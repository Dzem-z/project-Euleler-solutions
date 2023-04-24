#include <iostream>
#include <bitset>
#include <time.h>
#include <math.h>
#define LIMIT 10000
#define RSIZE 2000
__int64_t power(int a, int n, int mod)
{
 __int64_t power=a,result=1;

 while(n)
 {
  if(n&1)
   result=(result*power)%mod;
  power=(power*power)%mod;
  n>>=1;
 }
 return result;
}

bool witness(int a, int n)
{
 int t,u,i;
 __int64_t prev;
 __int64_t curr;

 u=n/2;
 t=1;
 while(!(u&1)){
  u/=2;
  ++t;
  }

  prev=power(a,u,n);
 for(i=1;i<=t;++i)
 {
  curr=(prev*prev)%n;
  if((curr==1)&&(prev!=1)&&(prev!=n-1))
   return true;
  prev=curr;
 }
 if(curr!=1)
  return true;
 return false;
}

inline bool IsPrime( int number )
{
 if ( ( (!(number & 1)) && number != 2 ) || (number < 2) || (number % 3 == 0 && number != 3) )
  return (false);

 if(number<1373653)
 {
  for( int k = 1; 36*k*k-12*k < number;++k)
  if ( (number % (6*k+1) == 0) || (number % (6*k-1) == 0) )
   return (false);

  return true;
 }

 if(number < 9080191)
 {
  if(witness(31,number)) return false;
  if(witness(73,number)) return false;
  return true;
 }


 if(witness(2,number)) return false;
 if(witness(7,number)) return false;
 if(witness(61,number)) return false;
 return true;

 /*WARNING: Algorithm deterministic only for numbers < 4,759,123,141 (unsigned int's max is 4294967296)
   if n < 1,373,653, it is enough to test a = 2 and 3.
   if n < 9,080,191, it is enough to test a = 31 and 73.
   if n < 4,759,123,141, it is enough to test a = 2, 7, and 61.
   if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11.
   if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13.
   if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.*/
}

std::bitset<LIMIT> Primes;
void SieveOfEratosthenes()
{
    Primes[0] = 1;
    for (int i = 3; i < LIMIT; i += 2)
    {
        if (Primes[i / 2] == 0)
        {
            for (int j = 3 * i; j < LIMIT; j += 2 * i)
                Primes[j / 2] = 1;
        }
    }
}
int primes[RSIZE] = {};
int powers_of_10[6] = {0,1,10,100,1000,10000};
char len(int num);
bool isPair(int num1, int num2);
int main(int argc, char * argv[]){
    SieveOfEratosthenes();
    clock_t time = clock();
    std::bitset<LIMIT> * array = new std::bitset<LIMIT>[LIMIT];
    for(int i = 0; i < LIMIT; i++)
      array[i] = std::bitset<LIMIT>();
    std::cout << isPair(7,11) << std::endl;
    int size = 0;
    primes[0] = 2;
    for(int i = 3; i < LIMIT; i+=2)
      if(Primes[i/2] == 0)
        primes[size++] = i;

    for(int i = 0; i < size; i++){
      for(int j = i; j < size; j++){
        if(isPair(primes[i],primes[j]))
          array[i][j] = 1;
        }
      }
    int p[5] = {};
    for(int i = 1; i < size; i++){
      for(int j = i; j < size; j++){
        if(array[i][j]){
          for(int k = j; k < size; k++){
            if(array[i][k] && array[j][k]){
              for(int z = k; z < size; z++){
                if(array[i][z] && array[j][z] && array[k][z]){
                  for(int c = z; c < size; c++){
                    if(array[i][c] && array[j][c] && array[k][c] && array[z][c]){
                      p[0] = primes[i];
                      p[1] = primes[j];
                      p[2] = primes[k];
                      p[3] = primes[z];
                      p[4] = primes[c];
                      goto a;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    a:
    int sum = 0;
    for(int i = 0; i < 5; i++){
      sum +=  p[i];
    }
    std::cout << sum << std::endl;
    std::cout << (clock()-time)*1000.f/CLOCKS_PER_SEC << " miliseconds elapsed";
  return 0;
}

bool isPair(int num1, int num2){
  char len1 = len(num1);
  char len2 = len(num2);
  //return IsPrime(num1*powers_of_10[len2]+num2) && IsPrime(num2*powers_of_10[len1] + num1);
  return IsPrime(num1*pow(10,len2)+num2) && IsPrime(num2*pow(10,len1) + num1);
}

char len(int num){
  char c = 0;
  while(num > 0){
    c++;
    num /= 10;
    }
  return c;
  }
