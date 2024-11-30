public class NoFly implements Flyable{
    @Override
    public void fly(Pokemon p) {
        System.out.println(p.getName() + "이(가) 하늘을 날수 없습니다!");
    }
}
