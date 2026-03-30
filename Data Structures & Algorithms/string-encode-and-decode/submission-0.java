class Solution {

    /*
        I - encode - List of strings, decode - string
        O - emcode - encoded string; decode() - List of strings
        C - None
        E - Empty list, empty strings

        Plan:

        encode()
        1. Instantiate a new StringBuilder object
        2. for str in strs:
            2.1 Get the length of the string
            2.2 Append the length, followed by a delimiter onto the sb(#)
            2.3 for char in str:
                2.3.1 Append each char to the sb
        return the sb

        decode()
        1. Instantiate a List of strings
        2. for char in strs:
            2.1 Read all the characters till #
            2.2 Convert to integer - x
            2.3 Instantiate a StringBuilder object
            2.4 for i in range(x + 1):
                2.4.1 Append ith character to the sb object
            2.5 Append the string to the List
        Return the list of strings
    */

    public String encode(List<String> strs) {
        StringBuilder encodedSb = new StringBuilder();
        for (String str: strs) {
            encodedSb.append(str.length()).append('#').append(str);
        }
        return encodedSb.toString();
    }

    public List<String> decode(String str) {
        List<String> strsList = new ArrayList<>();
        int i = 0;
        while(i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int n = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + n;
            strsList.add(str.substring(i, j));
            i = j;
        }
        return strsList;
    }
}
