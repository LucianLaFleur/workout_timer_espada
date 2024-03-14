# NOTE: ALL [standing] variations are the last sub-array when multiple are avaliable (a mat/ floor may not be viable sometimes...)

# key string will always end with _stand or _sit for each exercise type
# intended to have either stand or sit as the key

master_stretch_keyword_arr = [
    #  0 index is the standing version for all arrays
    ["ankles_mobility"],
    ["back_stand", "back_sit"],
    ["calves_stand", "calves_sit"],
    ["glutes_stand", "glutes_sit"],
    ["hamstring_stand" 
    #  NOTE: currently disabling the v-sit due to not having the right audio for it.
    # "hamstring_sit"
    ],
    ["hips_work"],
    ["neck"],
    ["quads_stand", "quads_sit"],
    # single hamstring stretch focus
    ["shoulder_stretch"],
    ["sing_hamstring_stand", "sing_hamstring_sit"],
    ["splits_stand", "splits_sit"],
    ["tricep_stretch"],
    ["wrists"]
]
master_warmup_keyword_arr = [
    "abs_work",
    "bicep_work",
    "leg work, hard",
    "leg work, light"
    "pectoral_work",
    "tricep_work",
    "tricep_stretch",
    "wrists_work"
]
master_stretch_dic = {
    "ankles_mobility":[
        ["Standing left ankle rotations", "Standing right ankle rotations"], 
        # ["Sitting, ankle rotations clockwise", "Sitting, ankle rotations counter-clockwise"],
        # ["Seated knee up toe-point, heel point", "seated boat isometric, toe-point heel-point"]
        ["Standing left toe point, heel point", "Standing right toe point, heel point"]
    ],
    "back_stand": [
        ["Left lunge torso turn", "Right lunge torso turn"], 
        ["standing hula hip rotations, clockwise", "standing hula hip rotations, counter-clockwise"]
    ],
    "back_sit": [
        ["Left leg across, model pose", "Right leg across, model pose"]
    ],
    "calves_stand":[
        ["Left, standing forward lean calf stretch", "Right standing forward lean calf stretch"]
    ],
    "calves_sit": [
        ["Pike position, left cross calf stretch", "Pike position, right cross calf stretch"]
    ],
    "glutes_stand": [
        ["Standing left knee-tuck stretch", "Standing right knee-tuck stretch"], 
        ["Left leg back, lunging stretch", "Right leg back, lunging stretch"]
    ],
    "glutes_sit": [
        ["Lying left knee-tuck stretch", "Lying right knee-tuck stretch"]
    ],
    "hamstring_stand": [
        ["Standing-v Left-leg", "Standing-v Right-leg", "standing-v center stretch"]
    ],
    "hamstring_sit": [
        ["V-sit Left", "V-sit Right", "V-sit Center"]
    ],
    "hips_work": [
        # ["Lying left leg hip mobility circles", "Lying right leg hip mobility circles"],
        ["Standing left hip circles", "Standing right hip circles"],
        ["left sideways hip abduction", "right sideways hip abduction"],
        # ["right leg, in and out hip-circles", "left leg, in and out hip-circles"]
        # ["Standing left straight-leg circles", "Standing right straight-leg circles"],
        # crab pose, leg traces a half-moon shape then switch legs
        # ["crab pose, half moon kicks", "seated scissor circles"]
    ],
    "neck": [
        ["Look-up neck rotation", "Look-down neck rotation"]
    ],
    "quads_stand":[
        ["Standing quad stretch, left", "Standing quad stretch, right"]
    ],
    "quads_sit": [
        ["Lying quad stretch, left", "Lying quad stretch, right"]
    ],
    "shoulder_stretch":[
        # ["Left arm reach-across, squats", "Right arm reach-across squatz"], 
        ["Left arm reach-across, high-knee lifts", "Right arm reach-across, high-knee lifts"],
        ["Left arm reach-across, side-to-side step", "Right arm reach-across, side-to-side step"]
        # ["Left arm reach-across, ankle raises", "Right arm reach-across, ankle raises"]
    ],
    "sing_hamstring_stand": [
        ["Standing center toe-touch reach", "Left leg over right, toe-touch", "Right leg over left, toe-touch"]
    ],
    "sing_hamstring_sit": [
        ["Sitting toe-touch reach", "Left leg out, toe-touch", "Right leg out, toe-touch"], 
        ["Sitting toe touch", "Sitting left leg extension hold", "Sitting right leg extension hold"]
    ],   
    "splits_stand":[
        ["Center split", "left side-lunge", "right side-lunge"]
    ],
    "splits_sit":[
        ["Center split", "Left front-split", "Right front-split"]
    ], 
    "tricep_stretch": [
        # ["Left tricep stretch squats", "Right tricep stretch squats"],
        # ["Left tricep stretch side-to-side step", "Right tricep stretch side-to-side step"],
        ["Left tricep stretch, ankle raises", "Right tricep stretch, ankle raises"],
        ["Left tricep stretch, high-knee lifts", "Right tricep stretch, high-knee lifts"]
    ],
    "wrists":[
        ["Arms up, wrist-rotations", "Arms out to sides, counter wrist-rotations"], 
        ["basic in-and-out wrist circles"],      
        ["3-count, X, Y, T, wrist rotations"], # "XYT, or "exit" dancer's wrist rotations, arms out, hug in for x, rotating wrists with each move                                                    
        # ["clockwise wrist-rotations", "counter-clockwise wrist-rotations"], 
        ["5-count yak's tax, wrist rotations"] # ADV. "Yak's Tax" means Y-A-X-T-X
        ["Cat's claw wrist bends", "thriller-pose wrist circles"], # side to side doing the car pose, forearm stretch ! be sure to go all the way up and all the way down with a wrist flap at the peak of each thriller pose
        # Alternating palm-down forearm raises
    ]  
}
master_warmup_dic ={
    # special selection keywords?
    "abs_work": [
        "Slow tension standing bicycles", 
        "windmill toe touches",
        "windmill sky chops", 
        "stellar windmills",
        "belly dancer kicks", # high knees if no space for it
        "Torso twisting slow side punches",
        "Lighthouse torso twists",
        "Cross-core knee strike",
        "torso twist, alternating lunges",
        "squat between standing bicycles",
        "straight-leg toe taps",
        "draw sword, side-bend",
        "Torso twist hip taps",
        "Open hip, straight high-knees"
    ],
    "bicep_work":[
        "curl to overhead press", 
        "biceb curl fly press", 
        "claw-hand Z-curls",
        "curl up, double punch out" 
        # biceb curl double punch
        # "mummy hug" # zombie curl, arms across chest, outward fly, clap in, z-curl down
        "claw-hand z-curl", 
        # "claw hand alternating bicep curls", 
        "barrel hug hammer curl", 
        # "sky scratchers" # "Volkenkratzer", claw pose biceb curl with mulitary press
        # Scary bear bicebs # claw pose biceb curl, arm rotation 
        # "45-degree palm press" # the bell-ringer
    ],
    "leg work, hard":[
        # "triangle pose side lunges", 
        "step-back lunges", 
        "three-point frog squats", 
        "squat pulse stand ups",
        # "prisoner squat to standing bicycle", 
        "squat to overhead press"
    ],
    "leg work, light":[
        # "marching zombie high knees", 
        "marching doll high knees", 
        "wall-crawlers" # "standing bird-dog reach"
        "heel-to-toe calf raises",
        # "point inward, point out calf raises", #turn on the heel
        # ["inward pointing calf-raises", "outward pointing calf-raises"]
        # "alternating reach and hip abduction" #reach with left arm as right leg goes out to side
        # "alternating forward single-leg reach" # stand on one leg, reach with both arms forward, keep back straight, come back up, switch.
    ],
    "pectoral_work":[
        # "Do the monkey!",
        "sky-punch fly press",
        "biceb curl fly press", 
        "single arm fly side-steps",
        # "arms fly out, double-punch forward", 
        # "hands-together up-and-downs", 
        # hands together, press up like hands together in tree pose, then down, like a lateral row
        "open hip thunderbolt palm press"
         # kneeling version lets you back bend for more range of movement
        # kneeling thunderbolt prayer,
        "X-Y fly press" # fly press, cross arms in an X, then arms go up to a y-pose, back in for X

    ],
    "shoulder_work":[
        # "arms out, tension wrist rotations",
        "four-count cheer squad", 
        # "wax on, wax off", # full motion to activate tricep
        "slow overhead lat pull-down"
        # "overhead lat pull down push-out"
        # "lateral pull down to shoulder shrug forward-back", 
        "single arm side-stepping sky punches", 
        "sky-punch, side stab",
        # "sky punch palm out, palm in",
        # "ankle raise, shoulder shrugs",
        # "ankle raise, big shoulder circles",
        "vampire wings" # from arms at sides, zombie claw up (for forearm tension), upward fly like opening a cape, arms rake down, picep curl inward, z-curl down to starting position

    ],
    "tricep_work":[
        # ["left overhead tricep tomahawk", "right overhead tricep tomahawk",]
        # ["side-step, side-stab"], # like a sideways chop, always keeping motion inward for play area
        # ["left tension tricep kickbacks", "right tension tricep kickbacks"],
        # "bodyweight tricep dips"
        "alternating hammer-downs", 
        "double-fang downward stabs"
    ],
    "wrists_work":[
        # "alternating claw-hand forearm raise", # same as zombie claw forearm raise, looks like frankenstein's monster
        "zombie claw forearm raise",
        "T-rex bicep curl", #wrists bent to add extra tension and activate forearms 
        "A-pose rotating claw-curls", #forearm tension, rotate to wrists-behind-back position, wrists tense back, then rotate to palm forward, wrists tense up and in
        "claw-hand Z-curls"
        # "arms forward, tension wrist rotations",
        # "arms out, tension wrist rotations" # crossover with shoulders
    ]
}

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
