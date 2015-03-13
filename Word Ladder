/*
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
*/

#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        unordered_map<string, int> dis; // store the distance from start to the current word
        queue<string> q; // FIFO for bfs purpose
        dis[start] = 1;
        q.push(start);
        while (!q.empty()) {
            string word = q.front(); q.pop();
            if (word == end) break;
            for (int i = 0; i < word.size(); i++) {
                for (int j = 0; j < 26; j++) {
                    string newWord = word;
                    newWord[i] = 'a' + j;
                    if (dict.count(newWord) > 0 && dis.count(newWord) == 0) {
                        dis[newWord] = dis[word] + 1;
                        q.push(newWord);
                    }
                }
            }
        }
        if (dis.count(end) == 0) return 0;
        return dis[end];
    }
};

int main(int argc, char** argv)
{
    //string start = "hit";
    //string end = "cog";
    //unordered_set<string> dict = {"hot","dot","dog","lot","log"};
    string start = "qa";
    string end = "sq";
    unordered_set<string> dict = {"si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"};

    Solution a;
    int r = a.ladderLength(start, end, dict);
    cout<<r<<endl;

    return 0;
}
