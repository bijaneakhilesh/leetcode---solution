class Solution {
    public int minimumDistance(int[] nums) {
        int n = nums.length;
        int ans = Integer.MAX_VALUE;
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        for (List<Integer> list : map.values()) {
            int size = list.size();
            if (size < 3) continue;
            for (int i = 0; i <= size - 3; i++) {
                int a = list.get(i);
                int c = list.get(i + 2);
                ans = Math.min(ans, 2 * (c - a));
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}