only_letters = "HelloWorld"
only_digits = "12345"

print("'HelloWorld'.isalpha() ->", only_letters.isalpha())
print("'12345'.isdigit() ->", only_digits.isdigit())

# Examples with spaces that we strip first
letters_with_space = " Hello World "
digits_with_space = " 12345 "

print("' Hello World '.strip().isalpha() ->", letters_with_space.strip().isalpha())
print("' 12345 '.strip().isdigit() ->", digits_with_space.strip().isdigit())
    ##output
'HelloWorld'.isalpha() -> True
'12345'.isdigit() -> True
' Hello World '.strip().isalpha() -> False
' 12345 '.strip().isdigit() -> True

=== Code Execution Successful ===
