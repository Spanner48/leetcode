/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let res_arr = [];

    for (i = 1; i <= n; i++) {
        let temp_str = ''

        if (i % 3 == 0) {
            temp_str += 'Fizz'
        }
        if (i % 5 == 0) {
            temp_str += 'Buzz'
        }
        if (temp_str == '') {
            temp_str += [i].toString()
        }
        res_arr.push(temp_str)
    }
    return res_arr
};