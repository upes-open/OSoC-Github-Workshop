def is_magic_number(n):
    while n > 9:
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        n = digit_sum
    return n == 1

num1 = 1234  
num2 = 123  

print(f"{num1} is a magic number: {is_magic_number(num1)}")
print(f"{num2} is a magic number: {is_magic_number(num2)}")