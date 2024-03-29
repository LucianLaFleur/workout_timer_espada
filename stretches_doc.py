# NOTE: ALL [standing] variations are the last sub-array when multiple are avaliable (a mat/ floor may not be viable sometimes...)
import random
# key string will always end with _stand or _sit for each exercise type
# intended to have either stand or sit as the key

stretch_keyword_arr = [
    #  0 index is the standing version for all arrays
    # ["ankles_mobility"],
    # ["back_stand", "back_sit"],
    # ["calves_stand", "calves_sit"],
    # ["glutes_stand", "glutes_sit"],
    # ["hamstring_stand" 
    # # "hamstring_sit"
    # ],
    # ["hips_work"
    # #  "hips_sitting"
    #  ],
    # ["neck"],
    # ["quads_stand", "quads_sit"],
    # # single hamstring stretch focus
    # ["shoulder_stretch"],
    # ["sing_hamstring_stand", "sing_hamstring_sit"],
    # ["splits_stand", "splits_sit"],
    # ["tricep_stretch"],
    ["wrists"]
]
warmup_keyword_arr = [
    "abs_work",
    "bicep_work",
    # "leg work, hard"
    # "leg work, light",
    # "pectoral_work",
    # "shoulder_work",
    # "tricep_work",
    "wrists_work"
]
# :["exercise_names/.wav"],
special_list = [
    # "side-slugger torso twist",
    # "open-hip, str. high-knee", # hands up, high knees
    # "torso twist hip taps", #don't forget to point the toes
    # "double-fang down-stab", # the high hammer curl
    # "squat to overhead press"
    ]
stretch_dic = {
    "ankles_mobility":[
        ["L.Stand ankle rotations", "R.Stand ankle rotations"], 
        # ["Sitting, ankle rotations clockwise", "Sitting, ankle rotations counter-clockwise"],
        # ["Seated knee up toe-point, heel point", "seated boat isometric, toe-point heel-point"]
        ["L.Stand heel-to-toe point", "R.Stand heel-to-toe point"]
    ],
    "back_stand": [
        ["L.Lunge torso turn", "R.Lunge torso turn"], 
        ["clock hula hips", "counter hula hips"],
    ],
    "back_sit": [
        ["L.Leg cross model pose", "R.Leg cross model pose"]
    ],
    "calves_stand":[
        ["L-stand fw-lean calf", "R-stand fw-lean calf"]
    ],
    "calves_sit": [
        # ["Pike, L-calf stretch", "Pike, R-calf stretch"] #need aud
        ["L-stand fw-lean calf", "R-stand fw-lean calf"]
    ],
    "glutes_stand": [
        ["Stand L. knee-tuck", "Stand R. knee-tuck"], 
        ["L.back, lunging stretch", "R.back, lunging stretch"]
    ],
    "glutes_sit": [
        ["Lying L-knee-tuck", "Lying R-knee-tuck"]
    ],
    "hamstring_stand": [
        ["Stand-V Left-leg", "Stand-V Right-leg", "Stand-V center"]
    ],
    "hamstring_sit": [
        ["V-sit Left", "V-sit Right", "V-sit Center"]
    ],
    "hips_work": [
        # ["L.Stand hip circles", "R.Stand hip circles"],
        ["L.Side hip abduction", "R.Side hip abduction"]
        # NEED TO ADD FROG SQUAT
        # ["L.Stand hip circles", "R.Stand hip circles", "Frog Squat Stretch"],
        # ["L.side hip abduction", "R.Side hip abduction", "Frog Squat Stretch"]
    ],
    # "hips_sitting":[
    #     ["Butterfly Stretch", "Lie.L.Leg hip Circles", "Lie.R.Leg hip Circles"],
    #     ["Butterfly Stretch", "Lie.L.Leg alt. hip-cir.", "Lie.R.Leg alt. hip-cir."],
    #     ["Butterfly Stretch", "Sit L.Hip Abduction", "Sit L.Hip Abduction"]
    # ],
    "neck": [
        ["Look-up neck ro.", "Look-down neck ro."]
    ],
    "quads_stand":[
        ["L.Stand quad pull", "R.Stand quad pull"]
    ],
    "quads_sit": [
        ["L.Lying quad stretch", "R.Lying quad stretch"]
    ],
    "shoulder_stretch":[
        # ["Left arm reach-across, squats", "Right arm reach-across squatz"], 
        ["L.Arm Across high-knees", "R.Arm Across high-knees"],
        ["L.Arm Across side step", "R.Arm Across side step"],
        ["L.Arm Across, Calf Raise", "R.Arm Across, Calf Raise"]
    ],
    "sing_hamstring_stand": [
        ["Stand.Center toe-touch", "L.Over toe-touch", "R.Over toe-touch"]
    ],
    "sing_hamstring_sit": [
        ["Sit.Toe-touch", "L.Leg out, toe-touch", "R.Leg out, toe-touch"], 
        ["Sit.Toe-touch", "Sit L.Extension hold", "Sit R.Extension hold"]
    ],   
    "splits_stand":[
        ["Center split", "Left side-lunge", "Right side-lunge"]
        # ["Center split", "left leg forward RDL","left leg forward RDL"]
    ],
    "splits_sit":[
        ["Center split", "Left front-split", "Right front-split"]
    ], 
    "tricep_stretch": [
        # ["Left tricep stretch squats", "Right tricep stretch squats"],
        ["L. Tri, side-step", "R. Tri, side-step"],
        ["L. Tri. & ankle raises", "R. Tri. & ankle raises"],
        ["L. Tri. & high-knees", "R. Tri. & high-knees"]
    ],
    "wrists":[
        ["Arms up, wrist-ro.", "Arms out, wrist-ro."], 
        ["X-Y-T Wrist rotations", "A-pose In. Wrist Cir.", "A-pose Out Wrist Cir."], # "XYT, or "exit" dancer's wrist rotations, arms out, hug in for x, rotating wrists with each move                                                    
        # ["clockwise wrist-rotations", "counter-clockwise wrist-rotations"], 
        ["Y-A-X-T-X, wrist ro.", "A-pose In. Wrist Cir.", "A-pose Out Wrist Cir."], # ADV. "Yak's Tax" means Y-A-X-T-X
        ["Cat's claw wrist bends", "Thriller wrist cir."] # side to side doing the car pose, forearm stretch ! be sure to go all the way up and all the way down with a wrist flap at the peak of each thriller pose
        # Alternating palm-down forearm raises
    ]  
}

warmup_dic ={
    "abs_work": [
        "slow stand. Bicycles", 
        "windmill toe touches",
        "windmill sky chops", 
        "stellar windmills",
        "Figure-8 oblique Ax.",
        "belly dancer kicks", # high knees if no space for it
        "lighthouse torso twists",
        "cross-core knee strike",
        # "squat-betw. stand.Bike",
        "straight-leg toe taps",
        "draw sword, side-bend",
        "wood chopper oblique"
    ],
    "bicep_work":[
        "curl, overhead press", 
        # "curl, fly press", 
        "claw-hand Z-curls", 
        "curl & double punch out", # Greaser's jacket
        # biceb curl double punch
        # "mummy hug" # zombie curl, arms across chest, outward fly, clap in, z-curl down
        # "claw hand alternating bicep curls", 
        "barrel hug hammer curl",
        # "chop out, scrape in", # tricep active, then bicep active, circular motion
        # "curl to ro. press # "periscope push" # claw pose biceb curl with rotating military press, arms go up like a periscope
        # Scary bear bicebs # claw pose biceb curl, arm rotation 
        # "45-degree palm press" # the bell-ringer
    ],
    "leg work, hard":[
        # "triangle pose side lunges", 
        "step-back lunges", 
        "alt. torso-twist lunges", #remember to tap opposite heel of planted foot
        "3-point frog squats", 
        # "comound fly press lunge",
        "squat pulse stand-ups"
        # "prisoner squat to standing bicycle", 
# moved to special arr "squat to overhead press"
    ],
    "leg work, light":[
        # "marching zombie knee raises", 
        "marching doll high knee", 
        "wall-crawlers" # "standing bird-dog reach"
        # "heel-to-toe calf raises",
        # "point inward, point out calf raises", #turn on the heel
        # ["inward pointing calf-raises", "outward pointing calf-raises"]
        # "alternating reach and hip abduction" #reach with left arm as right leg goes out to side
        # "alternating forward single-leg reach" # stand on one leg, reach with both arms forward, keep back straight, come back up, switch.
    ],
    "pectoral_work":[
        # "Do the monkey!",
        "sky-punch fly press",
        "biceb curl fly press", 
        "sing. arm fly side-step",
        # "arms fly out, double-punch forward", 
        # "hands-together up-and-downs", 
        # hands together, press up like hands together in tree pose, then down, like a lateral row
        # "open-hip T-bolt pr.ess",
         # kneeling version lets you back bend for more range of movement
        # kneeling thunderbolt prayer,
        "X-Y fly press" # "cactus hugger", fly press, cross arms in an X, then arms go up to a y-pose, back in for X

    ],
    "shoulder_work":[
        # "arms out, tension wrist rotations",
        "4-count cheer squad", 
        # "wax on, wax off", # full motion to activate tricep
        "slow lat pull-down",
        # "overhead lat pull down push-out"
        # "lateral pull down to shoulder shrug forward-back", 
        "sing.Side-step sky-punch", 
        "back-stroke torso twist",
        "sky-punch, side stab", # starting from boxer's position
        # "sky punch palm out, palm in",
        # "ankle raise, shoulder shrugs",
        # "ankle raise, big shoulder circles",
        "vampire wings" # claw pose, hands down in front, up to Y position and back down again
    ],
    "tricep_work":[
        # ["left overhead tricep tomahawk", "right overhead tricep tomahawk",]
        # ["side-step, side-stab"], # like a sideways chop, always keeping motion inward for play area
        # ["left tension tricep kickbacks", "right tension tricep kickbacks"],
        # "bodyweight tricep dips"
        "florentine 1-2", # arms up as if holding two swords, left arm to right shoulder chambered while right arm is up and out, backslash with left and down-slash with right; both go down with gravity, then switch; 
            # ^^ looks like a dance move tricep extension for an out
        "alternating hammer-downs" 
# *added to special arr "double-fang downward stab"
    ],
    "wrists_work":[
        # "alternating claw-hand forearm raise", # same as zombie claw forearm raise, looks like frankenstein's monster
        "zombie claw f.Arm Raise",
        "T-rex bicep curl", #wrists bent to add extra tension and activate forearms 
        "A-pose ro. claw-curls", #forearm tension, rotate to wrists-behind-back position, wrists tense back, then rotate to palm forward, wrists tense up and in
        "claw-hand Z-curls",
        "shrieking ghoul" # claw forearm raise, then press up, tricep hammer down in front
        # "arms forward, tension wrist rotations",
        # "arms out, tension wrist rotations" # crossover with shoulders
    ]
}

# def get_stretch_x_warmup_list():
#     # due to the set size of the workout to hit all muscle groups, there's an imbalance
#     # 13 total stretches. 15 warmup moves = 28 total moves, not counting mirroring
#     # 2 initial warmup moves get the blood flowing, then each stretch is followed by another warm-up move.
#     combined_list = []
#     list_of_stretch_lists = []
#     selected_warmups_name_arr = []
#     # get 2 random exercises for warm-up, 
#     random_2_starters = random.sample(warmup_keyword_arr, 2)
#     temp_warmup_keyword_arr = warmup_keyword_arr
#     for item in random_2_starters:
#         temp_warmup_keyword_arr.append(item)

#     for keyword in temp_warmup_keyword_arr:
#         chosen_warmup = random.choice(warmup_dic[keyword])
#         selected_warmups_name_arr.append(chosen_warmup)
#     for special_item in special_list:
#         selected_warmups_name_arr.append(special_item)
    
#     random.shuffle(selected_warmups_name_arr)
#     # input(f"current warmups are: >>> \n{selected_warmups_name_arr}")

#     # randomize the order of stretches

#     for x in stretch_keyword_arr:
#         chosen_stretch_type = random.choice(x)
#         chosen_stretch_motion_arr = random.choice(stretch_dic[chosen_stretch_type])
#         list_of_stretch_lists.append(chosen_stretch_motion_arr)
#     random.shuffle(list_of_stretch_lists)
#     # input(f"current stretch motions >> \n{list_of_stretch_lists}")
    
#     # enumerating on the warmups names because they'll go up to 15
#     for i, stretch_name in enumerate(selected_warmups_name_arr):
#         # since enumerate i starts at 0, we'll get the first two warm-ups like this, then move on to adding a stretch+warmup
#         if i < 2:
#             # print(f"index 'i' is {i}, not in main portion yet")
#             #  select an appropriate random item from the arrays at the dictionary entry accessed by the appropriate keyword
#             combined_list.append(stretch_name)
#         else:
#             # the stretches lag behind by 2 from the warmup list since we start off with 2 warm up moves before stretching
#                 # within the list-of-stretch-lists, this targets the sub-array at the given index.
#                 # this keeps all hamstring sets or quad sets together even if mirrored.
#             random.shuffle(list_of_stretch_lists[i-2])
#                 # ^^ also shuffling so it's not always left/right/center as data input is like
#             for individual_stretch in list_of_stretch_lists[i-2]:
#                 combined_list.append(individual_stretch)
#             combined_list.append(stretch_name)

#     return combined_list

# prepared_list = get_stretch_x_warmup_list()
# ------------------------------------------------------------------------------------------------------------------------------------
                                                # STRETCHES
# ------------------------------------------------------------------------------------------------------------------------------------
 # "Left lunge torso turn", "Right lunge torso turn", "standing hula hip rotations, clockwise", "standing hula hip rotations, counter-clockwise",
    # "Left leg across, model pose", "Right leg across, model pose",
    # "Left, standing forward lean calf stretch", "Right standing forward lean calf stretch",
    # "Pike position, left cross calf stretch", "Pike position, right cross calf stretch",
    # "Standing left knee-tuck stretch", "Standing right knee-tuck stretch", "Left leg back, lunging stretch", "Right leg back, lunging stretch",
    # "Lying left knee-tuck stretch", "Lying right knee-tuck stretch",
    # "Standing-v Left-leg", "Standing-v Right-leg", "standing-v center stretch",
    # "V-sit Left", "V-sit Right", "V-sit Center",
    # "Look-up neck rotation", "Look-down neck rotation",
    # "Standing quad stretch, left", "Standing quad stretch, right",
    # "Lying quad stretch, left", "Lying quad stretch, right",
    # "Standing center toe-touch reach", "Left leg over right, toe-touch", "Right leg over left, toe-touch",
    # "Sitting toe-touch reach", "Left leg out, toe-touch", "Right leg out, toe-touch", "Sitting toe touch", "Sitting left leg extension hold", "Sitting right leg extension hold",   
    # "Center split", "left side-lunge", "right side-lunge",
    # "Center split", "Left front-split", "Right front-split"

# extra bark words
# basic, steady, tension, focus, steady-breathing, controlled
# compound motion, combination move
#  singular motion, 
