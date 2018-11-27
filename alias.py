
array = list


if __name__ == "__main__":

    def a_func(arr: array = []) -> None:
        return arr

    print(a_func(['a', 'b']))