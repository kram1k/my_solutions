class Solution {
  bool canPlaceFlowers(List<int> flowerbed, int n) {
    int i = 0;
    List<int> f = [0] + flowerbed + [0];
    for (int i = 1; i <= f.length - 1; i++) {
      if (f[i] - 1 == 0 && f[i] == 0 && f[i + 1] == 0) {
        f[i] = 1;
        n -= 1;
      }
    }
    return n <= 0;
  }
}

void main() => print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1));
