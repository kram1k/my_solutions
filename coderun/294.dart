import 'dart:io';

void main() {

  var reader = stdin;
  int n = int.parse(reader.readLineSync() ?? ' ') ;
  List<String> arr = stdin.readLineSync()!.split(" ");
  int sum = 0;
  Set<int> last_arr = {};

  bool isLastArr(Set lst, int val){
    if(lst.contains(val)){
      return false;
    }
    return true;
  }

  for (int i = 0; i < n; i++){
    int x = int.parse(arr[i]);
    if(i == 0){
      sum += x;
      last_arr.add(x);
    } else {
      int y = int.parse(arr[i-1]);
      if(i >= 1 && isLastArr(last_arr, x)){
        last_arr.add(x);
        sum += x;
      }
    }
  }

  print(sum);
}
