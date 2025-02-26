class Solution {
  List<int> productExceptSelf(List<int> nums) {
    List<int> res = List.generate(nums.length, (_) => 1);
    int prefix = 1;
    int postfix = 1;

    for (int i = 0; i < nums.length; i++) {
      res[i] = prefix;
      prefix *= nums[i];
    }

    for (int j = nums.length - 1; j >= 0; j--) {
      res[j] *= postfix;
      postfix *= nums[j];
    }

    return res;
  }
}

void main() {
  Solution a = Solution();
  print(a.productExceptSelf([1, 2, 3, 4]));
}
