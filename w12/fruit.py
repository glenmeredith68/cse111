def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    fruit_list.append('orange')
    print(fruit_list)
    apple_index = fruit_list.index('apple')
    fruit_list.insert(apple_index, 'cherry')
    print(fruit_list)
    fruit_list.pop(fruit_list.index('banana'))
    print(fruit_list)
    print(fruit_list.pop())
    print(fruit_list)
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)


if __name__ == '__main__':
    main()