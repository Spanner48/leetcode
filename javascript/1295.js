/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let even_cnt = 0

    for (let i = 0; i < nums.length; i++) {
        cnt_digits = nums[i].toString().length

        if (cnt_digits % 2 == 0) {
            even_cnt += 1
        }
    }
    return even_cnt
};