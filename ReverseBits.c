/*
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
*/

uint32_t reverseBits(uint32_t n) {
    uint32_t a = 1;
    uint32_t r = 0;
    uint32_t i;
    for (i = 0; i < 32; i++) {
       r <<= 1;
       r ^= a & n;
       n >>= 1;
    }
    return r;
}
