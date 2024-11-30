class Attack<T>{
    private int damage;
    private String type;
    private T specialEffect;

    public Attack(int damage, String type, T specialEffect) {
        this.damage = damage;
        this.type = type;
        this.specialEffect = specialEffect;
    }
    public void execute(Pokemon target){
        System.out.println(target.getName()  +"에게 " + damage + "의 피해를 입힙니다! (공격 타입 : " + type + ")");
        if(specialEffect != null){
            System.out.println("특수 효과 : " + specialEffect);
        }
        target.setHp(target.getHp()-damage);
        if(target.getHp() <= 0)
            System.out.println(target.getName() + " RIP~");
        else
            System.out.println(target.getName() + "의 체력이 " + target.getHp()+"으로 감소!");
    }
}