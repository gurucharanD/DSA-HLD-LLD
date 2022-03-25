function decimalToBinary(decimal,binary) {
    if (decimal == 0) {
        return binary;
    }

    binary = decimal%2+binary

    return decimalToBinary(decimal/2,binary);
}