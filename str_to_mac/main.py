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

if __name__ == '__main__':
    while True:
        ask_usr_command = int(input("[1] str to mac\n[99] Exit\n    >>  "))
        if (ask_usr_command == 1):
            ask_usr_str = input("[+] Input str to convert to mac address : ")
            ___ =  str_to_mac(ask_usr_str)
            print(___)
            continue
        if (ask_usr_command == 99):
            print("Goodbye friend !\n")
            break
        else:
            print("Uh oh... What did you even try to type ?\n")