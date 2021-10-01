function splitter(a) {
    letters = a.split('');
    for (let i = 0; i < letters.length - 1; i++) {
        if (letters[i] == letters[i + 1]) {
            letters.splice(i, 2);
            splitter(letters.join(''));
        }
    }
    return letters.join('');
}


console.log(splitter('bbabbaadd'))