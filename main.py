def main():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    plain_text = get_plain_text()
    offset = get_offset()
    cipher_text = ''
    for plain in plain_text:
        _index = 0
        is_upper = False
        if plain.isdigit():
            cipher_char = numbers[(numbers.index(plain)+offset)%10]
        else:
            if plain.isupper():
                plain = plain.lower()
                is_upper = True
            cipher_char = alphabets[(alphabets.index(plain)+offset)%26]

        if is_upper:
            cipher_char = cipher_char.upper()
            
        cipher_text += cipher_char

    print('密文: {}'.format(cipher_text))
# 明文    
def get_plain_text():
    plain_text = None
    while True:
        plain_text = input('明文(限英數): ')
        if plain_text.isalnum():
            break
        else:
            print('明文格式錯誤請重新輸入')

    return plain_text

# 偏移量
def get_offset():
    offset = None
    while True:
        offset = input('偏移量(1-26): ')
        if offset.isdigit() and int(offset)>=1 and int(offset)<=26:
            break
        else:
            print('偏移量格式錯誤請重新輸入')

    return int(offset)

if __name__ == '__main__':
    main()