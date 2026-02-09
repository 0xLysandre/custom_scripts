def str_to_mac(address:str):
    if (len(address) != 17):
        return 1
    
    length = len(address)
    i = 0

    list_str_mac_address = []

    while (i < length):
        if (address[i] == '-'):
            list_str_mac_address.append(':')

        if not (address[i] == '-'):
            list_str_mac_address.append(address[i])

        i += 1
    
    return ''.join(list_str_mac_address)

print(str_to_mac('24-EC-99-CA-D8-88'))