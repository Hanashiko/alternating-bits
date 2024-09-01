def hasAlternatingBits(n: int) -> bool:
    binary_n: str = f"{n:b}"
    for i in range(len(binary_n)-1):
        if binary_n[i] == binary_n[i + 1]:
            return False
    return True

def main() -> None:
    print(hasAlternatingBits(5))
    print(hasAlternatingBits(7))
    print(hasAlternatingBits(11))
    
if __name__ == "__main__":
    main()