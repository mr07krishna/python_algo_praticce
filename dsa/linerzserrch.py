def linersearch(num, key):
    for i in range(len(num)):
        if key == num[i]:
            return True
    return False

num = [2,3,5,2,6,9,3,5,5,9,2]
key = 7

if linersearch(num, key):
    print(key,"is found in the list")

else:
    print(key, "not found in the list")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found


