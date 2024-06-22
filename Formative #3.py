def relationship_status(from_member, to_member, social_graph):

    if to_member in social_graph.get(from_member, {}).get("following", []):
        if from_member in social_graph.get(to_member, {}).get("following", []):
            return "friends"
        else: 
            return "follower"
    if from_member in social_graph.get(to_member, {}).get("following", []):
        return "followed by" 
    else:
        return "no relationship"

def tic_tac_toe(board):
# Row
    for row in board:
        if row.count("X") == len(board):
            return "X"
        elif row.count("O") == len(board):
            return "O"
# Column 
    for col in range(len(board)):
        X_count = 0
        O_count = 0
        for row in range(len(board)):
            if board[row][col] == "X":
                X_count += 1
            elif board[row][col] == "O":
                O_count += 1
        if X_count == len(board):
            return "X"
        elif O_count == len(board):
            return "O"

# Diagonals
    X_count = 0
    O_count = 0
    for i in range(len(board)):
        if board[i][i] == "X":
            X_count += 1
        elif board[i][i] == "O":
            O_count += 1
    if X_count == len(board):
        return "X"
    elif O_count == len(board):
        return "O"

    X_count = 0
    O_count = 0
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] == "X":
            X_count += 1
        elif board[i][len(board) - 1 - i] == "O":
            O_count += 1
    if X_count == len(board):
        return "X"
    elif O_count == len(board):
        return "O"

    return "NO WINNER"

def eta(first_stop, second_stop, legs):
    counter = 0
    stop_list = []
    while counter < len(legs):
        list_of_keys = list(legs.keys())
        first_keys = list_of_keys[counter][0]
        stop_list.append(first_keys)
        counter += 1

    travel_time = [legs[keys]["travel_time_mins"] for keys in legs]
    
    if (first_stop, second_stop) in legs:
        total_time = legs[first_stop, second_stop]["travel_time_mins"]
        return total_time

    elif first_stop in stop_list and second_stop in stop_list:
        first_index = stop_list.index(first_stop)
        second_index = stop_list.index(second_stop)

        if first_index < second_index:
            total_time = sum(travel_time[first_index:second_index])
            return total_time
        elif first_index > second_index:
            total_time = sum(travel_time[first_index:len(stop_list)]) + sum(travel_time[0:second_index])
            return total_time
        elif first_index == second_index:
            total_time = sum(travel_time[0:len(stop_list) + 1])
            return total_time
        elif second_index == 0:
            total_time = sum(travel_time[second_index + 1:len(stop_list)])
            return total_time
    else:
        return "Route not found." 