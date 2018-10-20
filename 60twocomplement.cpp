//Name:  Saar Haber
//Date:  April 19 2018
//program 60!!!!!

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

int main ()          //C++ programs all have a main() function
{
int n;
cout << "Enter a number between -31 and 31";
cin >> n;

int x;
int b = 16;

if (n<0){
  cout << 1;
  x = 32 + n;
}

if (n>=0){
  cout << 0;
  x = n;
}

while (b>0.5){
  if (x>=b){
    cout << 1;
  }
  else {
    cout << 0;
  }
  x = x%b;
  b = b/2;
  }
cout << "\n";

}
