def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    step=0

    while low <= high:
        step+=1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (step,mid)

    # якщо елемент не знайдений
    return (step, arr[high+1] if high<len(arr)-1 else None)

arr = [2.5, 3.5, 4.5, 10.5, 40.5]
x = 2
result = binary_search(arr, x)
if result[1] != None:
    print(f"Element {x} nearest {result[1]} found in {result[0]} steps")
else:
    print(f"Element {x} doesn't have bigger value")
    
x = 3
result = binary_search(arr, x)
if result[1] != None:
    print(f"Element {x} nearest {result[1]} found in {result[0]} steps")
else:
    print(f"Element {x} doesn't have bigger value")
    
x = 41
result = binary_search(arr, x)
if result[1] != None:
    print(f"Element {x} nearest {result[1]} found in {result[0]} steps")
else:
    print(f"Element {x} doesn't have bigger value")