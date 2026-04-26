class Solution {
    public boolean isPalindrome(String s) {
        
    
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        s = s.toLowerCase();

        int p1 = 0;
        int p2 = s.length()-1;
        boolean cond = true;

        while (p1 < p2){
            cond = (s.charAt(p1) == s.charAt(p2)) && cond;
            p1++;
            p2--;
        }

        return cond;

    }
}
