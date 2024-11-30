public class Wings implements Flyable{
    @Override
    public void fly(Pokemon p) {
        //System.out.println(this.getName() + "날개로 하늘을 날아갑니다~");
        System.out.println(p.getName() + "이(가) 날개로 하늘을 날아갑니다~");
    }
}
