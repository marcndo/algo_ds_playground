def daily_temperature(temperature):
    length = len(temperature)
    result = [0] * length
    for i in range(length):
        for j in range(i+1, length):
            if temperature[j] > temperature[i]:
                result[i] = j - i
                break
    return result

def daily_temperature_optimal(temperature):
    result = [0] * len(temperature)
    stack = []
    for i, t in enumerate(temperature):
        while stack and t > stack[-1][0]:
            stack_t, stack_index = stack.pop()
            result[stack_index] = i - stack_index
        stack.append((t, i))
    return result