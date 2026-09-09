class Solution {
    public int search(int[] nums, int target) {

        int l = 0;
        int r = nums.length-1;

        while(l< r){
            int median = l + ((r-l)/2);

            if(nums[median] > nums[r]){
                l = median+1;
            }
            else{
                r = median;
            } 
        }

        int pivot = l;
        int binarySerach1 = binarySearch(0,pivot-1,nums,target);
        if(binarySerach1 != -1) return binarySerach1;
        return binarySearch(pivot, nums.length-1,nums, target); 
        
    }

    public int binarySearch(int l,int r,int nums[],int targ){

        while(l <= r){
            int mid = l + ((r-l)/2);
            if(nums[mid] > targ){
                r = mid -1;
            }
            else if(nums[mid] < targ){
                l = mid+1;
            }
            else if (nums[mid] == targ){
                return mid;
            }
        }
    return -1;
    }
}
