'''
Lesson 28 - Main block
main block
__name__
__file__
'''
def create_test_file():
    with open('test_file.py', 'w') as file:
        file.write('''
def main():
    print(__file__)
    print(f'__name__ = {__name__}')

if __name__ == '__main__':
    main()
''')

def main():
    print(__file__)
    print(f'__name__ = {__name__}')
    create_test_file()
    import test_file
    test_file.main()

if __name__ == '__main__':
    main()
