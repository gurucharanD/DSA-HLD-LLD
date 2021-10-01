for (i = 0; i < 10; i++) {
    var x = B[i];
    var twos |= ones & x;
    var ones ^= x;
    var not_threes = ~(ones & twos);
    var ones &= not_threes;
    var twos &= not_threes;
}