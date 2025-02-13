import 'dart:io';

void main() {
  int k = int.parse(stdin.readLineSync()!);
  String word = stdin.readLineSync()!;
  int n = word.length;
  int ans = 0;

  for (int len = n; len >= 1; len--) {
    int count = 0;

    for (int i = 0; i <= n - len; i++) {
      if (isPalindrome(word, i, len)) {
        count++;
        i += len - 1;
      }
    }

    if (count >= k) {
      ans = len;
      break;
    }
  }

  print(ans);
}

bool isPalindrome(String str, int start, int length) {
  int end = start + length - 1;
  while (start < end) {
    if (str[start] != str[end]) return false;
    start++;
    end--;
  }
  return true;
}
