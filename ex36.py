# Designing and debugging

# tips & tricks
# * try not to nest IFs deeper than 2 levels
# * logical conditions should be simple and neat. If they get too complex, introduce variables and initialize them at the top. Use clear nomenclature.

# While loop in Python is almost never used. It is useful when you have to create a somewhat "infinite" loop, but pretty much only then.
# For loop is the usual go-to choice, especially when there's a constant, finite number of elements to loop through.

# Debugging:
# Something I've already found out myself - do not use debuggers, but tend to log all your data by either prints or using custom loggers.
# Write your code chunk by chunk, testing on the go. It is way better than writing a huge block of code and only debugging it at the end.