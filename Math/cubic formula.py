import cmath
value_a = int(input("Type the first coefficient (cannot be 0): "))
value_b = int(input("Type the second coefficient: "))
value_c = int(input("Type the third coefficient: "))
value_d = int(input("Type the final coefficient: "))
value_B = value_b / value_a
value_C = value_c / value_a
value_D = value_d / value_a
def calculate_p(c, b):
    return c - (b**2/3)
value_p = calculate_p(value_C, value_B)
def calculate_q(d, c, b):
    return d - ((b*c)/3) + ((2*b**3)/27)
value_q = calculate_q(value_D, value_C, value_B)
def calculate_delta(q, p):
    return (q**2/4) + (p**3/27)
value_delta = calculate_delta(value_q, value_p)
def calculate_y(q, delta):
    sqrt_delta = cmath.sqrt(delta)
    block_positive = (-q/2) + sqrt_delta
    block_negative = (-q/2) - sqrt_delta
    cube_root_positive = block_positive ** (1/3)
    cube_root_negative = block_negative ** (1/3)
    return cube_root_positive + cube_root_negative
value_y = calculate_y(value_q, value_delta)
def calculate_x(y, b):
    return y - (b/3)
value_x = calculate_x(value_y, value_B)
print(value_x)