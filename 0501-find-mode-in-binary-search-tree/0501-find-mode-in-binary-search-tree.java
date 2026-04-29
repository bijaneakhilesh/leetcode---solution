/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int[] findMode(TreeNode root) {
        int[] state = new int[]{Integer.MIN_VALUE, 0, 0, 0}; 
        inorder(root, state, null);
        int[] modes = new int[state[3]];
        state = new int[]{Integer.MIN_VALUE, 0, state[2], 0};
        inorder(root, state, modes);
        return modes;
    }
    private void inorder(TreeNode node, int[] state, int[] modes) {
        if (node == null) return;
        inorder(node.left, state, modes);
        if (node.val != state[0]) {
            state[0] = node.val;
            state[1] = 0;
        }
        state[1]++;
        if (state[1] > state[2]) {
            state[2] = state[1];
            state[3] = 1;
            if (modes != null) modes[0] = state[0];
        } else if (state[1] == state[2]) {
            if (modes != null) modes[state[3]] = state[0];
            state[3]++;
        }
        inorder(node.right, state, modes);
    }
}