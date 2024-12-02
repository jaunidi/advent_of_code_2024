

def read_input_file(path):
    
    with open(path,'r') as file:
        lines = file.readlines()
        
    list_1 = []
    list_2 = []
    
    for line in lines:
        data = line.split()
        list_1.append(int(data[0]))
        list_2.append(int(data[1]))
    return list_1,list_2

def order_list(list_to_order): #HARD STYLE. Could use .sort() built-in method instead.
    for i in range(len(list_to_order)):
        min_value_idx = i
        for j in range(i,len(list_to_order)):
            if list_to_order[j] < list_to_order[min_value_idx]:
                min_value_idx = j
        list_to_order[i],list_to_order[min_value_idx] = list_to_order[min_value_idx],list_to_order[i]
    return list_to_order

def compute_distance(list_1,list_2):
    distances_list = []
    for i in range(len(list_1)):
        distances_list.append(abs(list_1[i]-list_2[i]))
    tot_distance = sum(distances_list)
    return tot_distance

def main():
    list_1,list_2 = read_input_file(path='/Users/juandiaz/Documents/Github/advent_of_code_2024/day1_data')
    list_1_ordered = order_list(list_1)
    list_2_ordered = order_list(list_2)
    tot_distance = compute_distance(list_1_ordered,list_2_ordered)
    print(tot_distance)
    return

if __name__ == "__main__":
    
    main()
