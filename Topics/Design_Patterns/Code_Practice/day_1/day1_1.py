# Goal: Apply KISS (Keep It Simple, Stupid)
# def process_data(data, mode):
#     if mode == "sum":
#         result = 0
#         for item in data:
#             result += item
#         print("Sum:", result)
#     elif mode == "average":
#         result = 0
#         for item in data:
#             result += item
#         average = result / len(data)
#         print("Average:", average)
#     elif mode == "max":
#         max_val = data[0]
#         for item in data:
#             if item > max_val:
#                 max_val = item
#         print("Max:", max_val)
def find_sum(data):
    return "Sum: ", sum(data)

def find_average(data):
    return ("Average: ", (sum(data) / len(data)))

def find_max(data):
    return ("Max: ", max(data))

def print_result(label_and_value_pair):
    label, value = label_and_value_pair
    print(f"{label}: {value}")

def process_data(data, mode):
    print_result(mode(data))
    