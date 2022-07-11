from typing import Callable


def fizz_buzz(n: int) -> str:
    def fizz(buzzer: Callable) -> Callable:
        if n % 3 == 0:
            return lambda str: "Fizz" + buzzer("")
        else:
            return buzzer

    def buzz() -> Callable:
        if n % 5 == 0:
            return lambda str: "Buzz"
        else:
            return lambda x: x

    return fizz(buzz())(str(n))


if __name__ == "__main__":
    for n in range(30):
        print(fizz_buzz(n))
