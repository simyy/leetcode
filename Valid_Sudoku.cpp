/*
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules:http://sudoku.com.au/TheRules.aspx.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Analysis:
利用set去重复情况
*/


class Solution {

public:

    bool isValidSudoku(vector<vector<char>>& board) {

        for (int i = 0; i < 9; ++i) {

            set<char> row;

            set<char> column;

            set<char> box;

            for (int j = 0; j < 9; ++j) {

                pair<std::set<int>::iterator,bool> ret;

                if (board[i][j] != '.' && row.insert(board[i][j]).second == false) 

                    return false;

                if (board[j][i] != '.' && column.insert(board[j][i]).second == false)

                    return false;

                int h = 3*(i/3) + j/3;

                int k = 3*(i%3) + j%3;

                if (board[h][k] != '.' && box.insert(board[h][k]).second == false)

                    return false;

            }

        }

        return true;

    }

};
