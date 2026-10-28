class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int ZeroCnt = 0, ZeroIdx = -1, prod = 1, n = nums.size();

        for(int i = 0; i < n; i++){
            if(nums[i] == 0){
                ZeroCnt++;
                ZeroIdx = i;
                if(ZeroCnt > 1) {
                    vector<int> temp(n, 0);
                    return temp;
                }
                continue;
            } 
            prod *= nums[i];
        }

        if(ZeroCnt == 1){
            vector<int> temp(n, 0);
            temp[ZeroIdx] = prod;
            return temp;
        }

        vector<int> ans(n);
        for(int i = 0; i < n; i++){
            ans[i] = prod / nums[i];
        }

        return ans;
    }
};