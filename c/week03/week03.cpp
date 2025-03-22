#include <iostream>
using namespace std;

class Pokemon {
private:
  int hp;
public:
  Pokemon() {
    hp = 1;
  cout << "Default Coonstructr\n";
    
  }
  // Pokemon(int hp) {
  //   this->hp = hp;
  // }
  Pokemon(int hp) : hp(hp) {
  cout << "Parameter Constructor\n";

  }
  Pokemon(const Pokemon& pokemon) : hp(pokemon.hp) {
    cout << "Copy Constructor\n";
  }
  ~Pokemon(){
    cout << "Destructor\n";
  }
  void setHp(int hp) {
    this->hp = hp;

  }
  int getHp() {
    return hp;
  }

};
Pokemon p3(50);

Pokemon* test() {
  Pokemon* p4 = new Pokemon(200);
  Pokemon p5(77);
  cout << p4->getHp() <<endl;
  cout << p5.getHp() <<endl;

  return p4;
}

int main() {
  Pokemon p0;
  Pokemon p1(100);
  Pokemon p2(p0);
  //Pokemon* p4 = new Pokemon(200);

  Pokemon* p6 = test();
  p0.setHp(99);

  cout << p0.getHp() <<endl;
  cout << p1.getHp() <<endl;
  cout << p2.getHp() <<endl;
  cout << p3.getHp() <<endl;
  //cout << p4->getHp() <<endl;

  delete p5;

  return 0;
}
