def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))

    first = 0
    last = len(data) - 1  # 10

    while first <= last:
        mid = (first + last) // 2  # 5, 4
        print(mid)

        # Move mid to the closest non-empty value
        if not data[mid]:
            left = mid - 1  # 4,
            right = mid + 1  # 6,

            while True:
                if left < first and right > last:
                    return f"{search_val} is not in the dataset"
                elif left >= first and data[left]:
                    mid = left
                    break
                elif right <= last and data[right]:
                    mid = right
                    break

                left -= 1
                right += 1

        # Perform the check after finding a non-empty value
        if data[mid] == search_val:
            return f"{search_val} found at position {mid}"
        # If data[mid] < search_val, it means the value at the middle index is
        # alphabetically less than the search value. For example, if mid points
        # to "Art" and search_val is "Ball", since "Art" comes before "Ball"
        # alphabetically, the search needs to continue in the right half of the list.
        # This is because the list is sorted, and all values after "Art" could potentially
        # be "Ball" or come alphabetically after "Art".
        elif data[mid] < search_val:
            first = mid + 1
        else:
            last = mid - 1

    return f"{search_val} is not in the dataset"
