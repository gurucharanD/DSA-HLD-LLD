function isPalindrome(testString) {

    let characters = testString.split('');
    let startIndex = 0;
    let lastIndex = characters.length - 1;

    while (startIndex <= lastIndex) {
        if (characters[startIndex] == characters[lastIndex]) {
            startIndex++
            lastIndex--
        } else {
            return false
        }

    }
    return true

}

console.log(isPalindrome('abcsdba'))