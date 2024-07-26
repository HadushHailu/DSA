 def minimumPlatform(n,arr,dep):
        # Sort arrival and departure arrays
        arr.sort()
        dep.sort()
    
        # Initialize pointers for arrival and departure
        i = 0  # Pointer to arrival array
        j = 0  # Pointer to departure array
        platform_needed = 0  # Number of platforms needed at a time
        max_platforms = 0  # Maximum platforms needed
    
        # Traverse both arrays
        while i < n and j < n:
            # If next event in sorted order is arrival, increment count of platforms needed
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
                # Update result if needed
                max_platforms = max(max_platforms, platform_needed)
            else:
                # If next event is departure, decrement count of platforms needed
                platform_needed -= 1
                j += 1
    
        return max_platforms


n = 6
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(minimumPlatform(n, arr, dep))