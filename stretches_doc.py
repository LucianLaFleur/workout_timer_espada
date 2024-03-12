# NOTE: ALL [standing] variations are the last sub-array when multiple are avaliable (a mat/ floor may not be viable sometimes...)

# key string will always end with _stand or _sit for each exercise type
# intended to have either stand or sit as the key

centerpiece_abs_motions = [
"wall-crawlers",
"Side-chamber slugs",
"Left/right arm support, sweeping leg raise",
"squat axe handle uppercut",
]

abs_string_arr = [
    # exceptional focus on the core and on balanced footwork
    "Slow tension standing bicycles", 
    "windmill toe touches",
    "windmill sky chops", 
    "stellar windmills",
    "belly dancer kicks",
    # often done with weights or a medicine ball...
    "toso twist, alternating lunges",
    "squat between standing bicycles",
    # knee-tuck extensions, which is the single-side version of the standing bicycle as opposed to bicycles being opposite side, upper abs target
    "straight-leg toe taps",
    # legs straight, torso twist, but arms are up to assist with opening abs and targeting lower abdominals
    "draw sword, side-bend",
    # "the shy schoolgirl", single calf raise to pointed toe with the torso twisting
    "Torso twist hip taps",
    "Open hip, straight high-knees",
    # like you're grabbing a dude's head and driving it into your knee
    "Cross-core knee strike",
    # ADVANCED! No tension on back, slow motion, hold leg out and strengthen pelvis
    # "arm support, side-leg raise",
    # advanced 180 degree motion
    # "Arm support, sweeping left leg raise",
    # "Arm support, sweeping right leg raise",
    # "Lying left leg raise",
    # "Lying right leg raise"
    # opposite calf raise to reaching arm, tension !! not sluggers
    "Torso twisting slow side punches",
    # karate punch to side, then off-hand arm in chamber position, watch footwork for firm planting
    "Lighthouse torso twists",
    # "boxer's forward lean, back dodge cross"
    # "taunting sway cross",
    # "arms akimbo alternating side-bend",
    # "leg lifts",
    # "center row",
    # "center row, leg lift combo",

    # mirrored
    # "left lying hip-circles", "right lying hip circles"
    # "left side bends", "right side bends",
    #
    # Knee tuck focuses on lower abs from a standing position
    "Left/right out-step knee strike",
    # "right out-step knee strike",
    # big arm circle, little torso movement
    "Left/right arm circle torso rotations",
    # "right arm circle torso rotations",
    # full extension version of the petty bicycle
    # left three-quarters standing side-bend, cross
    "Left/right rock-and-box", 
    # "right rock-and-box",
    # keep hips open, knee forward, pull in with the abs, open with the hips
    "Left/right sky-punch knee-tuck",
    # "right sky-punch knee-tuck"
    # tree chopper sideways motion # kek, if it's a busty tomboy wearing a low tank top, it's great cleavage torso twists
    "Left/right great cleaver torso twists",
    # focus on balance, slightly forward with hips and back, but don't go ham with the pelvic thrust, your back should only bend slightly and not strain, keep eyes forward, do not look down-up at the same time... throws off balance
    # "heel toe rockers",
    
    #  NOT standing-friendly
    # "full extension starfish crunch",
    # "crab pose, half moon kicks", 
    # "seated scissor circles",
    # "left side-lying knee-to-elbow",
    # "right side-lying knee-to-elbow",
    # ADVANCED: "the venus fly trap tap", pull with obliques, side should not be hurting
    # "left side, leg-extended v-ups",
    # "right side, leg-extended v-ups",
    # "seated flutter kicks",
    # "basic upper abs crunch"
    # "tension scissor circles"
]

master_stretch_keyword_arr = [
    #  0 index is the standing version for all arrays
    ["back_stand", "back_sit"],
    ["calves_stand", "calves_sit"],
    ["glutes_stand", "glutes_sit"],
    ["hamstring_stand", "hamstring_sit"],
    ["neck"],
    ["quads_stand", "quads_sit"],
    ["sing_hamstring_stand", "sing_hamstring_sit"],
    ["splits_stand", "splits_sit"]
]

master_stretch_dic = {
    "back_stand": [["Left lunge torso turn", "Right lunge torso turn"], ["standing hula hip rotations, clockwise", "standing hula hip rotations, counter-clockwise"]],
    "back_sit": [["Left leg across, model pose", "Right leg across, model pose"]],
    "calves_stand":[["Left, standing forward lean calf stretch", "Right standing forward lean calf stretch"]],
    "calves_sit": [["Pike position, left cross calf stretch", "Pike position, left cross calf stretch"]],
    "glutes_stand": [["Standing left knee-tuck stretch", "Standing right knee-tuck stretch"], ["Left leg back, lunging stretch", "Right leg back, lunging stretch"]],
    "glutes_sit": [["Lying left knee-tuck stretch", "Lying right knee-tuck stretch"]],
    "hamstring_stand": [["Standing-v Left-leg", "Standing-v Right-leg", "Ginyu Force Center Salute"]],
    "hamstring_sit": [["V-sit Left", "V-sit Right", "V-sit Center"]],
    "neck": [["Look-up neck rotation", "Look-down neck rotation"]],
    "quads_stand":[["Standing quad stretch, left", "Standing quad stretch, right"]],
    "quads_sit": [["Lying quad stretch, left", "Lying quad stretch, right"]],
    "sing_hamstring_stand": [["Standing center toe-touch reach", "Left leg over right, toe-touch", "Right leg over left, toe-touch"]],
    "sing_hamstring_sit": [["Sitting toe-touch reach", "Left leg out, toe-touch", "Right leg out, toe-touch"], ["Sitting toe touch", "Sitting left leg extension hold", "Sitting right leg extension hold"]],   
    "splits_stand":[["Center split", "left side-lunge", "right side-lunge"]],
    "splits_sit":[["Center split", "Left front-split", "Right front-split"]], 
}

# ////////////// GENERAL warmups /////////

master_warmup_keyword_arr = [
    "ankles_work",
    "hips_work",
    "obliques_work",
    "shoulder_stretch",
    "tricep_stretch",
    "wrists_work"
]

master_warmup_dic ={
    "ankles_work":[
        ["Standing left ankle rotations", "Standing right ankle rotations"], 
        ["Sitting, both ankle rotations clockwise", "Sitting, both ankle rotations counter-clockwise"],
        ["Standing left toe point, heel point", "Standing right toe point, heel point"]
    ],
    "hips_work": [
        ["Lying left leg hip mobility circles", "Lying right leg hip mobility circles"],
        ["Standing left leg circles", "Standing right leg circles"],
        ["Standing left straight leg circles", "Standing right straight leg circles"],
        # crab pose, leg traces a half-moon shape then switch legs
        ["crab pose, half moon kicks", "seated scissor circles"]
    ],
    "obliques_work":[
        ["Left side bend", "Right side bend"],
        ["alternating ankle raise, side bend", "akimbo step and side-bend"],
        ["left boxer stance, sway punch", "right boxer stance, sway punch"],
        ["left three-quarters standing side-bend", "right three-quarters standing side-bend"]
    ],
    "shoulder_stretch":[
        ["Left arm-across, squats", "Right arm-across squatz"]
    ],
    "tricep_stretch": [
        ["Left tricep stretch squatz", "Right tricep stretch squatz"]
    ],
    "wrists_work":[
        ["Arms up, wrist-rotations", "Arms out to sides, wrist-rotations", "behind-the-back wrist rotations"],
        ["clockwise wrist-rotations", "counter-clockwise wrist-rotations", "side-to-side cat dance, wrist rotations"],
        ["palm-down fin flap", "palm up fin flap"], 
    #   also called the feline paw-flap and fairy flap
        ["arms out forward, fin flap", "arms out to sides, fin flap"]
    ],

    # special selection keywords?
    "abs_work": [
        "Slow tension standing bicycles", "windmill toe touches",
        # down for windmill, turn and reach up like karate chopping outward and up at a diagonal, then even yourself out before going down the opposite way
        "windmill sky chops", 
        # windmill, but move to opposite hand up to extended triangle pose, return to neutral before reaching down again
        "stellar windmills",
        # standing bicycle, but after doing each side, do a squat between
        "squat between standing bicycles",
        # the goose-step 
        "straight-leg toe taps",
        # Advanced move focusing on ab tension in seated position, tracing legs around an imaginary circle
        # "tension scissor circles"
        # squat, do the axe handle position of hands together, a slight torso twist, and pull up with obliques while pushing with legs to come up from the squat
        "squat axe handle uppercut",
        "full extension starfish crunch"
    ],
    "bicep_work":[
        "empty-handed curl and overhead press", "curl and bunch combo cycle", "empty-hand z-curl", "hammer curl, shoulder shrug"
    ],
    "shoulder_work":[
        "four-count cheer squad", 
        "lateral pull down to shoulder shrug forward-back", 
        "single arm side-stepping sky punches", 
        "sky-punch, side stab",
        # hands together, press up like hands together in tree pose, then down, like a lateral row
        # kneeling version lets you back bend for more range of movement
        "kneeling thunderbolt prayer press",
        "ankle raise, shoulder shrugs",
        "ankle raise, shoulder swimmers"
    ],
    "pectoral_work":[
        "single arm fly side-steps","arms fly out, punch forward", "finger laced up-and-downs", "thunderclaps (fly to palms together overhead position)"
    ],
    "leg work":[
        "sunrise squats (arm reach upward)","side-leg lunge-switch", "alternating high-knees", "jumping high knees",
    ]
}

# hip_moves = [["Lying left leg hip mobility circles", "Lying right leg hip mobility circles"],["Standing Left leg circles", "Standing Right leg circles"]]
shoulder_moves = ["Left arm-across, squats", "Right arm-across squatz"]
tricep_moves = ["Left tricep stretch squatz", "Right tricep stretch squatz"]
oblique_moves = ["Left side bend", "Right side bend"]
collection_of_warmup_moves = ["side-leg lunge-switch", "alternating high-knees", "jumping high knees",
                       "side-step and shrug", "empty-handed z-curl", 
                      "straight-leg cross-taps", "open oblique bicycles", "finger laced up-and-downs"
                    #   "the indecicive refrigerator"
                      "single arm fly side-steps","arms fly out, punch forward" # pectorals
                    #   left diag, right diag, up, out to sides
                      "four-count cheer squad", "lateral pull down to shoulder shrug forward-back", "single arm side-stepping sky punches", "sky-punch, side stab"]
# wrist_rotations = [["Arms up, wrist-rotations", "Arms out to sides, wrist-rotations", "behind-the-back wrist rotations"],["clockwise wrist-rotations", "counter-clockwise wrist-rotations", "side-to-side cat dance, wrist rotations"]]

# EXTRA WARM UP MOVES: standing hula hip rotations
# front and back leap-frogs.
# ! crouch walk
# gollum shuffle, left and right. gollum shuffle, triangle pattern
#  Sasquatch squat walk (lunge, up forward, squat, lunge back, squat, switch)
# side to side roll/sway evades?
# side to side bouncing hops, side to side pike jumps
# twist jacks # alternating lunges torso twists

# before workout checklist: make sure you know where your wall is IRL so you don't bump it, or you can reach out to balance. Will keep facing the same way, so you maintain orientation; room wall in vr will help orientation.
# pole friendly for support (though this is not a pole dancing class, if you know how, hit me up, I'd love to record and edit vids for you)
