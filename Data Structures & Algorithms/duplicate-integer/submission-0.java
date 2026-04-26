class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> myset = new HashSet <Integer>();

        for (int item : nums){
            if (myset.contains(item)){
                    return true;
            }

            else{
                myset.add(item);
            }
        }
        return false;
    }
}
