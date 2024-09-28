active_elements={}
active_calls={}
active_non_element_calls={}
def count_active(bb, depth=1):
    if bb.len > 0:
        if depth in active_elements:
            active_elements[depth] += bb.len 
        else:
            active_elements[depth] = bb.len
        if depth in active_calls:
            active_calls[depth] += 1
        else:
            active_calls[depth] = 1
        if depth in active_non_element_calls:
            active_non_element_calls[depth] += 1
        else:
            active_non_element_calls[depth] = 1
    elif bb.len == 0:
        x = 1 if bb.max == np.inf else 2
        if depth in active_elements:
            active_elements[depth] += x
        else:
            active_elements[depth] = x
        if depth in active_calls:
            active_calls[depth] += 1
        else:
            active_calls[depth] = 1
    
    if bb.children:
        for b in bb.children:
            count_active(b, depth=depth+1)

count_active(bbb)
active_elements
print("active_elements", active_elements)
print("active_calls", active_calls)
print("active_non_element_calls", active_non_element_calls)