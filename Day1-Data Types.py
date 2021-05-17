i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
input_int=int(input())
input_double= float(input())
input_string=str(input())
# Read and save an integer, double, and String to your variables.
# Print the sum of both integer variables on a new line.
print(i+ input_int)

# Print the sum of the double variables on a new line.
print(round(d+input_double, 1)) #The round keyword is used to round the value.
                                 # Without using the round keyword the output was 8.01
                                # So to print 8.0 round it to 1. 
# Concatenate and print the String variables on a new line
print(s+ input_string)

# The 's' variable above should be printed first.
