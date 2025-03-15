#include <iostream>
using namespace std;

int main() {
  int a = 9, b;
  int* p = &a; // 포인터 변수 *사용필요
  cout << a << "/ " << &a << "~\n";
  cout << *p << "/ " << p << "~\n";
  *p = 17;
  cout << a << "/ " << &a << "~\n";
  cout << *p << "/ " << p << "~\n";
  p = &b; // 포인터변수의 주소를 받을때는 *을 사용하지 않는다.
  *p = 7; // 포인터변수의 가지고있는데 주소의 접근할떄는 *을 사용한다.
  cout << *p << "/ " << p << "~\n";


  return 0;
}



// #include <iostream>
// using namespace std;

// int main() {
//   string name;
//   cin >> name;
//   cout << "hello " << name << "~\n";

//   return 0;
// }