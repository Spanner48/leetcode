/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    let funcLen = functions.length

    if (funcLen == 0) {
       return function(x) {
            return x
            }
    } else {
        return function(x) {
            var res = x
            for (let i = funcLen - 1; i >= 0; i--) {
                res = functions[i](res)
            }
            return res
        }
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */