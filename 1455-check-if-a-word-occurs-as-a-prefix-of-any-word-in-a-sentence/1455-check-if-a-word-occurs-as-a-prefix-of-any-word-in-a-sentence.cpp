class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        int ans = 1;
        string temp = "";
        for(char &ch : sentence)
        {
            if(ch == ' ')
            {
                ans++;
                temp = "";
            }
            else 
            {
                temp += ch;
                if(temp == searchWord)
                    return ans;
            }
        }
        return -1;
    }
};