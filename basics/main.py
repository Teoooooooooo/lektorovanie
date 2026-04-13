def main() -> None:
    try:
        # premenné
        meno: str = "Anna"
        vek: int = 15

        print("Premenné:")
        print("Meno:", meno)
        print("Vek:", vek)

        # operácie
        a: int = 10
        b: int = 3

        print("\nOperácie:")
        print("a + b =", a + b)
        print("a - b =", a - b)
        print("a * b =", a * b)
        print("a / b =", a / b)
        print("a // b =", a // b)
        print("a % b =", a % b)

        # funkcie
        def pozdrav(meno: str) -> str:
            return f"Ahoj {meno}"

        def sucet(x: int, y: int) -> int:
            return x + y

        print("\nFunkcie:")
        print(pozdrav(meno))
        print("Súčet 5 + 7 =", sucet(5, 7))

    except Exception as e:
        print("Chyba:", str(e))
    
if __name__ == "__main__":
    main()
    
    
    
    
# premenné
# if-else
# for loop
# while loop