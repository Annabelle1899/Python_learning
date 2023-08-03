def format_message(**kwargs):
    print(kwargs)
    if 'name' in kwargs and 'age' in kwargs:
        return f"Hello, my name is {kwargs['name']} and I am {kwargs['age']} years old."
    else:
        return "Please provide a name and age."

print(format_message(name='Alice', age=30))  # Output: Hello, my name is Alice and I am 30 years old.
print(format_message(name='Bob'))  # Output: Please provide a name and age.
