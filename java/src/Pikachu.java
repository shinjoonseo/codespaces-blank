//public class Pikachu extends Pokemon implements Flyable {
public class Pikachu extends Pokemon {
    public Pikachu(int hp, int attackRate, String name, Flyable flyable) {
        super(hp, attackRate, name, flyable);
        System.out.println("피까피까(매개변수 생성자)");
    }

    @Override
    public void attack() {

    }

//    @Override
//    public void fly() {
//        System.out.println(this.getName() + "이(가) 하늘을 날수 없습니다!");
//    }
}
