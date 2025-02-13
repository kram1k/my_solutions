import 'dart:io';

int countOverpraisedDevelopers(String path) {
  int x = 0;
  int y = 0;
  Map<String, int> visited = {};
  String startPoint = "$x,$y";
  visited[startPoint] = (visited[startPoint] ?? 0) + 1;

  for (int i = 0; i < path.length; i++) {
    switch (path[i]) {
      case 'U':
        y += 1;
        break;
      case 'D':
        y -= 1;
        break;
      case 'R':
        x += 1;
        break;
      case 'L':
        x -= 1;
        break;
    }
    String currentPosition = "$x,$y";
    visited[currentPosition] = (visited[currentPosition] ?? 0) + 1;
  }

  int overpraisedCount = 0;
  visited.forEach((key, value) {
    if (value > 1) {
      overpraisedCount++;
    }
  });
  return overpraisedCount;
}
void main(){
  String chars = stdin.readLineSync() ?? '';
  print(countOverpraisedDevelopers(chars));

}