import uuid

def get_mac():
    MAC = hex(uuid.getnode())
    print(MAC)
    MAC = MAC[2:]
    mac_list = [MAC[i:i+2]for i in range(0, len(MAC), 2)]
    mac_string = ':'.join(mac_list)
    return(mac_string)

def main():
    get_mac()

if __name__ == "__main__":
    main()