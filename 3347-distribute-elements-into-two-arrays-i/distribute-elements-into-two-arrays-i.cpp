class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        int l = nums[0] , r = nums[1] , n = nums.size() , i;
        nums[1] *= -1;
        for (i = 2 ; i < n ; i++){
            if (l > r){
                l = nums[i];
            }
            else{
                r = nums[i];
                nums[i] *= -1;
            }
        }
        std::vector<int> res;
        for (i = 0 ; i < n ; i++){
            if (nums[i] > 0){
                res.push_back(nums[i]);
            }
        }
        for (i = 0 ; i < n ; i++){
            if (nums[i] < 0){
                res.push_back(-nums[i]);
            }
        }
        return res;
    }
};