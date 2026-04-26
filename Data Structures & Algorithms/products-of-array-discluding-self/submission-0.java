class Solution {
    public int[] productExceptSelf(int[] nums) {
        int myarray [] = new int [nums.length];

        for (int i = 0; i < nums.length; i++){
            int temp = 1;
            int pointer = -1;

            if (i == nums.length - 1){
                pointer = 0;    
            }

            else{
                pointer = i + 1;
            }

            while (i != pointer){
                temp *= nums[pointer];
                if (pointer == nums.length - 1){
                    pointer = 0;
                }

                else{
                    pointer++;
                }
            }

            myarray[i] = temp;
        }

        return myarray;
    }
}  
