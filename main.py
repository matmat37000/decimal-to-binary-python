hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def main() -> None:
    dec = decimal_to_hexa(58)
    print(dec)
    return 

def decimal_to_binary(num: int) -> int:
    base: int = 2
    binary: list = []
    while num != 0:
        num, quotient = divmod(num, base)
        binary.insert(0, str(quotient))
    return int(''.join(binary))

def decimal_to_hexa(num: int) -> str:
    base: int = 16
    binary: list = []
    while num != 0:
        num, quotient = divmod(num, base)
        binary.insert(0, hexa[quotient])
    return ''.join(binary)

if __name__ == '__main__':
    main()