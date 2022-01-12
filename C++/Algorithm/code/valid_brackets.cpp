//
// Created by bright on 2022/1/12.
/* Demo Description: */

#include <iostream>
#include <string>
#include <stack>

bool isValid(string s) {
    std::stack<std::string> s;

    for (auto c: s) {
        if (c == '(' || c == '[' || c == '{') {
            s.push(c);
        } else {
            if (s.empty())
                return false;

            char ct = s.top();
            s.pop();

            char match;

            if (c == ')')
                match = '(';
            else if (c == ']')
                match = '[';
            else
                match = '{';

            if (match != ct)
                return false;
        }
    }

    if (s.empty())
        return true;
    return false;
}

