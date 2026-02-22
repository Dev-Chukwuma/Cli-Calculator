import math

# -------------------------------------------------------
#            CALCULATION FUNCTIONS (WITH WORKINGS)
# -------------------------------------------------------

def summation(values):
    total = sum(values)
    working = f"Sum = {' + '.join(map(str, values))} = {total}"
    return total, working

def product(values):
    result = 1
    for v in values:
        result *= v
    working = f"Product = {' × '.join(map(str, values))} = {result}"
    return result, working

def subtraction(values):
    result = values[0]
    for v in values[1:]:
        result -= v
    working = f"Subtraction = {values[0]} - {' - '.join(map(str, values[1:]))} = {result}"
    return result, working

def division(values):
    result = values[0]
    working_steps = [str(values[0])]
    for v in values[1:]:
        if v == 0:
            return "Error", "Division by zero is undefined."
        result /= v
        working_steps.append(str(v))

    working = f"Division = {' ÷ '.join(working_steps)} = {result}"
    return result, working

def mean_ungrouped(values):
    total = sum(values)
    count = len(values)
    mean_value = total / count
    working = f"Mean = Sum / Count = {total} / {count} = {mean_value}"
    return mean_value, working

def mean_grouped(values, frequencies):
    total_fx = sum(values[i] * frequencies[i] for i in range(len(values)))
    total_f = sum(frequencies)
    mean_value = total_fx / total_f 
    working = (
        f"Mean (Grouped)\n"
        f"Σ(f×x) = {total_fx}\n"
        f"Σf = {total_f}\n"
        f"Mean = Σ(f×x) / Σf = {total_fx} / {total_f} = {mean_value}"
    )
    return mean_value, working

def median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)

    if n % 2 == 1:
        med = sorted_vals[n // 2]
        working = f"Sorted values = {sorted_vals}\nMedian = Middle value = {med}"
    else:
        a = sorted_vals[n//2 - 1]
        b = sorted_vals[n//2]
        med = (a + b) / 2
        working = (
            f"Sorted values = {sorted_vals}\n"
            f"Median = (Middle two values {a} + {b}) / 2 = {med}"
        )
    return med, working

def mode(values):
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1

    highest = max(freq.values())
    modes = [k for k, v in freq.items() if v == highest]

    working = f"Frequencies = {freq}\nMode = {modes}"

    if len(modes) == 1:
        return modes[0], working
    return modes, working

def variance_ungrouped(values):
    mean_val = sum(values) / len(values)
    squared_diff = [(x - mean_val) ** 2 for x in values]
    var = sum(squared_diff) / len(values)

    working = (
        f"Mean = {mean_val}\n"
        f"Squared differences = {squared_diff}\n"
        f"Variance = Sum of squared differences / N = {sum(squared_diff)} / {len(values)} = {var}"
    )
    return var, working

def std_dev_ungrouped(values):
    var, var_work = variance_ungrouped(values)
    sd = math.sqrt(var)
    working = var_work + f"\nStandard deviation = √Variance = √{var} = {sd}"
    return sd, working

def square_root(value):
    result = math.sqrt(value)
    working = f"Square root = √{value} = {result}"
    return result, working

def square(value):
    result = value ** 2
    working = f"Square = {value}² = {result}"
    return result, working

def cube_root(value):
    result = value ** (1/3)
    working = f"Cube root = {value}^(1/3) = {result}"
    return result, working

def power(value, p):
    result = value ** p
    working = f"{value}^{p} = {result}"
    return result, working

def nth_root(value, n):
    result = value ** (1/n)
    working = f"{n}th root = {value}^(1/{n}) = {result}"
    return result, working

# -------------------------------------------------------
#                  INPUT COLLECTION
# -------------------------------------------------------

def get_values():
    print("\nEnter your numbers. Type 'done' to finish:")
    values = []
    while True:
        inp = input("→ ")
        if inp.lower() == "done":
            break
        try:
            values.append(float(inp))
        except:
            print("Invalid number. Try again.")
    return values

# -------------------------------------------------------
#                      MAIN PROGRAM
# -------------------------------------------------------

def calculator():
    print("\n===== SMART CALCULATOR =====")

    values = get_values()

    print("""
What do you want to calculate?

 1. Sum
 2. Product
 3. Division
 4. Subtraction
 5. Mean (Ungrouped)
 6. Mean (Grouped)
 7. Variance
 8. Standard Deviation
 9. Square Root
 10. Square
 11. Cube Root
 12. Any Power
 13. Any Root
 14. Median
 15. Mode
 """)

    choice = input("Enter choice number → ")

    try:
        if choice == "1":
            ans, work = summation(values)

        elif choice == "2":
            ans, work = product(values)

        elif choice == "3":
            ans, work = division(values)

        elif choice == "4":
            ans, work = subtraction(values)

        elif choice == "5":
            ans, work = mean_ungrouped(values)

        elif choice == "6":
            print("\nEnter frequencies:")
            freq = []
            for i in range(len(values)):
                freq.append(float(input(f"Freq for {values[i]}: ")))
            ans, work = mean_grouped(values, freq)

        elif choice == "7":
            ans, work = variance_ungrouped(values)

        elif choice == "8":
            ans, work = std_dev_ungrouped(values)

        elif choice == "9":
            ans, work = square_root(values[0])

        elif choice == "10":
            ans, work = square(values[0])

        elif choice == "11":
            ans, work = cube_root(values[0])

        elif choice == "12":
            p = float(input("Enter power: "))
            ans, work = power(values[0], p)

        elif choice == "13":
            n = float(input("Enter root degree: "))
            ans, work = nth_root(values[0], n)

        elif choice == "14":
            ans, work = median(values)

        elif choice == "15":
            ans, work = mode(values)

        else:
            print("Invalid choice.")
            return

        print("\n===== ANSWER =====")
        print(ans)

        print("\n===== WORKING =====")
        print(work)

    except Exception as e:
        print("Error:", e)

# -------------------------------------------------------
#                        RUN
# -------------------------------------------------------
calculator()