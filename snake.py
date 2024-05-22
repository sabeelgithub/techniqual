import pandas as pd
import random

def game(grid_size,num_players):
    max_position = grid_size * grid_size
    players_data = []

    for player in range(num_players):
        dice_roll_history = []
        position_history = []
        current_postion = 0

        while current_postion < max_position:
            dice_roll = random.randint(1,6)
            dice_roll_history.append(dice_roll)
            current_postion += dice_roll
            if current_postion > max_position:
                current_postion = max_position
            position_history.append(current_postion)
            if current_postion >= max_position:
                break

        players_data.append({
            "Player":f"Player {player + 1}",
            "Dice Roll History":','.join(map(str,dice_roll_history)),
            "Postion History":','.join(map(str,position_history)),
            "Win Status":1 if current_postion >= max_position else 0
        })

    df = pd.DataFrame(players_data)
    return df

df=game(3,3)
print(df)

    

