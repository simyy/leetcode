/*
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Analysis:
change all chars to lower letters, and jump to next char when it is not char, then cmp tow char until uneque.
*/

class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0; 
        int r = s.length()-1;
        while(l < r) {
            if (!isalnum(s[l])) 
                l++;
            else if (!isalnum(s[r])) 
                r--;
            else if (tolower(s[l++])!=tolower(s[r--])) 
                return false;
            }
        }
        return true;
    }
};
