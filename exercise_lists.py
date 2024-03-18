# legacy arrays
bodyweight_abs_single_motion_list = []
bodyweight_abs_dual_motion_list = []
arm_exercises = []
shoulder_exercises = []
ticep_exercises = []
all_exercise_keyword_list = []
# NOTE: need to remove above. currently maintained for functionality

# ------------------------------------------------------------------------------------------------------------------------------------
#  Bodyweight only / no equipment needed
# ------------------------------------------------------------------------------------------------------------------------------------ 
#  side-stepping helicopter torso twists
#  low block with arm, L/R
# High knee-circle half-step-back# start feet side by side, activate hip flexors and lower abs, lift knee, move to 3/4 stance, alternate
# hook punch, hook kick
# basic hook kick # no turn
#inner wheel kick, side kick
# outer wheel kick, cross punch
# deadlifts
#  ADVANCED (needs name: Way to wrap a push up in a compound)= lunge to single-knee down, single kneeling bell-ringer rope pull, push up position, rope pull again, then stand up, switch sides
# Research: single-arm row, upright row muscle groups

#  single leg RDL
#  both legs, forward-leaning RDL



#  scan through for medicine ball / weights variation moves
# duplicate exercises where secondary muscle group is targeted
# special array for multi-target compound move
# NYI: alternate arrs for heavy motions only and standing motions only
# tag exercises as heavy or not

potato = [
# [!] Abs  ------------------------------------------------------------------------------------------------------  
    # "kneeling torso twists",
    # lunge-switch torso twists # ADV. jumping lunge w.twist, high intensity 
    # "basic standing windmills",   
    # ["clock hula hips", "counter hula hips"],
    # Fencing exercises: L./R In/Out-block, lunge
    # stepping single lunge.
    #high guard, two-hand slash, alternate footwork, shoulder mobility exercise, light cardio
    # step-lunge to shuffle-lunge
    # guard and main gauche (florentine inner guard, offhand stab)
    # stepping arm-fly to cross crunch combo!
    # + Center abs target -------------------------
        # "Left/right arm support, sweeping leg raise",
        # "squat to axe handle uppercut"
        ["hip raise, leg extension"], #need Straight bark for it
        # lying leg-tuck cycle # Needs name, leg lift, then row extension, candle, controll down, cycle starts back to leg lift.
        ["boat row"], #rowboat leg extensions
        ["leg lifts, candle pose"],
        # [add l8r]: Turtle crunch
        # "basic leg lifts"
        # "L.Leg Ex. side-suitcase", "R.Leg Ex. side-suitcase"
        # "banana boat rocker", 
        # "left side-lying knee-to-elbow", "right side-lying knee-to-elbow",
   # + delts --------------------------------------------
    # "crab pose, half moon kicks",
    # ["Rev.Plank L.leg lifts", "Rev.Plank R.leg lifts"]
    # Cat's crescent moon # like bird dog, but you lift up with the extended leg and arm, like supermand
    # + hip flexors ---------------------------------
    # kneeling back lean # ADVANCED! No tension on back, slow motion, hold leg out and strengthen pelvis
    # "arm support, L.Leg abduction", # both arms are behind to support you, ADV is only one arm, leaning for greater range of motion
    # "arm support, R.Leg abduction",
    # "Arm support, sit.Left sweep",
    # "Arm support, sit.Right sweep", # ADV 180 degree motionleg sweep-across, mind the balls men  
    # + Lower Abs  ----------------------------------------
    # ++ compound for hip flexor, quad, lower ab
        # "bird dog crunch", # opposite arm and leg out, then bring in
        # "full extension starfish crunch",
        # "seated flutter kicks",
        # ["standing bird-dog reach"]
        # sitting leg lever # small range of motion leg raise, "the paperclip"
        ["wall-crawlers"],
        ["open-hip, str. high-knee"],
        ["flutter kicks"],
        # ["fasion model cross-crunch, left", "fasion model cross-crunch, right"], #"prisoner pose, out-step cross crunch"
        ["left lying hip-circles", "right lying hip circles"],
        ["L.out Knee Strike", "R.out Knee Strike"], # like you're grabbing a dude's head and driving it into your knee
        # "prison pose high knees" #target lower abs 
        # "seated scissor circles",
        # ADVANCED: "the venus fly trap tap", pull with obliques, side should not be hurting
    # pike position,single leg back kick extension to plank knee tuck, on same leg, alternating
    # single side verions of ^^
    # ++ compound for hip flexor, quad, lower ab, shoulder----------------------------------------
        #  "dancing downward dog", !!! voice line exists
        ["full extension cross-crunch"],
        ["cross-core knee strike"],
        # out-step knee-tuck extensions, which is the single-side version of the standing bicycle as opposed to bicycles being opposite side, upper abs target
        # straight, single knee-tuck extensions
    # ++ Compound, hip flexor, quad----------------------------------------
        ["belly dancer kicks"], # legs straight, torso twist, but arms are up to assist with opening abs and targeting lower abdominals
        ["half windshield wiper combo"], # l8r need expansion on windshield wiper moves
        # single leg windshield wiper
        # seated leg lever
        # ["Lying left leg raise", "Lying right leg raise"]
        # ["standing single leg hip circles"],
        # ["reverse plank, flutter kicks"]  
        # lying six o'clock tick-tock, leg lift, hup abduction one at a time motion...
    # + Obliques  ---------------------------------------------------------------------------
        ["side-slugger torso twist"], # # karate punch to side, then off-hand arm in chamber position, watch footwork for firm planting
        ["lighthouse torso twists"],# opposite calf raise to reaching arm, tension !! not sluggers
        # ["Left hip raise", "Right hip raise"],# small rage of motion, big burn
        ["oblique heel-taps"],
        ["windshield wiper leg lifts"],
        ["seated russian twists"],
        # ["left side bends", "right side bends"],
        ["torso twist hip taps"],# "the shy schoolgirl", "punchdown hip taps" single calf raise to pointed toe with the torso twisting
        ["draw sword, side-bend"],
        # ["L.Ax-handle pull-downs","R.Ax-handle pull-downs"] # stab enemy behind with reverse grip under the armpit
        # ["Alt. Ax-handle pull-down"]
        # ["Sit L.Ax-handle P.D","Sit R.Ax-handle P.D"] #   
        # ["Sit Alt. Ax-handle P.D"] #high verison of a russian twist
        # L/R V-Up lateral Lying lateral leg-lift # Heavy!
        # lying L/R hip-up
        # "arms akimbo alternating side-bend",
        #  ^^ make Left/Right variations of above and alternating voice bark
    # + Shoulders --------------------------------------------------------------------------------
        ["L. rock-and-box", "R. rock-and-box"],
         # left three-quarters standing side-bend, cross
    # + Upper abs -------------------------------------------------------------------------------------
        # "open-hip T-bolt pr.ess":["stretch_auds/.wav"],
        # ["basic upper-abs crunch"],
    # + Unknown / research needed ------------------------------------------------------------------
        ["half-bridge hip-thrusts"],
        ["heels to the heavens"],
        ["slow stand. Bicycles"],
        ["stellar windmills"],
        ["straight-leg toe taps"],
        ["windmill toe touches"],
        ["windmill sky chops"],
        ["wood chopper oblique"], #also baseball swing oblique       
#       ["figure-eight obliques"] # hands are clasped for the double ax-handle figure-eight obliques

# [!] Biceps ------------------------------------------------------------------------------------------------------
        # ["Left lying bicep press"], ["Right lying bicep press"],
        # ["L/R seated single-arm curl"],
    # + Pecs ----------------------------------------------------------------
        ["barrel hug hammer curl"], #unique compound
        ["biceb curl fly press"],
    # + Delts, upper chest, traps (with military press) ----------------------------------------
        ["curl, overhead press"],
    # + Delts ----------------------------------------------------------------
        ["curl & double punch out"], # The Greaser's jacket
    # + Forearm ----------------------------------------------------------------
        # with knee-ups = stalking raptor
        ["A-pose ro. claw-curls"],
        ["shrieking ghoul"],
        # "basic hammer curl":["stretch_auds/mori_alt_basicHammerCurls.wav"],   
        #  Hammer curl to wrist rotation # compound
        # wrist rotations
    # + Tricep & forearm ----------------------------------------------------------------
        ["alternating hammer-downs"],
        # ["lying crunch biceb curl"], # seated hip-up bicep curl # "AT-field curls", because zettai ryouiki
        # ["lying towel crunch biceb curl"], 
        # ["lying towel hammer curl"],  

# [!] Calves -------------------------------------------
        ["heel toe rockers"],
        #  squatting position tip-toes # an ankle-raise motion while squatting
        # "squat to ankle stand-up" # keep butt out or it'll hurt your back, tighten core, arms out front for balance, should feel in top of leg
        # "ankle hops", 
        # "pidgeon toe inner pointing calf raise", 
        # "toes pointed outward calf raise", 
        # "side-to-side swaying ankle raise", 
        # "side lunge boxer's roll ankle raise"
        # ["Seated knee up toe-point, heel point"], 
        # ["seated boat isometric"], 
        # ["toe-point heel-point"]
 #  ALL ankle hop agility patterns ----------------------------------------------------------------
        # ["side-to-side small ankle-hops"] cardio, step out, shift weight, feet together, step out other way; these are not full lunges and maintain tension in calves
        # ["forward-stepping,  ankle hops"]
        # ["chevron ankle hops"] inverted V formation movement
        # ["back-stepping ankle hops"] # needs name:start w/feet together, one foot back, together, other back, together, bounce on ankles /chevron-pattern footwork, 3/4 boxing stance ankle hop
        # ["lateral bunny-hops"] # both feet
        #["forward-back bunny hops"]
        # ["diamond bunny hops"]
        
# [!] Delts -------------------------------------------------------------------------
    # very focused on delts ----------------------------------------------------------------
        # goblet halos # circle head with the weight, keeping arms up; often done with a barbell plate
        ["pike push-up"], # & pecs
        # handstand push-up / inverted push-up
        ["T-Y-A arms-out shoulder circles"],
        ["T-plank Ro. push-ups"], #push up, rotate to left side plank, [hip up], back to plank, push, alternate T-plank
    # + abs ----------------------------------------------------------------
        # "slo-mo mountain climbers", # Heavy
        # seated/standing boat row motion
        # canoe oar motion # The gondala driver
        #  crocodile crawl, cat crawl, ape traversal, frog crawl
        ["bear crawl"],
        ["slow and low crawl"],
        # ADV: spinning crab compound. Crab to side T-plank
        # ["walk the plank"], # stand, down to plank, [push-up], walk-up # inchworm
        # ["pike-to plank walk-out"],
        # Pike position, bird-dog bear crawl
        # triangle pattern ape-mover/traversal, knuckledragger
        # ["Left single-arm crab-reach"], ["Right single-arm crab-reach"]
        # ["Alternating Moscow T-planks"],
        # ["alternating crab bridge reaches"],
        #  ["plank-tuck push-up"], #tuck legs in after each rep, a bit cardio focused
    # + hamstrings ----------------------------------------------------------------
        # ["push-up pop-ups"], # ADV. Burpee pushup -> stand, crouch to plank, push up, come back up
    # + hip flexors ----------------------------------------------------------------
        # ["cross-body push up"], # kick leg across as you go down. Alternate
    # + obliques ----------------------------------------------------------------
        # "boxer's forward lean, back dodge cross" #muscle group needs confirmation
        # "taunting sway cross",
        ["back-stroke torso twist"],
        ["pike position cross toe-touches"],
    #  + Pectorals ----------------------------------------------------------------
        #  "part the curtains" # half-breast stroke in and out motion like a fly with palms facing out left and right, 
        # "Standing swim, breast-stroke" # same motion as swimmin, both arms out at same time, scoop the water back
        ["plank shoulder taps"],
        # ["staggered push-ups"],
        # wax on, wax off
        # L/R outward arm block, 
        # L/R upper arm block
        # L/R upper arm block to cross-punch
        #  Alligator Pushup # ADV
        # Florentine scissor # the movie thing of slashing both swords at once that's ahistorical but cool
    # + quads  ----------------------------------------------------------------
        # Alternating lunge-down push-ups# stand, lunge back-step, down to plank, push up, knee up, press up on knee to stand
        # L/R lunge-down push-ups
    # + Triceps ----------------------------------------------------------------
        # ["pseudo-plance push-up"] # fingers outward, forward-leaning pushup
        ["sky-punch, side stab"],
        # ["sumo-squat push-ups"], 
        # ["frog stand to ukemi"],
        # ["dive-bomber push-up"],  # ADV compound and pecs
    # + Compounds ----------------------------------------------------------------
        # "superman punch" ADV # simplified as step-punch
        # "ankle raise, shoulder shrugs",
        # "ankle raise, big shoulder circles"   
        # Floor jack pike # push-up position, then legs spread, together, tuck in, then back to normal push-up position
        #  hip-to-hip barrel mover# some pectoral focus \ quad activation version ADV, like tai-chiwide stance, alternating weight as moving arms like picking up a barrel and placing it down)
        # kamehamehas with quad activation swaying 

# [!] Forearms ------------------------------------------------------------------------------------------------------
        ["claw-hand Z-curls"],
        # arms out wrist-bend claws s the jiangshi move
        ["zombie claw f.Arm Raise"],
        ["marching zombie high knees"],
        #  T-pose, claw-hand wrist curl rotations # needs name
        # Scary bear biceb fly press # claw pose biceb curl, fly press 
        # "claw hand alternating bicep curls", 
        # "T-rex hammer curl", # Ovoraptor, wrists bent in, palms facing toward each other like holding a giant egg, to add extra tension and activate forearms 
        # ["T-rex bicep curl"], claw pose forearm raise
        # alt T-rex bicep curl = godzilla on a rampage# alternaring claw-hand forearm raise
        # "mummy hug" # ADV. compound zombie curl, arms across chest, outward fly, clap in, z-curl down
        # ["behind-the-back wrist flex"], # back of the hand is skyward 
        # ["A-pose inner wrist curls"], # palm is skyward
        # ["A-pose hammer curl to chest"]
        # ["A-pose small chops up and down"]
        # ["Cat's claw wrist bends", "thriller-pose wrist circles"], # side to side doing the car pose, forearm stretch ! be sure to go all the way up and all the way down with a wrist flap at the peak of each thriller pose
    # + delts ----------------------------------------------------------------
        # "sky scratchers" # "Volkenkratzer", claw scratch up, scratch down
        # alternating sky scratchers... feral looking
        # T-pose forearm rotations
        # ["arms forward, fin flap", "arms out to sides, fin flap"] #   also called the feline paw-flap and fairy/penguin flap
        # palm-down/palm up wrist curls
        # ["3-count, X, Y, T, wrist rotations"], # "XYT, or "exit" dancer's wrist rotations, arms out, hug in for x, rotating wrists with each move                                                     
        # ["5-count yak's tax, wrist rotations"] # ADV. "Yak's Tax" means Y-A-X-T-X

# [!] Glutes ---------------------------------------------------------------------------
        # basic side lunges
        # back-kicks
        # cat-pose back kicks
        # all-fours upward mule kicks
        # all-fours upward kick, back kick
        # hip flexor fire hydrant
        # L/R side kick # back foot in 3/4
        # low side-kick stomp
        # shuffle side-kick # front foot
        # front+side kick combo
        # compound fire hydrant, mule kick upwards, straight kick backwards, L/R variation
        # side lunge cross punches #horse stance, low dodge, oblique for punch tension
        # side lunge windmills (stay low with the wide stance, good for thighs)
        # forward-leaning RDL #lean forward, kick back
        # ["deadlift"]
        # ["single-leg RDL"]
        # NOTE: needs name: arms out squat position to toe touch

# [!] Hamstrings ---------------------------------------------------------------------------------------------------
    # + Delts only
        # "sumo palm-strike squats (palm strike at the bottom and top, left, left, then right right on next rep)"
    # + Delts, traps
        ["squat to overhead press"], # AUD: the superhero lift
        # "squat between standing bicycles", # standing bicycle, but after doing each side, do a squat between
        ["sunrise squats"], # like outlining a big circle with hands, palms facing forward, full arm extension
    # forearms ----------------------------------------------------------------
    # hay bale squats #Slavic A-pose squat press, hammer-curl, military press, # dynamic/explosive #motion like squatting down to pick up a hay bale, then pushing it to throw it in the pickup truck
    # 7-count A-frame forearm: needs name: A-pose squat, romanian deadlift, forearm raise, wrist forearm curl
    # lower abs ----------------------------------------------------------------
        # tuck jumps
    # upper abs ----------------------------------------------------------------
        # ["prisoner squat to ramping bicycle"] # ADV: start with one bicycle between squats, increase it with each rep for time duration. NOTE: can be made into own function for compatible items... maybe a new keyword like "ramping" for info array
    # + Compound ----------------------------------------------------------------
        # slav squat, forearm raise # needs name
        # slav squat, forearm raise, military press # needs name
        # ["squat to rising uppercut"], 
        # burpees # stand, crouch to plank, push up, jump up
        # pike-jack purpee jumps # ADV. impact
        # "squat between standing bicycles",
        # grounded A-pose squat (swing arms to activate triceps)
        # side to side tuck-jumps # ADV. impact
        # floor jack tuck jumps (ADV, compound)

# [!] Hip Flexors ----------------------------------------------------------------------------------------
        ["L.side hip abduction", "R.Side hip abduction"],
        # "jumpy alternating high knees",
        #  "skipping motion high knees" 
        # "puppet string knee raise" # compound :"the bootstrap", like standing bird dog, but on same side, forearm raise, like you have an imaginary rope looped under your heel and you're picking your foot up
    # + Center abs ----------------------------------------------------------------
        # heel press seated row # lotus position, move in and out
        # the leggy venus fly-trap and pull-in # overly possessive girlfriend secret inner thigh no-jutsu
        # scissor lotus abduction # v-sit with legs out, brings legs in for indian-style sit, then out to V again, alternating which leg crosses in on top. Tap opposite heel to hamstring on inner position, V sit is outer position.#   --  AKA -> criss-cross applesauce
    # + Lower abs ----------------------------------------------------------------
        # L/R lying scissor-kick
    # + Delts ---------------------------------------------------------------- 
        ["marching doll high knee"],
    # + Pecs ----------------------------------------------------------------
        # ["push-up to kneeling lean-back crunch"] #needs name
    
# [!] Pectorals ----------------------------------------------------------------------------------------------------
        ["sing. arm fly side-step"],
        # "Do the monkey!",
        # ["The Pharoh's Salute"] # x across chest
        # ["Cheering Pharoh"] # X across chest, y hands, high tricep extension
        # ["Peking sword salute"] # sing. arm variation of cheering pharoh is  (pec. and sword salute), knuckle tap opposite pec, arm at 45 degrees to side, reach back for tricep extension, pump and pull back to start 
        # *alligator arms (left top, right top, switch)
        # empty hand straight-arm fly
        # lying empty hand fly
        # palm press offering / palm press give and take
        # Water wheel palm press # imagine a big wheel that you have to close your palms over and rotate in a circle back and forth
        # *fly clap palm press pull # a "gathering in" motion focusing on pec tension
        # Spiderman push-up
        # thunderclap # thunderbolt pose palm press, up and out to t pose, clap in a fly
        # side to side kamehamehas
        # front kamehamehas
    # + Delts ----------------------------------------------------------------
        # "hands-together up-and-downs", # prayer press or thunderbolt
        ["sky-punch fly press"],
        ["vampire wings"],
        ["X-Y fly press"],
        # "open hip thunderbolt palm press"# hands together, press up like hands together in tree pose, then down, like a lateral row
        # "knuckle-pecks" #tap chest like knocking on a door, right kuckles to left collarbone
    # + Obliques ---------------------------------------------------------------- 
        # ["Spiderman push-up"]
    # + Quads ----------------------------------------------------------------
        ["thunderbolts between lunges"],
    # + Traps ----------------------------------------------------------------
        ["closet door open-and-shut"],
        ["reverse-palm push-up"],
        # ["45-degree palm press"] # the bell-ringer
        # ["wide-arm push-up"], ["archer push-up"]
    # compound, multiple ----------------------------------------------------------------
        # "florentine 1-2":["stretch_auds/mori_florentine12.wav", "stretch_auds/mori_florentineone-two.wav"],

# [!] Quads -----------------------------------------------------------------------------------------------------     
        ["squat pulse stand-ups"],
        ["3-point frog squats"],
        ["step-back lunges"],
        # l/r crouching archer pulls #the sneaking ranger, crouching sideways archer pull# same as 3-point frog squat
        # goblet squat pulse
        # goblet squat-pulse stand-ups
        # goblet side lunges
        # l/r step-out side-lunges
        # L/R 3-point pose side lunge
        # alternating side-lunges
        # curtsey squats  Research muscle and how-to
    # + Upper abs ----------------------------------------------------------------
        # "elbow to knee, squat isometric" 
    # + Oblique ----------------------------------------------------------------
        ["alt. torso-twist lunges"],
        # lunge down to plank, alternate legs while rising. Start with the right leg (audio direct.)
        # squat-between stepping lunges
        # "seiza to kneeling warrior, alternating arms"
        # comound fly press lunge
        # Sasquatch squat walk, arms sway to the side, two step forward, legs together, alternate leg (planting one foot at a time), always twisting toward the knee that's forward, if exhausted, can rest on that knee and push yourself up from it
        # "sumo stomp squats"
        # ADV: crouch walk: crouch walk, stand up, keep feet shoulder-width apart, bend your knees, feet together before standing up, do not put pressure on your back, you may need to bend lower to do so
        # "low squat pulse",
    # Pecs ----------------------------------------------------------------
        # ["Push-up between alternating lunges"]
    # + Traps ----------------------------------------------------------------
        # ["alternating lunge to warrior arher"] # kneeling archery shots 
    # + Compound / other ----------------------------------------------------------------
        # roundhouse kick
        # low-mid roundhouse kick (same side)
        # ["invisible barbell deadlift press"] # imaginary barbell, deadlift, forearm raise, overhead press
#  [!] Traps --------------------------------------------------------
        # alternating back-stroke arm rotations
        # double back-stroke arm rotations
        # double forward stroke arm rotation # Standing butterfly swimmer
        ["4-count cheer squad"], #  left diag, right diag, out to sides while bending back, arms swing forward, pump both arms up
                                 #  On diagonals the opposite leg steps out for support
        ["lat pull-down push-out"],
        # "overhead lat pull down push-out"
        # "standing lateral pull down to shoulder shrug forward-back",
        # "kneeling lat pull down push out with hip flexion"
        # "lying over-under lat-pulls" (towel pull behind head, then under to collar bone, repeat motion)
        ["lying lat pull-downs"],
        ["sing.Side-step sky-punch"],
        ["slow lat pull-down"],
        ["flying cobra"],
        ["lat pull-down push-out"],
        ["lying lat pull-downs"],
        ["pike position cross toe-touches"],
        ["reaching row"],
        ["snow angel shoulders"],
        ["supermans"],
        ["tension lat pull-downs"],
        # ["lying splash-back reach-outs"]
        # alternating single-arm reaching row; freestyle superman swimmer, one arm at a time, then rotate.
    # + Obliques ----------------------------------------------------------------
        # single-side bellringer rope-pulls 
        # alternating bell ringer rope pulls
        # "criss-cross bellringer punchdowns": 45-degree rope pull motion, then hip tap the opposite side (the punchdown). Grab star fom the sky, put it in the pocket, no the opposite pocket
    # + Delts ----------------------------------------------------------------
        #["L\R archer pull"] 
        #["saggitarius archer pull" ] # 45-degree angle up and alternating 
        # ["4-count archer pulls"] # 45-degree L/R, straight L/R
    # + Pecs ----------------------------------------------------------------
        # gorilla archers # archer pull, but on draw, supporting hand comes in for a chest thump, then alternate sides
    # + Triceps ----------------------------------------------------------------
        # Archer pull to side-knife stab # pulling arm pulls and holds, "bow-holding" hand comes in to chest # ^^ no irl analogue, so it's like taunting a goblin to come close since you're using a bow, but the bow is an illusion and it's actually a knife, so you ready up to hit them properly

# [!] Triceps ------------------------------------------------------------------------------------------------------
        # "tricep dips", 
        # *unnamed: upper chicken wing position, over chop, under chop
        # leg out tricep dips
        #  crab position tricep dips
        # "dolphin push-up", # sphynx to pike transition
        # "plank to seal-pose", 
        # ["tricep get-ups"],
        # "left tricep kickbacks", "right tricep kickbacks"
        # victory cheer tricep extensions #arm up in Y position to do it
        #  overhead goblet tricep extension
        #  goblet squat tricep extension
        # goblet raise between alternating lunges
        # side to side upward arcing tricep extension # from upper chicken wing position
    # + Bicep ----------------------------------------------------------------
        # high hammer curls, low hammer curls
        # "left overhead tricep extension":["exercise_names/mori_leftOverheadTriExtension.wav"]
        # "right overhead tricep extension":["exercise_names/mori_RtOverheadTriExtension.wav", "exercise_names/mori_RtOverheadTriExtension.wav"] 
        # "chop out, scrape in":["stretch_auds/.wav"], # compound, push and pull
    # + Delts ----------------------------------------------------------------
        # ["sphynx push-up"],
        ["double-fang down-stab"]
        # Alternating akimbo tomahawks # like weilding hatchets, X motion of slashes, but one at a time
        # "ice cliff climber" #focus on tricep tension, climbing motion as if having daggers in reverse grip and climbing up a wall
        # ["L.3/4 Stance Hatchet", "R.3/4 Stance Hatchet"], #one arm at a time, full range of motion for tricep dip back, full slash forward
        # draw double swords from back, (the elephant tusk backpack)
        # double-back sword, downward swing.
        # Db.Bk.Swo. cross slash, in, out, sheathe
        # Db.Bk.Swo.slash down stab out front, stab out to sides 
        # rainbow wave - high chiken wing position, tricep extension, like waving to someone far away to flag em down.
        # alt. rainbow wave - left wave, right wave, repeat
        # "Yawnining tricep extension" # chicken wing position, but palms out, above shouldersarms are going up against gravity, bending at the elbow
    # + Pecs ----------------------------------------------------------------
        # ["diamond pushup"],
        # ["elbows-back Tri. push-ups"],
    # + Forearms ----------------------------------------------------------------
        #  Double chop pulse : Arms at sides, hammer curl, karate chop hands full wrist extension, then at bottom position with arms at waist, wrists go down and up
    # + Compound ----------------------------------------------------------------
        # "high-hammer curls": ["stretch_auds/mori_highHammerCurl.wav"],
        # "Alt. high-hammer curls": ["stretch_auds/mori_altHighHammerCurls.wav"],

#  STRETCHES ARE KEPT IN SEPARATE DOC!!! -------------------------------------
# NOTE:  JUST A BACKUP
# [!] Stretches ------------------------------------------------------------------------------------------------------
        # "R.Stand ankle rotations":["stretch_auds/.wav"],
        # "L.Stand ankle rotations":["stretch_auds/.wav"],
        # "L.Stand heel-to-toe point":["stretch_auds/.wav"],
        # "R.Stand heel-to-toe point":["stretch_auds/.wav"],
        # "L.Arm Across high-knees":["stretch_auds/.wav"], 
        # "R.Arm Across high-knees":["stretch_auds/.wav"],
        # "L.Arm Across side step":["stretch_auds/.wav"], 
        # "R.Arm Across side step":["stretch_auds/.wav"],
        # "L. Tri. & ankle raises":["stretch_auds/.wav"], 
        # "R. Tri. & ankle raises":["stretch_auds/.wav"],
        # "L. Tri. & high-knees":["stretch_auds/.wav"], 
        # "R. Tri. & high-knees":["stretch_auds/.wav"],
        # "Arms up, wrist-ro.":["stretch_auds/.wav"], 
        # "Arms out, wrist-ro.":["stretch_auds/.wav"],
        # "X-Y-T Wrist rotations":["stretch_auds/.wav"], 
        # "Down In/Out Wrist Cir.":["stretch_auds/.wav"],
        # "Y-A-X-T-X, wrist ro.":["stretch_auds/.wav"], 
        # "Down In/Out Wrist Cir.":["stretch_auds/.wav"],
        # "Cat's claw wrist bends":["stretch_auds/.wav"], 
        # "thriller wrist cir.":["stretch_auds/.wav"],

        # "L.Lunge torso turn":["stretch_auds/me_leftLungeTrianglePose.wav"],
        # "R.Lunge torso turn":["stretch_auds/me_rightLungeTrianglePose.wav"],
        # "clock hula hips":["stretch_auds/me_standingHulaHipRotations_clockwise.wav"],
        # "counter hula hips" :["stretch_auds/me_standingHulaHipRotations_counterclockwise.wav"],
        # "L.Leg cross model pose":["stretch_auds/me_leftlegAcrossmodelpose.wav"],
        # "R.Leg cross model pose":["stretch_auds/me_rightLegAcrossModelPose.wav"],
        # "L-stand fw-lean calf":["stretch_auds/mori_standLeftLeanCalfStretch.wav", "stretch_auds/mori_leftLegStandLeanForwardCalf2.wav", "stretch_auds/me_leftstandingforwardleaningcalfStretch.wav"],
        # "R-stand fw-lean calf":["stretch_auds/mori_StandRightCalfStretch2.wav", "stretch_auds/mori_right_leg_calfStretch1.wav"],
        # "Pike, L-calf stretch":["stretch_auds/me_pikePositionleftCrossCalfStretch.wav"],
        # "Pike, R-calf stretch":["stretch_auds/me_pikePositionRightCrossCalfStretch.wav"],
        # "Stand L. knee-tuck":["stretch_auds/mori_standingLeftKneeTuckHold.wav"],
        # "Stand R. knee-tuck":["stretch_auds/mori_standingRightkneeTuckHold.wav"],
        # "L.back, lunging stretch":["stretch_auds/mori_leftlegBackLungingStretch.wav"],
        # "R.back, lunging stretch":["stretch_auds/mori_rightLegBackLungingStretch.wav"],
        # "Lying L-knee-tuck":["stretch_auds/mori_lyingleftKneeTuckStretch.wav"],
        # "Lying R-knee-tuck":["stretch_auds/mori_lyingRightKneeTuckStretch.wav"],
        # "Stand-V Left-leg":["stretch_auds/mori_standingVLeftLeg.wav"],
        # "Stand-V Right-leg":["stretch_auds/mori_standingVRightLeg.wav"],
        # "Stand-V center":["stretch_auds/mori_standingVCenterStretch.wav"],
        # "V-sit Left":["stretch_auds/me_standingVLeftLeg.wav"],
        # "V-sit Right":["stretch_auds/me_standingVRightLeg.wav"],
        # "V-sit Center":["stretch_auds/me_standingVCenterStretch.wav"],
        # "Look-up neck ro.":["stretch_auds/mori_upperHalfCircleNeckRotation.wav"],
        # "Look-down neck ro.":["stretch_auds/mori_downwardhalfCircleNeckRotation.wav"],
        # "L.Stand quad pull":["stretch_auds/me_standingleftquadStretch.wav"],
        # "R.Stand quad pull":["stretch_auds/me_standingRightQuadStretch.wav"],
        # "L.Lying quad stretch":["stretch_auds/me_lyingLeftQuedStretch.wav"],
        # "R.Lying quad stretch":["stretch_auds/me_lyingRightQuadStretch.wav"],
        # "Stand.Center toe-touch":["stretch_auds/me_Standing_center_toe_touch_reach.wav"],
        # "L.Over toe-touch":["stretch_auds/me_leftLegoverrighttoetouch.wav"],
        # "R.Over toe-touch":["stretch_auds/me_rightlegOverLeftToeTouch.wav"],
        # "Sit.Toe-touch":["stretch_auds/me_sittingtoetouchreach.wav","stretch_auds/me_sittingToeTouchReach2.wav"],
        # "L.Leg out, toe-touch":["stretch_auds/me_leftLegOutToeTouchReach.wav"],
        # "R.Leg out, toe-touch":["stretch_auds/me_rightlegOutToeTouchReach.wav"],
        # "Sit L.Extension hold":["stretch_auds/me_sittingLeftLegExtensionHold.wav"],
        # "Sit R.Extension hold":["stretch_auds/me_sittingRightLegExtensionHold.wav"],   
        # "Center split":["stretch_auds/me_centerSplit.wav"],
        # "Left side-lunge":["stretch_auds/me_leftSideLunge.wav"],
        # "Right side-lunge":["stretch_auds/me_rightSideLunge.wav"],
        # "Left front-split":["stretch_auds/me_leftFrontSplit.wav"],
        # "Right front-split":["stretch_auds/me_rightFrontSplit.wav"],

    ]


# ----------------
# Jokes, etc.
# tree chopper sideways motion # kek, if it's a busty tomboy wearing a low tank top, it's great cleavage torso twists
  # ----------------
#   squat to alternating sky punches
#  alternating rising uppercuts

# how to dance and dancer exercises:
    # downward palm press opposite knee raise
# forearm wrist flap alternate positions as headpats
# reaching clench: overhead, T-pose, behind back, out front
# forearm reaching clench at 3/4 position, like grasping swallow-tail in tai-chi
# alternating basic bicep curl
# Frankenstein arm raise, delts

    # fencer moves need SALVAGE; R: footwork exercises
# side to side roll/sway evades? BOXING exercises
# step lunge to kneeling 3-point lunge
#  R: brazillian jui jitsu and muy thai training exercises
# R: Yoga exercises
# need to research moves for upper and lower pecs
# R : different kinds of pull-ups
# R: other martial arts kicks for training
# ! need to explain positioning, back foot bend, toe front pointed, still like 80/20, supporting, Knee never bends over toes for threat of hurting knee and off-balance
