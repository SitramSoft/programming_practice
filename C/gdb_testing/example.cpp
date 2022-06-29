#include <iostream>
#include <stdlib.h> //srand
#include <stdio.h>  //printf

using namespace std;

int main () {

srand (time(NULL));
int alpha = rand() % 8;
cout << "Hello world." << endl;
int beta = 2;

printf("alpha is set to is %s\n", alpha);
printf("kiwi is set to is %s\n", beta);

 return 0;
} // main