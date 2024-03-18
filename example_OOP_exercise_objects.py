# This document is a reference for the OOP structure, transitioning away from the multi-array
# + Intended as a possible solution to filtering exercises by strings in multiple arrays
# + minimizes repeat data by relying on one master list of exercises, where the exercises contain tags within info
# + more funcitons will be added and tags standardized as feedback accrues 

class WorkoutMove:
    def __init__(self, name_string, display_name_list, info_list):
        self.key_name = name_string
        self.display_name_list = display_name_list
        self.info_list = info_list

# key name
all_exercise_objects = [
    WorkoutMove("single rock-and-box",
        ["L. rock-and-box","R. rock-and-box"],
        ["abs", "obliques", "delts", "mirrored", "cardio", "light", "martial"]),
    WorkoutMove("alternating rock-and-box", # need aud
        ["Alt. rock-and-box"],
        ["abs", "obliques", "delts", "cardio", "light", "martial"]),
    WorkoutMove("Side-slugger torso twist", # side punch, turn, punch to other side
        ["Side-slugger torso twist"],
        ["abs", "cardio", "light", "control", "martial", "res.band"]),
    WorkoutMove("squat to overhead press",
        ["squat to overhead press"],
        ["hamstrings", "delts", "med", "cardio", "compound", "big_weight", "small_weight"]),
    WorkoutMove("marching doll high knee",
        ["marching doll high knee"],
        ["hip flexors", "delts", "light", "cardio", "compound"]),
    WorkoutMove("single arm fly side-step",
        ["alt. arm fly side-step"],
        ["pecs", "delts", "light", "cardio", "compound"]),
    WorkoutMove("lat pull-down push-out",
        ["lat pull-down push-out"],
        ["traps", "delts", "compound", "cardio", "small_weight"]),
    WorkoutMove("3-point frog squats",
        ["3-point frog squats"],
        ["quads", "delts", "med", "cardio", "compound", "dumbbell"]),
    WorkoutMove("kneel_lat pull-down push-out", # need aud
        ["Kn.Lat pull-down push-out"],# need aud
        ["traps", "delts", "compound", "cardio", "small_weight", "ground"]),
    WorkoutMove("single forearm raise",
        ["L.forearm raise", "R.forearm raise"],
        ["forearms", "mirrored", "small_weight", "big_weight"]),
    WorkoutMove("single inner bicep curl",# need aud
        ["L.inner bicep curl", "R.inner bicep curl"],
        ["biceps", "mirrored", "small_weight", "big_weight"])
]

all_workout_object_keys = [
"Side-slugger torso twist", 
"single rock-and-box", 
"alternating rock-and-box",
"squat to overhead press",
"marching doll high knee",
"single arm fly side-step",
"lat pull-down push-out",
"3-point frog squats",
"kneel_lat pull-down push-out",
"single forearm raise",
"single inner bicep curl"
]

def exclude_keywords_from_workout_list(keyword_list):
    # out_arr = []
    # for move in all_exercise_objects:
    #     for keyword in keyword_list:
    #         if keyword in move.info_list:
    #             for name_string in move.display_name_list:
    #                 out_arr.append(name_string)
    # print(out_arr)
    out_arr = [move.display_name_list for move in all_exercise_objects if not any(exclusion_term in keyword_list for exclusion_term in move.info_list)]
    print(out_arr)

def get_moves_matching_at_least_one_keyword(keyword_list):
    # iterate through all exercise objects. only return the ones that match at least one item in the target array
    out_arr = [move.display_name_list for move in all_exercise_objects if any(exclusion_term in keyword_list for exclusion_term in move.info_list)]
    # return [car for car in cars if not any(color in exclude_colors for color in car.color)]
    print(out_arr)
    
get_moves_matching_at_least_one_keyword(["traps"])
print(f"*"*24)
exclude_keywords_from_workout_list(["delts", "biceps"])
