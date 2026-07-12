# Different ways to define strings
my_str_1 = 'Hello'
my_str_2 = "World"
my_str_3 = """Multiline string"""
my_str_4 = '''Another multiline string'''

# Handling quotes inside strings
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# Escaping quotes
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

# String membership and indexing
my_str = 'Hello world'
print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)     # False
print('e' in my_str)      # True
print('f' in my_str)      # False
print(len(my_str))
print(my_str[0])  # H
print(my_str[6])  # w