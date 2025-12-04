def joltage(battery):
    battery = str(battery)
    first_digit = max(battery[:-1])
    first_digit_index = battery.find(first_digit)
    second_digit = max(battery[first_digit_index+1:])
    value = int(first_digit + second_digit)
    return value

def total_joltage(batteries):
    batteries = batteries.split('\n')
    total_value = 0
    for battery in batteries:
        total_value += joltage(battery)
    return total_value


batteries = """987654321111111
811111111111119
234234234234278
818181911112111"""
print (total_joltage(batteries))
