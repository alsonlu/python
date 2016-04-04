def is_triangle(side_one, side_two, side_three):
    if side_one + side_two < side_three or side_one + side_three < side_two or side_two + side_three < side_one:
        print("No")
    else:
        print("Yes")

side_one = int(input("First side: "))
side_two = int(input("Second side: "))
side_three = int(input("Third side: "))

is_triangle(side_one, side_two, side_three)
