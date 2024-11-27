public class PokemonGame {
    public static void main(String[] args) {
        //Pokemon pokemon = new Pokemon();  // 추상클래스의 객체(인스턴스) 생성 불가
        Charizard charizard1 = new Charizard(500, 200, "멋진 리자몽", new Wings());  // 리자몽 클래스는 구체(concrete) 클래스로 객체(인스턴스) 생성 가능
        Charizard charizard2 = new Charizard();  // 리자몽 클래스는 구체(concrete) 클래스로 객체(인스턴스) 생성 가능
        Pikachu pikachu1 = new Pikachu(280, 90, "지우 피카츄", new NoFly());

        charizard2.setName("나쁜 리자몽");
        //charizard1.attack(charizard2);
        charizard1.attack(pikachu1);
        charizard1.attack();
        //charizard1.fly();
        //pikachu1.fly();
        charizard1.performFly();
        pikachu1.performFly();
        charizard1.attack(pikachu1);
    }
}
