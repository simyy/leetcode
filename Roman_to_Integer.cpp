/*
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

Analysis:
利用hash来实现o(1)的查找，需要注意的是罗马数字的变化规律：
1.0-3 I II III 每次都是增加相同的
2. 4-6 IV V VI, 其中 IV=V-I，VI = V+I，那么需要注意4的时候是5-1得到的
3. 7-8 VII VIII 还是正常的
4. 9 XI ，其中XI=X-I，与2中情况一样
*/

#include <iostream>
#include <string.h>
#include <map>
using namespace std;

class Solution {
public:
    int  romanToInt(string s) {
        char symbol[7] = {'I','V','X','L','C','D','M'};
        map<char, int> table;
        table['I'] = 1;
        table['V'] = 5;
        table['X'] = 10;
        table['L'] = 50;
        table['C'] = 100;
        table['D'] = 500;
        table['M'] = 1000;
        int i = 0;
        int sum = 0;
        int len = s.length(); 
        while (i < len - 1) {
            if (table[s[i]] >= table[s[i+1]])
                sum += table[s[i]];
            else
                sum -= table[s[i]];
            i++;
        }
        sum += table[s[i]];
        return sum;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    int r = a.romanToInt("IV");
    cout<<r<<endl;

    return 0;
}
