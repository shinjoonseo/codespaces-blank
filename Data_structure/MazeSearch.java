package Data_structure;

public class MazeSearch {

  private int[][] move = {{0,1},{1,0},{-1,0},{0,-1}};
  public static boolean DFS (int[][] maze, int startX, int startY, int endX, int endY) {
    DataStructureInterface<int[]> stack = new MyStack<>();
    stack.input(new int[]{startX, startY}); // 시작 지점
    maze [startX][startY] = 2;

    while (true) {
      int[] current = stack.output();
      int currentX = current[0];
      int currentY = current[1];

      if (currentX == endX && currentY == endY) {
        System.out.println("DFS미로의 경로: ");
        stack.entireprint();
        return true;
      }

    }
  }
  public static boolean BFS(int[][] maze, int startX, int startY, int endX, int endY) {
    DataStructureInterface<int[]> queue = new MyQueue<>();
    queue.input(new int[]{startX, startY});
    maze [startX][startY] = 2;

    while (true) {
      int[] current = queue.output();
      int currentX = current[0];
      int currentY = current[1];

      if (currentX == endX && currentY == endY) {
        System.out.println("BFS미로의 경로: ");
        queue.entireprint();
        return true;
      }
    }
  }
  private static boolean isValid (int[][] maze, int x, int y) {
    return 
  }

}



