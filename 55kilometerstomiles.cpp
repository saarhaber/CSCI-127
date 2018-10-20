//Name:  Saar Haber
//Date:  April 19 2018
//program 55

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

int main ()          //C++ programs all have a main() function
{
double num;
cout << "enter number in kilometers";
cin >> num;

double num1 = num*0.621371;
cout << "miles = " << num1;

return 0;
}
