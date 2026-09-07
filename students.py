# a) Store marks in a list (1 mark)
marks = [45, 78, 56, 32, 89, 60]

# b) Function to calculate average (3 marks)
def calculate_average(lst):
    return sum(lst) / len(lst)

# c) Count passes/fails using a loop (3 marks)
passed = 0
failed = 0
for m in marks:
    if m >= 50:
        passed += 1
    else:
        failed += 1

# d) Display results (1 mark)
avg = calculate_average(marks)
print(f"Average mark: {avg:.2f}")
print(f"Passed: {passed}, Failed: {failed}")

# e) Conditional for class performance (2 marks)
if avg >= 70:
    print("GOOD CLASS PERFORMANCE")
elif avg >= 50:   # average from 50 to 69
    print("FAIR CLASS PERFORMANCE")
else:
    print("POOR CLASS PERFORMANCE")