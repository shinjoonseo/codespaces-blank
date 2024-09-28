//public class Charizard extends Pokemon implements Flyable{
public class Charizard extends Pokemon{
    public Charizard() {
        System.out.println("자몽자몽(기본 생성자)");
    }

    public Charizard(int hp, int attackRate, String name, Flyable flyable) {
        super(hp, attackRate, name, flyable); // 부모 클래스의 매개변수 생성자를 호출, 반드시 생성자 첫 줄에 super를 사용해야 한다
        System.out.println("자몽자몽(매개변수 생성자)");
    }

    @Override
    public void attack() {  // 광역 딜
        System.out.println(this.getName() + "이(가) 광역 불장판 공격을 시전합니다~");
    }

    //public void attack(Charizard targetPokemon){  // 쩜사
    public void attack(Pokemon targetPokemon){  // 쩜사
        System.out.println(this.getName() + "이(가) 플레임 화염공격을 "+ targetPokemon.getName()  +"에게 시전 합니다");
        targetPokemon.setHp(targetPokemon.getHp()-this.getAttackRate());
        if(targetPokemon.getHp() <= 0)
            System.out.println(targetPokemon.getName() + " RIP~");
        else
            System.out.println(targetPokemon.getName() + "의 체력이 " + targetPokemon.getHp()+"으로 감소했습니다!");
    }

//    @Override
//    public void fly() {
//        System.out.println(this.getName() + "이(가) 날개로 하늘을 날아갑니다~");
//    }
ma
//    public void attack(Pikachu targetPokemon){  // 쩜사
//        System.out.println(this.getName() + "이(가) 플레임 화염공격 합니다");
//    }
}
