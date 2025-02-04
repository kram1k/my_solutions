import 'dart:io';

void main() async {
  File inputFile = File("input.txt");
  List<String> content = await inputFile.readAsLines();
  int len = int.parse(content[0]);
  content.remove(content[0]);
  String str = content[0];
  content.remove(content[0]);
  content = content[0].split(' ');
  List<int> lst = [];
  for (final i in content){
    lst.add(int.parse(i));
  }
  int max_sec = lst[0];
  int index = 0;
  for (var i = 0; i < len - 1; i++){
    int second = lst[i + 1] - lst[i];
    if (max_sec <= second){
      max_sec = second;
      index = i + 1;
    }
  }
  File outputFile = File("output.txt");
  String res = str.substring(index, index + 1);
  await outputFile.writeAsString(res);
}