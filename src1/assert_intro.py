
# Step 1: MicroPython assert Keyword
# Try to copy and paste following code into REPL

x = "hello Micropython"

# if condition returns True, then nothing happens:
assert x == "hello Micropython"

# if condition returns False, AssertionError is raised:
assert x == "bye"


# Step 2: Write a message if the condition is False
# Try to copy and paste following code into REPL

x = "hello Micropython"

# if condition returns False, AssertionError is raised:
assert x == "bye", "x should be 'hello Micropython'"
