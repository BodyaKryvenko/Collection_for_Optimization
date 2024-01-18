import pathlib

data = []
targets = []
replay_memory_location = (
        pathlib.Path("ML_replay_memories") / "random_random_10k_games.txt"
)
with open(file=replay_memory_location, mode="r") as replay_memory_file:
    for line in replay_memory_file:
        feature_string, won_label_str = line.split("||")
        feature_list_strings = feature_string.split(",")
        feature_list = [int(feature) for feature in feature_list_strings]
        won_label = int(won_label_str)
        data.append(feature_list)
        targets.append(won_label)

X = data
y = targets

