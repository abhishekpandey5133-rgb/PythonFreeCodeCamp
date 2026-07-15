def divide(a,b):
    result = a/b
    return result

print(divide(2,3))
print(divide(10,5))

# Now going to try TRY and EXCEPT funtion
# One thing is clear if we don't use the right except after the try expression it result in error

try:
    result = 10/0
except ValueError:
    print("This is Value Error")
#This except adding after generating error
except ZeroDivisionError:
    print("Division by Zero is not possible")
else:
    print(f"Division is possibe and result: {result}")
finally:
    print("I always run!")

# Now going to use alias for Error message

try:
    result  = 10/0
except ZeroDivisionError as e:
    print(f"Error is: {e}")
else:
    print(f"Division occured: {result}")
finally:
    print("I always run!")

# Now going to give multiple error in except at once

try:
    result = 23/0
except (ZeroDivisionError, ValueError, TypeError) as e:
    print(f"Error is: {e}")
else:
    print("I will not run in this condition")
finally:
    print("Hahaha lol I will always run")

# Now going to program new logic for raise() statement
# Basically what i know is raise is used to generate error

def age(a):
    if a < 0:
        raise ValueError("Age cannot be less than 0")
    return a

try:
    print(age(5))
    print(age(-3))
except (ValueError, TypeError) as e:
    print(f'Error is: {e}')
else:
    print('Hahah my turn!')