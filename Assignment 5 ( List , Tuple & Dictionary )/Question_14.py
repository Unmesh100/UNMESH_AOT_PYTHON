def maxValue(events, k):
    def backtrack(idx, k_left, last_end):
        if idx >= len(events) or k_left == 0:
            return 0
        
        # Skip current event
        max_val = backtrack(idx + 1, k_left, last_end)
        
        # Take current event if no overlap
        curr_start, curr_end, value = events[idx]
        if curr_start > last_end:
            max_val = max(max_val, value + backtrack(idx + 1, k_left - 1, curr_end))
            
        return max_val
    
    # Sort by start time to handle overlaps efficiently
    events.sort()
    return backtrack(0, k, 0)

# Get user input
if __name__ == "__main__":
    num_events = int(input("Enter the number of events: "))
    events = []
    
    for i in range(num_events):
        start = int(input(f"Enter start time for event {i+1}: "))
        end = int(input(f"Enter end time for event {i+1}: "))
        value = int(input(f"Enter value for event {i+1}: "))
        events.append([start, end, value])
    
    k = int(input("Enter the maximum number of events you can attend: "))
    print("Maximum value that can be obtained:", maxValue(events, k))
