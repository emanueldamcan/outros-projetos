def ramanujan_pi(iterations, precision):
    scale = 10 ** precision
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    sigma_sum = 0
    for k in range(iterations):
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = (factorial(k) ** 4) * (396 ** (4 * k))
        term = (num * scale) // den
        sigma_sum += term
    scaled_sqrt_8 = (8 * (scale**2))**0.5
    multiplier = scaled_sqrt_8 // 9801
    pi_scaled = (scale ** 3) // (multiplier * sigma_sum)
    pi_str = str(pi_scaled)
    return pi_str[0] + pi_str[1:precision]
digits = 99
results = ramanujan_pi(3, digits)
print(results)