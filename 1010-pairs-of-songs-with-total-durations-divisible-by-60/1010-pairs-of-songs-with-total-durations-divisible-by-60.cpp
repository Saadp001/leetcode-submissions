class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int count = 0;
        unordered_map<int, int>mp;
        for(int i = 0; i < time.size(); i++)
        {
            int val = abs(time[i] - 1200) % 60;
            cout << val << endl;
            if(mp.find(val) != mp.end())
                count += mp[val];
            mp[time[i] % 60]++;
        }
        return count;
    }
};