
def APseries_checker(arr):
    diff = arr[1]-arr[0]
    # print(diff)
    for i in range(len(arr)-1):
        print(i,arr[i],arr[i]-arr[i+1])
        print(diff)

        if arr[i] - arr[i+1] == diff:
            continue
        else:
            return False
    return True

arr = [3,5,1]
print(APseries_checker(arr))
