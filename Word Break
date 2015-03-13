/*
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
*/


#include <iostream>
#include <unordered_set>
#include <string>
#include <queue>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        if (BFS(s, dict))
            return true;
        return false;
    }

    bool BFS(string s, unordered_set<string> &dict) {
        queue<int> bfs;
        unordered_set<int> visited;

        bfs.push(0);

        while(bfs.size() > 0)
        {
            int start = bfs.front();
            bfs.pop();

            if (visited.find(start) == visited.end()) 
            {
                visited.insert(start);
                for (int i = start; i < s.size(); i++)
                {
                    string word(s, start, i - start + 1);
                    if (dict.find(word) != dict.end())
                    {
                        bfs.push(i+1);
                        if (i+1 == s.size())
                            return true;
                    }
                }
            }
        }
        return false;
    }

    bool DP(string s, unordered_set<string> &dict) {
        for (int i=0; i<s.length();) {
            int j = 1; 
            int flag = 0;
            for (; j<s.length()-i+1; ++j) {
                if (dict.find(s.substr(i, j)) == dict.end())
                    continue;
                else {
                    flag = 1;
                    break;
                }   
            }
            if (flag == 1) {
                if (j == s.length() - i)
                    return true;
                else{
                    flag = 0;
                    i += j;
                }
            }
            else
               return false; 
        }
        return false; 
    }

    bool wordBreak(string s, int i, unordered_set<string> &dict) {
        
    }
};

int main(int argc, char** argv)
{
    unordered_set<string> x;
    x.insert("aaaa");
    x.insert("aaa");
    Solution* p;
    //bool s = p->wordBreak("helloworld", x);
    bool s = p->wordBreak("aaaaaaa", x);
    if (s)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    return 0;
}
