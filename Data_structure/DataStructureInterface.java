package Data_structure;

public interface DataStructureInterface<T> {
  void add(T element); // 데이터 추가
  T remove();          // 데이터 제거
  boolean isEmpty(); // 비어있는지 확인
}
