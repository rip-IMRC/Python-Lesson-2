def process_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    odd_squares = [x for x in squares if x % 2 != 0]
    even_squares = [x for x in squares if x % 2 == 0]
    print("Odd Squares:", odd_squares)
    print("Even Squares:", even_squares)
process_squares(1, 10)