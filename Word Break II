/*
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <utility>
using namespace std;

struct node
{
    bool flag;
    vector<pair<int, int>> list;
    node() {
        flag = false;
    }
};


class Solution {
public:
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        vector<struct node> dp;
        int len = s.length();
        for (int i =0 ;i <= len; i++) {
            struct node p;
            dp.push_back(p);
        }
        dp[len].flag = true;
        for (int i = len-1; i >= 0; i--) {
            for (int j = i; j < len; j++) {
                string str = s.substr(i, j-i+1);
                if ((dict.find(str) != dict.end())&&(dp[j+1].flag)) {
                    if (dp[i].flag == false)
                        dp[i].flag = true;
                    dp[i].list.push_back(make_pair(i, j));
                }
            }
        }
        if (dp[0].flag == true)
            cout<<"true"<<endl;
        else
            cout<<"false"<<endl;
        for (int i = 0; i < dp.size(); i++) {
            if (dp[i].flag = true){
                for ( int j = 0; j < dp[i].list.size(); j++ ) {
                    cout<<dp[i].list[j].first<<"\t"<<dp[i].list[j].second<<endl;
                    cout<<s.substr(dp[i].list[j].first, dp[i].list[j].second-dp[i].list[j].first+1)<<endl;
                }
            }
        }
        
        vector<string>* x = new vector<string>();
        if (dp[0].flag == true) {
            vector<pair<int, int>> tmp;
            vector<string> v;
            string str = "";

            for (int i = 0; i < dp[0].list.size(); i++) {
                tmp.push_back(dp[0].list[i]);
                v.push_back(str);
            }

            while (!tmp.empty()) {
                pair<int, int> a = tmp.back();
                tmp.pop_back();

                str = v.back();
                v.pop_back();
                
                if (a.first == 0){
                    str = s.substr(a.first, a.second - a.first + 1);
                }
                else {
                   str += " " + s.substr(a.first, a.second - a.first + 1); 
                }
                for (int i = 0; i < dp[a.second+1].list.size(); i++ ){
                   tmp.push_back(dp[a.second+1].list[i]); 
                   v.push_back(str);
                }
                if (a.second == len - 1){
                    cout<<"a.second:"<<a.second<<"\t"<<"len-1:"<<(len-1)<<endl;
                    x->push_back(str);
                    //v.pop_back();
                    //tmp.pop_back();
                    //cout<<str<<endl;
                }
            }
        }

        return *x; 
    }
};

int main(int args, char** argv)
{
    string s = "aaaaaaa";
    unordered_set<string> dict;
    dict.insert("aaaa");
    dict.insert("aa");
    dict.insert("a");

    vector<string> res;
    Solution a;
    res = a.wordBreak(s, dict);
    cout<<"answer: "<<endl;
    for (int i = 0; i < res.size(); i++) {
        cout<<res[i]<<endl;
    }

    return 0;
}
