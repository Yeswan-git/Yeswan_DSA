class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int n = arr.size();
        if (k < arr[0]){
            return k;
        }
        if (k > arr[n - 1]){
            return k + n;
        }
        int l = 0 , r = n - 1;
        while (l <= r){
            int mid = l + (r - l) / 2;
            int miss = arr[mid] - (mid + 1);
            if (miss < k){
                l = mid + 1;
            }
            else{
                r = mid - 1;
            }
        }
        int miss_at_r = arr[r] - (r + 1);
        return arr[r] + (k - miss_at_r);
    }
};