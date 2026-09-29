int romanToInt(char* s) {
    int values[256];
    values['I'] = 1;
    values['V'] = 5;
    values['X'] = 10;
    values['L'] = 50;
    values['C'] = 100;
    values['D'] = 500;
    values['M'] = 1000;

    int total = 0;
    int prev = 0;

    // Iterate from right to left
    for (int i = strlen(s) - 1; i >= 0; i--) {
        int curr = values[(unsigned char)s[i]];
        if (curr < prev) {
            total -= curr;  // subtraction case (IV, IX, etc.)
        } else {
            total += curr;
        }
        prev = curr;
    }

    return total;
}