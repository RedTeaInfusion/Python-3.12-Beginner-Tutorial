'''
Lesson 29 - Annotation
annotation
__annoatations__
__doc__
global
'''
largest_area = 0

def greet(name: str) -> str:
    '''Greet a person'''
    return f'Hello {name}'

def triangle_area(base: float, height: float) -> float:
    global largest_area
    area: float = base * height / 2
    if area > largest_area:
        largest_area = area

    return area

def main():
    print(greet('Red'))
    print(greet.__annotations__)
    print(greet.__doc__)

    print(triangle_area(5.5, 2.3))
    print(triangle_area.__annotations__)
    print(triangle_area(4,8))
    print(largest_area)

if __name__ == '__main__':
    main()
