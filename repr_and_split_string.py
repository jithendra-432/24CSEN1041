text = "   hello   "
print(text)        # looks like: hello   (spaces not obvious)
print(repr(text))  # shows: '   hello   '
  ##output
     hello   
'   hello   '

=== Code Execution Successful ===
  sample = "   hello   world  from  Python   "

# 1) Remove spaces at the beginning and end
clean = sample.strip()
print("After strip():", repr(clean))

# 2) Split into words by whitespace
words = clean.split()
print("split() ->", words)
       ## output
    After strip(): 'hello   world  from  Python'
  split() -> ['hello', 'world', 'from', 'Python']
