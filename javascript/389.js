/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    let result = [];
    let sArr = Array.from(s).sort();
    let tArr = Array.from(t).sort();

    let i = 0;
    let j = 0;
    while (j < tArr.length) {
        if(i >= sArr.lentgh || sArr[i] != tArr[j]) {
            result.push(tArr[j]);
            j++;
        } else {
            i++;
            j++;
        }
    }
    return result.join('')
};