class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map <String, List<String> > myMap = new HashMap<>();
        List < List<String> > result = new ArrayList<>();

        for (String item : strs){

            char [] myarray = item.toCharArray();
            Arrays.sort(myarray);
            String temp = Arrays.toString(myarray);

            if (!myMap.containsKey(temp)){
                myMap.put(temp, new ArrayList<String>());
            }

            myMap.get(temp).add(item);
        }

        for (String i : myMap.keySet()){
            result.add(myMap.get(i));
        }

        return result;

    }
}
