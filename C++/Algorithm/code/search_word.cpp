//
// Created by bright on 2022/1/20.
/* Demo Description: */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int d[4][2] = {{-1, 0},
               {0,  1},
               {1,  0},
               {0,  -1}};
int m, n;
vector<vector<bool>> visited;

bool intArea(int x, int y) {
    return x >= 0 && x < m && y >= 0 && y < n;
}

bool searchWord(const vector<vector<char>> &board, const string &word, int index, int startx, int starty) {
    if (index == word.size() - 1) {
        return word[index] == board[startx][starty];
    }

    if (word[startx][starty] == word[index]) {
        visited[startx][starty] = true;
        for (int i =0; i<4; i++) {
            int newx = startx + d[i][0];
            int newy = starty + d[i][1];
            if (intArea(newx, newy) && !visited[newx][newy] && searchWord(board, word, index + 1, newx, newy))
            return true;
        }
        visited[startx][starty] = false;
    }

    return false;
}

bool exist(vector<vector<char>> &board, string word) {
    m = board.size();
    assert(m > 0);
    n = board[0].size();
    assert(n > 0);

    visited = vector<vector<bool>>(m, vector<bool>(n, false));

    // 遍历每个可行的起始点
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (searchWord(board, word, 0, i, j))
                return true;
        }
    }

    return false;
}


