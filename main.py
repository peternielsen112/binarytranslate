import sys

input = sys.argv[1]

#translation code
#numerals 0-64
if input == '0':
    print('0000000')
elif input == '1':
    print('0000001')
elif input == '2':
    print('0000010')
elif input == '3':
    print('0000011')
elif input == '4':
    print('0000100')
elif input == '5':
    print('0000101')
elif input == '6':
    print('0000110')
elif input == '7':
    print('0000111')
elif input == '8':
    print('0001000')
elif input == '9':
    print('0001001')
elif input == '10':
    print('0001010')
elif input == '11':
    print('0001011')
elif input == '12':
    print('0001100')
elif input == '13':
    print('0001101')
elif input == '14':
    print('0001110')
elif input == '15':
    print('0001111')
elif input == '16':
    print('0010000')
elif input == '17':
    print('0010001')
elif input == '18':
    print('0010010')
elif input == '19':
    print('0010011')
elif input == '20':
    print('0010100')
elif input == '21':
    print('0010101')
elif input == '22':
    print('0010110')
elif input == '23':
    print('0010111')
elif input == '24':
    print('0011000')
elif input == '25':
    print('0011001')
elif input == '26':
    print('0011010')
#capital letters and numbers 65 - 90
elif input == 'A' or '65':
    print('1000001')
elif input == 'B' or '66':
    print('1000010')
elif input == 'C' or '67':
    print('1000011')
elif input == 'D' or '68':
    print('1000100')
elif input == 'E' or '69':
    print('1000101')
elif input == 'F' or '70':
    print('1000110')
elif input == 'G' or '71':
    print('1000111')
elif input == 'H' or '72':
    print('1001000')
elif input == 'I' or '73':
    print('1001001')
elif input == 'J' or '74':
    print('1001010')
elif input == 'K' or '75':
    print('1001011')
elif input == 'L' or '76':
    print('1001100')
elif input == 'M' or '77':
    print('1001101')
elif input == 'N' or '78':
    print('1001110')
elif input == 'O' or '79':
    print('1001111')
elif input == 'P' or '80':
    print('1010000')
elif input == 'Q' or '81':
    print('1010001')
elif input == 'R' or '82':
    print('1010010')
elif input == 'S' or '83':
    print('1010011')
elif input == 'T' or '84':
    print('1010100')
elif input == 'U' or '85':
    print('1010101')
elif input == 'V' or '86':
    print('1010110')
elif input == 'W' or '87':
    print('1010111')
elif input == 'X' or '88':
    print('1011000')
elif input == 'Y' or '89':
    print('1011001')
elif input == 'Z' or '90':
    print('1011010')
#numerals 91-96
elif input == '91':
    print('1011011')
elif input == '92':
    print('1011100')
elif input == '93':
    print('1011101')
elif input == '94':
    print('1011110')
elif input == '95':
    print('1011111')
elif input == '96':
    print('1100000')
#lowercase letters and numbers 97 - 122
elif input == 'a' or '97':
    print('1100001')
elif input == 'b' or '98':
    print('1100010')
elif input == 'c' or '99':
    print('1100011')
elif input == 'd' or '100':
    print('1100100')
elif input == 'e' or '101':
    print('1100101')
elif input == 'f' or '102':
    print('1100110')
elif input == 'g' or '103':
    print('1100111')
elif input == 'h' or '104':
    print('1101000')
elif input == 'i' or '105':
    print('1101001')
elif input == 'j' or '106':
    print('1101010')
elif input == 'k' or '107':
    print('1101011')
elif input == 'l' or '108':
    print('1101100')
elif input == 'm' or '109':
    print('1101101')
elif input == 'n' or '110':
    print('1101110')
elif input == 'o' or '111':
    print('1101111')
elif input == 'p' or '112':
    print('1110000')
elif input == 'q' or '113':
    print('1110001')
elif input == 'r' or '114':
    print('1110010')
elif input == 's' or '115':
    print('1110011')
elif input == 't' or '116':
    print('1110100')
elif input == 'u' or '117':
    print('1110101')
elif input == 'v' or '118':
    print('1110110')
elif input == 'w' or '119':
    print('1110111')
elif input == 'x' or '120':
    print('1111000')
elif input == 'y' or '121':
    print('1111001')
elif input == 'z' or '122':
    print('1111010')
#if the character given is not recognized
else:
    print('Sorry, the number or character you have typed is not available to be translated at this time.')
