public abstract class Pokemon {
    private int hp;
    private int attackRate;
    private String name;

    Flyable flyable;

    public Pokemon() {  // default constructor
        hp = 1;
        attackRate = 1;
        name = "무명";
    }

    public Pokemon(int hp, int attackRate, String name, Flyable flyable) {  // parameter constructor
        this.hp = hp;
        this.attackRate = attackRate;
        this.name = name;
        this.flyable = flyable;
    }

    public <T> void  performFly(T flyingAbility){  // generic method
        this.flyable.fly(this);
        System.out.println(this.getName() + "의 비행 능력 : " + flyingAbility);
    }

    public int getHp() {
        return hp;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }

    public int getAttackRate() {
        return attackRate;
    }

    public void setAttackRate(int attackRate) {
        this.attackRate = attackRate;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

//    public void attack(){
//        System.out.println("공격을 시전합니다!");
//    }

    public abstract void attack();  // 추상 메서드 (반드시 자식 클래스에서 오버라이딩 해야 한다)
}
