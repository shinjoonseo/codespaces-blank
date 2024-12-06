package Data_structure;

public class MazeSearch {
  
  private static int[][] move = {{0,1},{1,0},{-1,0},{0,-1}};

  private static boolean isValid (int[][] maze, int x, int y) {
    return x >= 0 && y >= 0 && x< maze.length && y < maze[0].length && maze[x][y] == 0;
  }

  public static boolean DFS (int[][] maze, int startX, int startY, int endX, int endY) {
    DataStructureInterface<int[]> stack = new MyStack<>();
    stack.input(new int[]{startX, startY}); // 시작 지점
    maze [startX][startY] = 2;

    while (!stack.isEmpty()) {
      int[] current = stack.output();
      int currentX = current[0];
      int currentY = current[1];

      if (currentX == endX && currentY == endY) {
        System.out.println("DFS미로의 경로: ");
        stack.entireprint();
        return true;
      }
    }
    return false;
  }
  public static boolean BFS(int[][] maze, int startX, int startY, int endX, int endY) {
    DataStructureInterface<int[]> queue = new MyQueue<>();
    queue.input(new int[]{startX, startY});
    maze [startX][startY] = 2;

    while (!queue.isEmpty()) {
      int[] current = queue.output();
      int currentX = current[0];
      int currentY = current[1];

      if (currentX == endX && currentY == endY) {
        System.out.println("BFS미로의 경로: ");
        //도착 지점까지의 경로 복원
        while (maze[currentX][currentY] != 2) { // 도착지점까지 반복 
          System.out.print("[" + currentX + ", " + currentY + "] ");

          for (int[] search : move) {
            int newX = currentX + search[0];
            int newY = currentY + search[1];
            // 자기 자신보다 1 작으면
            if (newX >= 0 && newY >= 0 && newX < maze.length && newY < maze[0].length&& maze[newX][newY] == maze[currentX][currentY] - 1) { 
              currentX = newX;
              currentY = newY;
              break;
            }
          }
        }
        //출발지점 출력
        System.out.print("[" + currentX + ", " + currentY + "]");
        System.out.println();
        return true;
      }
      for (int[] search : move) {
        int newX = currentX + search[0];
        int newY = currentY + search[1];

        if (isValid(maze, newX, newY)) {
          queue.input(new int[]{newX, newY});
          maze[newX][newY] = maze[currentX][currentY] + 1;
        }
      }
    }
    return false; // 경로가 없음
  }
  public static void main(String[] args) {
    // 미로 배열 설정 (0은 이동 가능, 1은 벽)
    int[][] maze = {
        {0, 1, 0, 0, 0},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 1, 0},
        {1, 1, 0, 0, 0},
        {0, 0, 0, 1, 0}
    };

    // 시작점과 도착점 설정
    int startX = 0, startY = 0; // 시작점 좌표
    int endX = 4, endY = 4;     // 도착점 좌표

    // BFS를 호출해 경로를 탐색
    boolean pathFound = BFS(maze, startX, startY, endX, endY);

    // 결과 출력
    if (pathFound) {
        System.out.println("\n경로를 성공적으로 찾았습니다!");
    } else {
        System.out.println("\n경로를 찾을 수 없습니다.");
    }

}
}



