class Solution {
private:
    std::string postBackspace(const std::string& str) {
        std::string stack = "";
        for (char c : str) {
            if (c == '#') {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            } else {
                stack.push_back(c);
            }
        }
        return stack;
    }

public:
    bool backspaceCompare(std::string s, std::string t) {
        return postBackspace(s) == postBackspace(t);
    }
};
