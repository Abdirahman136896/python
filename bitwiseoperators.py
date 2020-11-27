#complement(tilde operator)
print(~12)#12 is 00001100 in binary and its complement is 11110011.Using 2's complement 11110011 is -13
#bitwise AND
print(12 & 13) #12 - 00001100
               #13 - 00001101
                    #00001100 which corresponds to 12 in decimal format .We get these because AND is only true(1) when
# both the upper value is 1 and the value below it is 1
#bitwise OR
print(12 | 13) #12 - 00001100
               #13 - 00001101
                    #00001101 which corresponds to 13 in decimal format .We get these because OR is only false(0) when
# both the upper value is 0 and the value below it is 0
#xor operator
print(12 ^ 13) #12 - 00001100
               #13 - 00001101
                    #00000001#which corresponds to 1 in decimal format .We get these because XOR is only true(1) when
# both the upper value and the value below has odd number of 1's.
#left shift operator
print(10 << 2) #10 - 1010.000 shift two bits after the decimal points into the side of the whole number part therefore
# 101000.0 which corresponds to 40 in decimal format
#right shift operator
print(10 >> 2) #10 - 1010 shift two bits from the right end side ,it loses the 1 and 0 bits from the right therefore
# 10 which corresponds to 2 in decimal format.