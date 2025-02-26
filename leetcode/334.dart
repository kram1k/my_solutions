class Solution {
  bool increasingTriplet(List<int> nums) {
    int n1 = 100000000;
    int n2 = 100000000;
    for (int n in nums) {
      if (n > n2) {
        return true;
      }
      if (n <= n1) {
        n1 = n;
      } else if (n <= n2) {
        n2 = n;
      }
    }
    return false;
  }
}
