class Solution {
    public int uniqueXorTriplets(int[] nums) {
         int n = nums.length;
        BitSet seen = new BitSet();
        for (int x : nums) {
            seen.set(x);
        }
        HashSet<Integer> pairXor = new HashSet<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                pairXor.add(nums[i] ^ nums[j]);
            }
        }
        for (int px : pairXor) {
            for (int x : nums) {
                seen.set(px ^ x);
            }
        }
        return seen.cardinality();
    }
}