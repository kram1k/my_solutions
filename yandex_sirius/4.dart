import 'dart:io';

void main() {
  final List<String> firstLine = stdin.readLineSync()!.split(' ');
  final int n = int.parse(firstLine[0]);
  final int k = int.parse(firstLine[1]);

  final List<int> weights = stdin.readLineSync()!.split(' ').map(int.parse).toList();

  int trips = 0;
  int count = 0;
  for (int weight in weights) {
    if (weight > k) {
      print('Impossible');
      return;
    }
    trips++;
    count += weight;
  }
  trips = (count + k - 1) ~/ k;

  print(trips);
}
