class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int myarray [] = new int [k];

        Map <Integer, Integer> myMap = new HashMap<>();

        for (int item : nums){
            if (!myMap.containsKey(item)){
                myMap.put(item, 1);
            }

            else{
                myMap.put(item, myMap.get(item) + 1);
            }
        }

        for (int i = 0; i < k; i++){

            if (myMap.isEmpty()){
                break;
            }

            int max = (Collections.max(myMap.values()));
            int maxKey = 0;
            for (int key : myMap.keySet()){
                if (max == myMap.get(key)){
                    maxKey = key;
                }
            }

            myarray[i] = maxKey;
            myMap.remove(maxKey);
            
        }

        return myarray;
    }
}
