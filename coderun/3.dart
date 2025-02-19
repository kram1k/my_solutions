import 'dart:io';

void main(){
  int len = int.parse(stdin.readLineSync()!);
  String input = stdin.readLineSync()!;
  List<String> parts = input.split(' ');
  List<int> array = [];

  for (String part in parts) {
    array.add(int.parse(part));
  }

  int res = 0;
  for (int i = 0; i < len; i++){
    res += array[i];
  }

  print(100 ~/ res);
}