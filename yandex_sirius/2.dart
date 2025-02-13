import 'dart:io';

void main() {
  String input = stdin.readLineSync()!;
  List<int> numbers = input.split(' ').map(int.parse).toList();

  int totalRemoved = 0;

  while (true) {
    final groups = numbers.groupListsBy((num) => num);
    final newNumbers = <int>[];
    var removedInThisIteration = 0;

    for (var group in groups.values) {
      if (group.length >= 3) {
        removedInThisIteration += group.length;
      } else {
        newNumbers.addAll(group);
      }
    }

    if (removedInThisIteration == 0) {
      break;
    }

    totalRemoved += removedInThisIteration;
    numbers = newNumbers;
  }

  print(totalRemoved);
}

extension GroupByExtension<T> on Iterable<T> {
  Map<K, List<T>> groupListsBy<K>(K Function(T element) grouper) {
    final map = <K, List<T>>{};
    for (final element in this) {
      final key = grouper(element);
      map.update(key, (value) => value..add(element), ifAbsent: () => [element]);
    }
    return map;
  }
}