#include <iostream>
using namespace std;
int g;

//void test(int b) {
int* test(int b) {
  int c;

  int* pa;
  pa = new int;
  cout << &pa << endl;  // stack
  cout << pa << endl;  // heap
  //delete pa;
  cout << &b << endl; 
  cout << &c << endl; 

  
  
  return pa;
}

int main() {
  int a;

  cout << &a << endl;  // stack
  int* mainPtr = test(77);
  cout << &g << endl;  //static
  cout << mainPtr << endl;

  delete mainPtr;
  return 0;
}

// #include <iostream>
// using namespace std;

// int main() {
//   int people = 0;
//   int totalPrice = 0;
//   //int ages[people] = {};
//   cin >> people;

//   int* ages = new int[people]; //heap memory
//   for(int i=0; i<people; i++) {
//     cout << "How old are u";
//     cin >> ages[i];
//   }
//   for(int j=0; j<people; j++) {
//     // kids : 5000, adulst : 9000, senior : 6000
//     int age = ages[j];
//     if (age < 8)
//       totalPrice = totalPrice + 5000;
//     else if(age < 65)
//       totalPrice = totalPrice + 9000;
//     else
//       totalPrice = totalPrice + 6000;
//   }

//   delete[] ages; // 메모리 초기화
//   cout << "Total price : " << totalPrice << '\n';

//   return 0;
// }