class Solution {
    public boolean isAnagram(String s, String t) {
        char [] myarray = s.toCharArray();
        char [] myarray2 = t.toCharArray();

        Arrays.sort(myarray);
        Arrays.sort(myarray2);

        String s2 = Arrays.toString(myarray);
        String t2 = Arrays.toString(myarray2);

        if (s2.equals(t2)){
            return true;
        }

        else{
            return false;
        }
    }
}
