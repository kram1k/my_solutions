  import 'dart:io';

  int getSum(dog, collar, n, i_plus) {
    int res = 0;
    for(int i = 0; i < n; i++){
      int diff = collar[i] - dog[i_plus];
      if (diff < 0) {
        res += 0;
      } else if (diff < 100) {
        num re = diff ~/ 2;
        res += re.toInt();
      } else {
        res += 30;
      }
    }
    return res;
  }

  List<int> calculateBestStart(dogs, collars, n){
    int best_start = 1;
    List<int> dogs_x2 = dogs + dogs;
    int min_diss = 99999999999;
    for (int i = 0; i < n; i++){
      int diss = getSum(dogs_x2, collars, n, i);
      if (diss < min_diss){
        min_diss = diss;
        best_start = i + 1;
      }
    }
    List<int> res = [best_start, min_diss];
    return res;
  }

  void main(){
    var reader = stdin;
    int n = int.parse(reader.readLineSync() ?? ' ');
    List<String> dog_str = reader.readLineSync()!.split(" ");
    List<String> collar_str = reader.readLineSync()!.split(" ");
    List<int> dog = dog_str.map(int.parse).toList();
    List<int> collar = collar_str.map(int.parse).toList();

    List<int> query = calculateBestStart(dog, collar, n);
    int res = query[0];
    int w = query[1];
    print('${res} ${w}');
  }