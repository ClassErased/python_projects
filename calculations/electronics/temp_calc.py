#OpenAI demo, I wont use it to entirely write a program like this.
#But its awesome to ask it to write something you have already coded up and see the diff

# Define the variables
voltage = 120  # in volts
current = 10   # in amperes
resistance = 0.5  # in ohms

# Calculate the power using the law of power
power = voltage * current

# Calculate the temperature rise using the formula
# T = P * R / (k * A)
# where T is the temperature rise, P is the power, R is the resistance,
# k is the temperature coefficient, and A is the cross-sectional area
temperature_rise = power * resistance / (0.00426 * 0.0127)

# Print the result
print("Temperature rise = ", temperature_rise, "degrees Celsius")