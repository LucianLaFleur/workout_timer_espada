import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random
import pygame
import math
import time
import threading
import audio_doc
import stretches_doc
import exercise_lists
import make_martial_arts

# -------------- Color scheme note for other tabs -----------------------------------
   # Main color BG: DARK PURPLE: #27233A 
    # aquamarine  52FFB8
    # carmine #931621
    # saffron #F9C22E
    # timberwolf grey #D5C7BC
    # hunter green #34623F
    # lemon chiffon #FEF6C9
    # wisteria #BEA7E5
    # field drab (olive, dark) #73683B
    # ice blue  #9BF3F0
    # honolulu blue #0077B6
    # sienna 	#A0522D
# -------------- / Color scheme note  -----------------------------------------------
# -------------- For martial arts audio with 43e's voice -----------------------------------
voice_43e_dictionary = {
    "backhand": "martial_audio/43e_backhand1.wav",
    "backstep": "martial_audio/43e_backstep_util.wav",
    "back-sway": "martial_audio/43e_backSway.wav",
    "bell clap": "martial_audio/43e_bellClap.wav",
    "chain punch": "martial_audio/43e_chainPunch.wav",
    "choke slam": "martial_audio/43e_chokeSlam.wav",
    "cross-punch": "martial_audio/43e_crossPunch.wav",
    "cross-to-knee": "martial_audio/43e_crossToKnee.wav",
    "cross palm strike": "martial_audio/43e_crosstoPalmStrike.wav",
    "cross to shuffle punch": "martial_audio/43e_crossToShufflePunch.wav",
    "double-arm shove":"martial_audio/43e_doubleArmShove.wav",
    "ducking sway":"martial_audio/43e_duckingSway.wav",
    "downward elbow strike":"martial_audio/43e_downwardElbowStrike.wav",
    "elbow jab":"martial_audio/43e_elbowJab1.wav",
    "elbow smash":"martial_audio/43e_elbowSmash.wav",
    "falling double axe handle": "martial_audio/43e_fallingDoubleAxeHandle.wav",
    "feinting hook, true jab" :"martial_audio/43e_feintHookJab.wav",
    "feinting cross":"martial_audio/43e_feintingCross343.wav",
    "feinting cross, side chop":"martial_audio/43e_feintingCrossSideChop.wav",
    "feinting hook":"martial_audio/43e_feintingHook.wav",
    "feinting hook, shove":"martial_audio/43e_feintingHookShove.wav",
    "feinting jab":"martial_audio/43e_feintingJab.wav",
    "feinting jab, true cross":"martial_audio/43e_feintJabTrueCross.wav",
    "knee-feint":"martial_audio/43e_feintKnee_2.wav",
    "gut punch":"martial_audio/43e_gutPunch.wav",
    "heavy palm strike":"martial_audio/43e_heavyPalmStrike.wav",
    "high block":"martial_audio/43e_highBlock.wav",
    # :"martial_audio/43e_highFullRedirection.wav",
    "hooking knee strike":"martial_audio/43e_hookingKneeStrike.wav",
    "hook, shove":"martial_audio/43e_hookShove.wav",
    "inner parry":"martial_audio/43e_innerParry.wav",
    # :"martial_audio/43e_inwardFullRedirection.wav",
    "in-sway" :"martial_audio/43e_inwardSway.wav",
    "straight jab" :"martial_audio/43e_jab.wav",
    "jab, karate chop":"martial_audio/43e_jabKarateChop.wav",
    # :"martial_audio/43e_jabPalmStrike.wav",
    "jab to knee":"martial_audio/43e_jabToKnee.wav",
    "karate chop":"martial_audio/43e_entheusiasticKarateChop.wav",
    "low block":"martial_audio/43e_lowBlock_0.wav",
    # :"martial_audio/43e_lowBlockFullRedirection.wav",
    # :"martial_audio/43e_lowBlockOutwwardParry.wav",
    "lunge for the legs":"martial_audio/43e_lungeForTheLegs.wav",
    # :"martial_audio/43e_outwardFullRedirection.wav",
    "outward parry":"martial_audio/43e_outwardParry.wav",
    "outward parry palm strike":"martial_audio/43e_outwardParryPalmStrike.wav",
    "out-sway":"martial_audio/43e_outwardSway.wav",
    "quick palm strike":"martial_audio/43e_palmStrike2.wav",
    "quarter turn roll":"martial_audio/43e_quarterTurnRoll.wav",
    "quarter turn step":"martial_audio/43e_quarterTurnStep.wav",
    "roll and uppercut":"martial_audio/43e_rollingUppercut.wav",
    "roll and hook":"martial_audio/43e_rollinHook.wav",
    "shuffle back":"martial_audio/43e_shuffleBack.wav",
    "shuffle forward":"martial_audio/43e_shuffleForward.wav",
    "shuffle-forward jab":"martial_audio/43e_shuffleForwardJab.wav",
    "side chop":"martial_audio/43e_sideChop.wav",    
    "sidestep roll":"martial_audio/43e_sidestepRoll.wav",
    "step forward":"martial_audio/43e_stepForward_utility.wav",
    "single-leg shove takedown":"martial_audio/43e_singleLegShoveTakedown.wav",
    "straight knee":"martial_audio/43e_straightKnee.wav",
    "outward parry, clothesline":"martial_audio/43e_outwardParryClothesline.wav",
    "throat punch":"martial_audio/43e_throatPunch.wav",
    "white crane, shove":"martial_audio/43e_whiteCraneShove.wav",
    "low shove":"martial_audio/43e_lowShove.wav",
    "feinting jab":"martial_audio/43e_feintingJab.wav",
    "rising double axe handle":"martial_audio/43e_RisingDoubleAxeHandle.wav",
    "superman punch":"martial_audio/43e_SupermanPunch.wav",
    "white crane, bell clap":"martial_audio/43e_WhiteCraneBellClap.wav",
    # :"martial_audio/.wav",
}
voice_43e_feint_auds = [
    "martial_audio/43e_feint2.wav",
    "martial_audio/43e_feint.wav"
]
voice_43e_left_auds = [
    "martial_audio/43e_left.wav",
    "martial_audio/43e_leftFootForward.wav",
    "martial_audio/43e_leftFootForward2.wav",
    "martial_audio/43e_leftSide.wav"
]
voice_43e_right_auds = [
    "martial_audio/43e_right.wav",
    "martial_audio/43e_rightfootforward.wav",
    "martial_audio/43e_rightFootForward2.wav",
    "martial_audio/43e_rightSide.wav"
]

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
        ["abs", "cardio", "light", "martial", "res_band"]),
    WorkoutMove("squat to overhead press",
        ["squat to overhead press"],
        ["hamstrings", "delts", "med", "cardio", "compound", "big_weight", "small_weight"]),
    WorkoutMove("marching doll high knee",
        ["marching doll high knee"],
        ["hip flexors", "delts", "light", "cardio", "compound"]),
    WorkoutMove("alt. arm fly side-step",
        ["alt. arm fly side-step"],
        ["pecs", "delts", "light", "cardio", "compound"]),
    WorkoutMove("lat pull-down push-out",
        ["lat pull-down push-out"],
        ["traps", "delts", "compound", "cardio", "small_weight"]),
    WorkoutMove("3-point frog squats",
        ["3-point frog squats"],
        ["quads", "delts", "med", "cardio", "compound", "dumbbell", "small_weight"]),
    WorkoutMove("kneel lat pull-down push-out", # need aud
        ["Kn.Lat pull-down push-out"],# need aud
        ["traps", "delts", "compound", "cardio", "small_weight", "ground"]),
    WorkoutMove("single forearm raise",
        ["L.forearm raise", "R.forearm raise"],
        ["forearms", "mirrored", "small_weight", "big_weight", "dumbbell"]),
    WorkoutMove("alternating forearm raise",
        ["Alt.forearm raise"],
        ["forearms", "small_weight", "big_weight", "dumbbell", "med"]),
    WorkoutMove("single inner bicep curl",# need aud
        ["L.inner bicep curl", "R.inner bicep curl"],
        ["biceps", "mirrored", "small_weight", "big_weight", "dumbbell", "med"]),
    WorkoutMove("alternating bicep curl",
        ["Alt.Bicep curl"],
        ["bicebs", "small_weight", "big_weight", "dumbbell"]),
    WorkoutMove("4-count cheer squad",
        ["4-count cheer squad"], # remember to pull down with the back like lat pull down to activate traps
        ["traps", "light", "small_weight", "delts"]),
    WorkoutMove("Alt.Side-step sky-punch",
        ["Alt.Side-step sky-punch"],
        ["delts", "light", "small_weight", "cardio", "dumbbell"]),
    WorkoutMove("slow lat pull-down",
        ["slow lat pull-down"],
        ["traps", "light"]),
    WorkoutMove("flying cobra",
        ["flying cobra"],
        ["traps", "ground"]),
    WorkoutMove("lying lat pull-downs",
        ["lying lat pull-downs"],
        ["traps", "ground"]),
    WorkoutMove("supermans",
        ["supermans"],
        ["traps", "ground"]),
    WorkoutMove("shoulder swimmers",
        ["shoulder swimmers"],
        ["traps"]),
    WorkoutMove("3-count cherry pickers",
        ["3-count cherry pickers"],
        ["traps", "meme", "light"]),
    WorkoutMove("lying back-splash reach-outs",
        ["lying back-splash reach-outs"],
        ["traps", "light", "ground"]),
    WorkoutMove("superman swimmers",
        ["superman swimmers"],
        ["traps"]),
    WorkoutMove("lying alt. backstroke",
        ["lying alt. backstroke"],
        ["traps"]),
    WorkoutMove("Fly-press side-step",
        ["Fly-press side-step"],
        ["traps", "small_weight", "light"]),
    WorkoutMove("sing.Hip abductions",
        ["sing.Hip abductions"],
        ["hip flexors"]),
    WorkoutMove("alt. hammer-downs",
        ["alt. hammer-downs"],
        ["triceps", "small_weight", "light"]),
    WorkoutMove("tricep dips",
        ["tricep dips"],
        ["triceps", "ground", "bench"]),
    WorkoutMove("sing.Leg tricep dips",
        ["L.Leg tricep dips", "R.Leg tricep dips"],
        ["triceps", "ground", "bench", "heavy"]),
    WorkoutMove("Tricep get-ups",
        ["Tricep get-ups", "heavy"],
        ["triceps", "ground"]),
    WorkoutMove("sing.Tri kick-backs",
        ["L.Tri kick-backs", "R.Tri kick-backs", "med", "heavy"],
        ["triceps", "res_band", "small_weight"]),
    WorkoutMove("sphynx push-up",
        ["sphynx push-up"],
        ["triceps", "ground", "adv", "heavy"]),
    WorkoutMove("Sing.3/4 Stance Hatchet",
        ["R.3/4 Stance Hatchet", "L.3/4 Stance Hatchet"],
        ["triceps", "small_weight", "light"]),
    WorkoutMove("Alt.3/4 Stance Hatchet",
        ["Alt.3/4 Stance Hatchet"],
        ["triceps", "small_weight", "light"]),
    WorkoutMove("Double Down Swords",
        ["Double Down Swords"],
        ["triceps", "small_weight", "light"]),
    WorkoutMove("Sing.Overhead Tri.Ext.",
        ["Sing.Overhead Tri.Ext."],
        ["triceps", "adv", "dumbbell", "small_weights"]),
    WorkoutMove("Overhead goblet Tri.Ext.",
        ["Overhead goblet Tri.Ext."],
        ["triceps", "compound", "dumbbell", "big_weight"]),
    WorkoutMove("Goblet squat Tri.Ext.",
        ["Goblet squat Tri.Ext."],
        ["triceps", "dumbbell", "heavy", "big_weight"]),
    WorkoutMove("Diamond push-up",
        ["Diamond push-up"],
        ["triceps", "ground", "heavy"]),
    WorkoutMove("Elbows-back Tri.Push-up",
        ["Elbows-back Tri.Push-up"],
        ["triceps", "ground", "heavy"]),
    
    # WorkoutMove("",
    #     [""],
    #     ["traps"]),
]
muscle_groups = [ "abs", "biceps", "forearms", "glutes", "hamstrings", 
    "obliques",  "pecs", "traps",  "triceps"]
traits = ["adv", "big_weight", "cardio", "dumbbell", "ground", "heavy", "light", "martial", 
    "med", "mirrored", "res_band", "small_weight"]

# franken forearm, delts
# preying mantis
#  cats claw wrists, cat
# thriller wrises, dance
#  a pose inner
#  a pose outer

# also need aud call: auds exist
# R.Elbow, L.Knee
# L.Elbow, R.Knee
#  figure eight obliques
# prisoner position high knees #dance

# SALVAGE THE WARMUPS FROM STRETCHES DOC FIRST BECAUSE AUDIO EXISTS

all_workout_object_keys = [
"Side-slugger torso twist", 
"single rock-and-box", 
"alternating rock-and-box",
"squat to overhead press",
"marching doll high knee",
"alt. arm fly side-step",
"lat pull-down push-out",
"3-point frog squats",
"kneel lat pull-down push-out",
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
    # print(out_arr)

def get_moves_matching_at_least_one_keyword(keyword_list):
    # iterate through all exercise objects. only return the ones that match at least one item in the target array
    out_arr = [move.display_name_list for move in all_exercise_objects if any(exclusion_term in keyword_list for exclusion_term in move.info_list)]
    # return [car for car in cars if not any(color in exclude_colors for color in car.color)]
    # print(out_arr)
    
# NYI NOTE: NYI filtering options in the above functions DO work! Not applied though
# get_moves_matching_at_least_one_keyword(["traps"])
# print(f"*"*24)
# exclude_keywords_from_workout_list(["delts", "biceps"])

# audio: Lunge down into triangle pose standups!
# "kn.Lat pull-down push-out" audio_hit_half/pdaBeepBeep.wav
# "L.forearm raise", "R.forearm raise" audio_hit_half/pdaBeepBeep.wav
# "L.inner bicep curl", "R.inner bicep curl" audio_hit_half/pdaBeepBeep.wav

# main properties for info:
#   - main muscle group is in position 0. Other muscle groups follow
#   - if NEEDS equipment, tag keyword "equip" DO NOT use if there is an empty-hand variant; this is a limiting filter
#   -- if compatible with heavy lifting, "big_weight", and light only, "small_weight"
#   - if needs ground for sit of lying, tag keyword "ground"
#   - if not compatible with a VR workout, tag "no vr"
#   - cardio, stretch, compound, res_band, dumbbell
#   - light, med, heavy, explosive, high impact







































class ExerciseTimerApp:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Exercise Timer")

        # Set the width and height of the window
        self.master.geometry("1105x850")
        # Assign fixed width to column 1
        # self.master.grid_columnconfigure(1, minsize=235)

        # Create a Notebook widget to manage tabs
        self.tab_manager = ttk.Notebook(master)
        self.tab_manager.pack(fill="both", expand=True)
        
        self.tab1 = ttk.Frame(self.tab_manager)
        self.tab_manager.add(self.tab1, text="Filters")

        self.tab2 = ttk.Frame(self.tab_manager)
        self.tab_manager.add(self.tab2, text="Stretches")

        self.tab3 = ttk.Frame(self.tab_manager)
        self.tab_manager.add(self.tab3, text="Boxing")

        self.tab4 = ttk.Frame(self.tab_manager)
        self.tab_manager.add(self.tab4, text="Hard x Soft")

        #  initialize pygame so I can play music properly
        pygame.init()
        # Load Stretches from stretches_doc.py --------------------------------------------------------------------------------------------------
        # self.stretches_arr = stretches_doc
        # ---------------------------------------------------------------------------------------------------------
        #  Init all temp arrs for all audio categories / this is also a list of which arrs exist
        self.temp_start_bumper_aud_arr = []
        self.temp_active_song_aud_arr = []
        self.temp_end_bumper_aud_arr = []   
        self.temp_interval_song_aud_arr = []
        # self.temp_half_bumper_aud_arr = []
        # self.end_of_workout_arr = []
        # self.temp_special_ender_aud_arr = []
        self.default_encouragement = "audio_hit_start/letsGetMovingBubblegum1.wav"
        #  -----------------------------------------------------------------------------
        # NOTE: motion halfway SFX, motion end SFX, and workout end MSG are currently static sounds
        self.halfway_alarm = "audio_hit_half/pdaBeepBeep.wav"
        self.end_alarm = "audio_hit_end/blake_gunfire_shot.wav"
        self.workout_end_aud = "audio_special_ender/TP_Fanfare_SmallItem_tada.wav"
        # ---------------------------------------------------------------------------------------------------------
        # audio_hit_start/
        self.start_bumper_aud_arr = audio_doc.outsourced_start_bumper_aud_arr 
        
        # audio_active_songs for push sets
        self.active_song_aud_arr = audio_doc.outsourced_active_song_aud_arr
        
        # audio_interval_songs, for downtempo sets/rest
        self.interval_song_aud_arr = audio_doc.outsourced_interval_song_aud_arr 
        
        # audio_hit_end, for end of motion
        self.end_bumper_aud_arr = audio_doc.outsourced_end_bumper_aud_arr 

        # audio_special_ender for when the workout is done
        # self.special_ender_aud_arr = []


# This is the default array with mixed voices, 
        #  a similar structure could be done for specific voices only
        self.master_exercise_name_audio_dic = {
# [!] Abs  ------------------------------------------------------------------------------------------------------
        "belly dancer kicks":["exercise_names/mori_bellydancerKicks.wav"], 
        "cross-core knee strike":["exercise_names/mori_crossCoreKneeStrike.wav"],
        "draw sword, side-bend":["exercise_names/mori_drawSwordSideBend.wav"],
    # + Center abs target -------------------------
        "hip raise, leg extension": ["exercise_names/23B_hipRaiseLegExtension.wav"],
        "boat row" : ["exercise_names/23B_boatRow.wav"],
        "leg lifts, candle pose": ["exercise_names/23B_legLiftsCandlePose.wav", "exercise_names/legLiftCandleBubblegum.wav"],
        # [add l8r]: Turtle crunch

    # + Lower Abs  ----------------------------------------
        # compound for hip flexor, quad, lower ab
        "wall-crawlers":["exercise_names/mori_wallCrawlers.wav"],
        "open-hip, str. high-knee":["stretch_auds/mori_handsUpHighKnees.wav", "stretch_auds/mori_highKnees.wav"],
        "flutter kicks": ["exercise_names/flutterkickBubblegum.wav"], 
        "L.out Knee Strike": ["exercise_names/mori_leftOutstepKneeStrike.wav"],
        "R.out Knee Strike": ["exercise_names/mori_rightOutstepKneeStrike.wav"],
        # compound for hip flexor, quad, lower ab, shoulder
        "full extension cross-crunch":["exercise_names/23B_fullExtensionCrossCrunch.wav", "exercise_names/fullextensioncrossCrunchBubblegum.wav"],
        # compound for obliques
        "half windshield wiper combo": ["exercise_names/23b_halfwayWindshieldWiperCombo.wav"],
        # [add l8r; NYI] single leg windshield wiper
        # [add l8r; NYI] seated leg lever
    # + Obliques  ---------------------------------------------------------------------------
        "Figure-8 oblique Ax.":["exercise_names/kaf_figure8Obliques.wav", "exercise_names/kaf_alternatingAxeHandleObliques.wav"],
        "side-slugger torso twist":["stretch_auds/mori_torsoTwistSidePunch.wav", "stretch_auds/mori_torsoTwistPunches.wav", "stretch_auds/mori_sideChamberSlugs.wav"], # compound 
        "lighthouse torso twists":["stretch_auds/mori_lighthouseTorsoTwists.wav"],
        # "sideways hip raise": ["exercise_names/23B_sidewaysHipRaise.wav"],
        "oblique heel-taps":["exercise_names/23b_obliqueHeelTaps.wav", "exercise_names/obliqueHeelTaps.wav"],
        "windshield wiper leg lifts": ["exercise_names/23b_windshieldWiperLegLifts.wav"], # ADVANCED
        "hatchet cross tension": ["exercise_names/23b_hatchetMotionxCross.wav"],
        "seated russian twists": ["exercise_names/23B_seatedRussianTwists.wav"],
        "torso twist hip taps":["exercise_names/mori_torsoTwistHipTaps.wav"], # can also be done weighted
    # + Quads  -----------------------------------------------------------------------------------
        "alt. torso-twist lunges":["stretch_auds/mori_twistedCactusLunge.wav", "stretch_auds/mori_torsoTwistLunges.wav"], #also weighted 
        "step-back lunges":["exercise_names/mori_stepBackLunges.wav"], 
    # + Shoulders --------------------------------------------------------------------------------
        "L. rock-and-box": ["exercise_names/mori_leftRockAndBox.wav"],
        "R. rock-and-box": ["exercise_names/mori_RightrockAndBox.wav"],
    # + Upper abs -------------------------------------------------------------------------------------
    # "open-hip T-bolt pr.ess":["stretch_auds/.wav"],
    # basic crunch
    # + Unknown / research needed ------------------------------------------------------------------
        "half-bridge hip-thrusts" : ["exercise_names/halfbridgeHipThrustsBubblegum.wav"], 
        "heels to the heavens": ["exercise_names/23b_heelsToHeavens.wav", "exercise_names/heels2HeavensBubblegum.wav"], 
        "slow stand. Bicycles":["exercise_names/kaf_standing_bicycle.wav", "exercise_names/mori_slowTensionStandingBicycles.wav"], 
        "stellar windmills":["exercise_names/mori_stellarWindmills.wav"],
        "straight-leg toe taps":["exercise_names/mori_straightLegToeTaps.wav"],
        "windmill toe touches":["exercise_names/kaf_standing_windmills.wav", "exercise_names/mori_windmillToeTouches.wav"],
        "windmill sky chops":["exercise_names/mori_windmillSkyChops.wav"],
        "wood chopper oblique":["stretch_auds/mori_woodChopper.wav", "stretch_auds/mori_treeChopper.wav"],
# [!] Biceps ------------------------------------------------------------------------------------------------------
    # + Pecs
        "barrel hug hammer curl":["stretch_auds/mori_barrelHugHammerCurl.wav"], #  Unique compound for barrel hug...
        "biceb curl fly press":["stretch_auds/mori_bicepCurlFlyPress2.wav", "stretch_auds/mori_bicepCurlFlyPress.wav"],
    # + Delts, upper chest, traps (with military press)
        "curl, overhead press":["stretch_auds/mori_curlToOverHeadPress.wav"],
    # + Delts
        "curl & double punch out":["stretch_auds/mori_curlUpDoublePunchOut.wav"],
    # + Forearm 
        "T-rex bicep curl":["stretch_auds/mori_trexBicebCurl.wav"], # weighted variation
        "A-pose ro. claw-curls":["stretch_auds/mori_latPoseRotatingClaws.wav"],
        "shrieking ghoul":["stretch_auds/mori_shriekingGhoul1.wav", "stretch_auds/mori_shriekingGhoul2.wav"], # and Delts
    # + Tricep & forearm
        "alternating hammer-downs":["stretch_auds/mori_whackamoleHammers.wav","stretch_auds/mori_alternatingHammerDown.wav", "stretch_auds/mori_altWhackAMole.wav"],
# Delts -----------------------------------------------------------
        "Franken Forearm Raise":["exercise_names/me_frankensteinForearmRaise.wav"],
# [!] Forearms ------------------------------------------------------------------------------------------------------
        "claw-hand Z-curls":["stretch_auds/mori_clawHandZCurls.wav", "stretch_auds/mori_clawHandZCurls2.wav"],
        "zombie claw f.Arm Raise":["stretch_auds/mori_zombie_clawForearmRaise.wav", "exercise_names/me_preyingMantisForearmRaise.wav"], 
# [!] Hamstrings ---------------------------------------------------------------------------------------------------
    # + Delts, traps
        "squat to overhead press":["exercise_names/mori_squatToOverheadPress1.wav"],
# [!] Hip Flexors ----------------------------------------------------------------------------------------
        "R.Side hip abduction":["exercise_names/kaf_obliqueLegLift.wav"],
        "L.Side hip abduction":["exercise_names/kaf_obliqueLegLift.wav"],
    # + delts    
        "marching doll high knee":["stretch_auds/mori_marchingDollHighKnee.wav"],
# [!] Pectorals ----------------------------------------------------------------------------------------------------
        "alt. arm fly side-step":["stretch_auds/mori_singleArmFlySidestep.wav"],
    # Division for upper, side, and lower pecs needed
    # + delts
        "sky-punch fly press":["stretch_auds/mori_skyPunchFlyPress.wav"],
        "vampire wings":["stretch_auds/mori_vampireWings.wav"],
        "X-Y fly press":["stretch_auds/mori_xyFlyPress.wav", "stretch_auds/mori_cactusHugger.wav"],
    # compound, multiple
        "florentine 1-2":["stretch_auds/mori_florentine12.wav", "stretch_auds/mori_florentineone-two.wav"],

# [!] Quads -----------------------------------------------------------------------------------------------------     
        "squat pulse stand-ups":["exercise_names/mori_squatPulseStandUps.wav", "exercise_names/mori_squatPulseStandUp2.wav"],
        "3-point frog squats":["stretch_auds/mori_3ptFrogSquats.wav"],

# [!] Shoulders------------------------------------------------------------------------------------------------------
        #  !!! - Division for delts and traps needed -
        "slow lat pull-down":["exercise_names/kaf_tensionLatPullDown.wav", "exercise_names/tensionLatPullDownBubblegum.wav","exercise_names/elf_tension_lat_pull_downs.wav","stretch_auds/mori_overheadLat3.wav", "stretch_auds/mori_overheadLatPulldown2.wav"],
        "Alt.Side-step sky-punch":["stretch_auds/mori_singleArmSidesteppingSkyPunches.wav"],
        "back-stroke torso twist":["stretch_auds/mori_armCircleTorsoRotations.wav", "stretch_auds/mori_backstrokeTorsoTwists.wav"],
        "sky-punch, side stab":["stretch_auds/mori_skyPunchSideStab.wav"],
        "4-count cheer squad":["stretch_auds/mori_4countCheerSquad.wav"],
        "bear crawl": ["exercise_names/bearCrawlBubble.wav"], 
        "flying cobra": ["exercise_names/kaf_flyingCobra.wav", "exercise_names/elf_flying_cobra.wav", "exercise_names/flyingCobraBubble.wav"],
        "lat pull-down push-out" : ["exercise_names/elf_kneeling_lat_pull_down_push_outs.wav"],
        "lying lat pull-downs": ["exercise_names/kaf_lyingLatPullDowns.wav", "exercise_names/lyingLatPullDownBubblegum.wav"],
        "pike position cross toe-touches":["exercise_names/elf_pike_position_cross_toe_touches.wav", "exercise_names/pikePositionCrossToeBubblegum.wav"], 
        "pike push-up":["exercise_names/elf_pike_push_up.wav", "exercise_names/pikePushUpBubblegum.wav"],
        "plank shoulder taps":["exercise_names/kaf_plankShoulderTaps.wav", "exercise_names/elf_plank_shoulder_taps.wav", "exercise_names/plankShoulderTapsbub.wav"], 
        # "reaching row" : ["exercise_names/kaf_reachingRow.wav", "exercise_names/reachingRowBubble.wav"], 
        "slow and low crawl": ["exercise_names/elf_slow_and_low_crawl.wav"],
        "snow angel shoulders":["exercise_names/kaf_snowAngelShoulders.wav", "exercise_names/snowAngelShoulders1.wav"],
        "supermans": ["exercise_names/kaf_supermans.wav", "exercise_names/elf_supermans.wav"],
# [!] Triceps    ------------------------------------------------------------------------------------------------------
    # + bicep 
        # "left overhead tricep extension":["exercise_names/mori_leftOverheadTriExtension.wav"]
        # "right overhead tricep extension":["exercise_names/mori_RtOverheadTriExtension.wav", "exercise_names/mori_RtOverheadTriExtension.wav"] 
        # "chop out, scrape in":["stretch_auds/.wav"], # compound, push and pull

    #  + Delts
        "double-fang down-stab":["stretch_auds/mori_doubleFangDown3.wav", "stretch_auds/mori_doubleFangDownwardStab.wav"],
        # draw double swords from back # (the elephant tusk backpack)
        # from 3/4 boxer's stance, Ushiro-iaijutsu (L/R mirror), one arm at a time, full range of motion for tricep dip back, full slash forward
# + Forearms
        # "basic hammer curl":["stretch_auds/mori_alt_basicHammerCurls.wav"],   
        #  Hammer curl to wrist rotation # compoun
        #  Double chop pulse : Arms at sides, hammer curl, karate chop hands full wrist extension, then at bottom position with arms at waist, wrists go down and up
    # + Multiple compound, chest and shoulders
        # "high-hammer curls": ["stretch_auds/mori_highHammerCurl.wav"],
        # "Alt. high-hammer curls": ["stretch_auds/mori_altHighHammerCurls.wav"],
   
# [!] Stretches ------------------------------------------------------------------------------------------------------
        "R.Stand ankle rotations":["stretch_auds/me_RtLegStAnkleRotation.wav", "stretch_auds/me_rtSideStandAnkleRotations.wav"],
        "L.Stand ankle rotations":["stretch_auds/me_leftLegStAnkleRotations.wav"],
        "L.Stand heel-to-toe point":["stretch_auds/me_leftLegStandingHeelToToePoint.wav"],
        "R.Stand heel-to-toe point":["stretch_auds/me_RtLegStHeelToToePoint.wav"],
        "L.Arm Across high-knees":["stretch_auds/me_leftArmAcrossKneeRaises.wav", "stretch_auds/me_leftARmAcrossHighKneeRaze.wav", "stretch_auds/me_leftArmAcrossHighKnees.wav"], 
        "R.Arm Across high-knees":["stretch_auds/me_RtArmAcrossHighKnee1.wav", "stretch_auds/me_rightArmAcrossHighKnee2.wav"],
        "L.Arm Across side step":["stretch_auds/me_leftArmAcrossSideStep.wav"], 
        "R.Arm Across side step":["stretch_auds/me_RightArmAcrossSideStep.wav", "stretch_auds/me_rtArmAcrossSideStep.wav"],
        "L.Arm Across, Calf Raise":["stretch_auds/me_LArmAcrossAnkleRaises.wav"], 
        "R.Arm Across, Calf Raise":["stretch_auds/me_right_armAcrossCalfRaises.wav"],
        "L. Tri. & ankle raises":["stretch_auds/me_leftTricepStretchCalfRaises2.wav"], 
        "R. Tri. & ankle raises":["stretch_auds/me_righttricepStretchCalf2.wav"],
        "L. Tri. & high-knees":["stretch_auds/me_leftTricepKneeRaises.wav"], 
        "R. Tri. & high-knees":["stretch_auds/me_rightTricepHighKneeRaise.wav", "stretch_auds/me_rightTriKneeRaises.wav"],
        "L. Tri, side-step":["stretch_auds/me_leftTriSidestep.wav"],
        "R. Tri, side-step":["stretch_auds/me_rtTriSideStep.wav"],
        "Arms up, wrist-ro.":["stretch_auds/me_armsUpWristRotations.wav"], 
        "Arms out, wrist-ro.":["stretch_auds/me_armsOutWristRotations.wav"],
        "X-Y-T Wrist rotations":["stretch_auds/me_xytWristRotations.wav"], 
        "Y-A-X-T-X, wrist ro.":["stretch_auds/me_yaxtx_spelled.wav", "stretch_auds/me_yaxtx_wrist2.wav"], 
        "A-pose In. Wrist Cir.":["stretch_auds/me_aPoseInwardWrCircles.wav"],
        "A-pose Out Wrist Cir.":["stretch_auds/me_a_poseOutWristCircles.wav", "stretch_auds/me_a_poseOutWristCir2.wav"],
        # "Down In/Out Wrist Cir.":["stretch_auds/.wav"],
        "Cat's claw wrist bends":["stretch_auds/me_catsClawWristBends.wav"], 
        "Thriller wrist cir.":["stretch_auds/me_thrillerWristCircles.wav"],
        # "Frog Squat Stretch":["exercise_names/.wav"],
        "L.Lunge torso turn":["stretch_auds/me_leftLungeTrianglePose.wav"],
        "R.Lunge torso turn":["stretch_auds/me_rightLungeTrianglePose.wav"],
        "clock hula hips":["stretch_auds/me_standingHulaHipRotations_clockwise.wav"],
        "counter hula hips" :["stretch_auds/me_standingHulaHipRotations_counterclockwise.wav"],
        "L.Leg cross model pose":["stretch_auds/me_leftlegAcrossmodelpose.wav"],
        "R.Leg cross model pose":["stretch_auds/me_rightLegAcrossModelPose.wav"],
        "L-stand fw-lean calf":["stretch_auds/mori_standLeftLeanCalfStretch.wav", "stretch_auds/mori_leftLegStandLeanForwardCalf2.wav", "stretch_auds/me_leftstandingforwardleaningcalfStretch.wav"],
        "R-stand fw-lean calf":["stretch_auds/mori_StandRightCalfStretch2.wav", "stretch_auds/mori_right_leg_calfStretch1.wav"],
        "Pike, L-calf stretch":["stretch_auds/me_pikePositionleftCrossCalfStretch.wav"],
        "Pike, R-calf stretch":["stretch_auds/me_pikePositionRightCrossCalfStretch.wav"],
        "Stand L. knee-tuck":["stretch_auds/mori_standingLeftKneeTuckHold.wav"],
        "Stand R. knee-tuck":["stretch_auds/mori_standingRightkneeTuckHold.wav"],
        "L.back, lunging stretch":["stretch_auds/mori_leftlegBackLungingStretch.wav"],
        "R.back, lunging stretch":["stretch_auds/mori_rightLegBackLungingStretch.wav"],
        "Lying L-knee-tuck":["stretch_auds/mori_lyingleftKneeTuckStretch.wav"],
        "Lying R-knee-tuck":["stretch_auds/mori_lyingRightKneeTuckStretch.wav"],
        "Stand-V Left-leg":["stretch_auds/mori_standingVLeftLeg.wav"],
        "Stand-V Right-leg":["stretch_auds/mori_standingVRightLeg.wav"],
        "Stand-V center":["stretch_auds/mori_standingVCenterStretch.wav"],
        # "V-sit Left":["stretch_auds/me_standingVLeftLeg.wav"],
        # "V-sit Right":["stretch_auds/me_standingVRightLeg.wav"],
        # "V-sit Center":["stretch_auds/me_standingVCenterStretch.wav"],
        "Look-up neck ro.":["stretch_auds/mori_upperHalfCircleNeckRotation.wav"],
        "Look-down neck ro.":["stretch_auds/mori_downwardhalfCircleNeckRotation.wav"],
        "L.Stand quad pull":["stretch_auds/me_standingleftquadStretch.wav"],
        "R.Stand quad pull":["stretch_auds/me_standingRightQuadStretch.wav"],
        "L.Lying quad stretch":["stretch_auds/me_lyingLeftQuedStretch.wav"],
        "R.Lying quad stretch":["stretch_auds/me_lyingRightQuadStretch.wav"],
        "Stand.Center toe-touch":["stretch_auds/me_Standing_center_toe_touch_reach.wav"],
        "L.Over toe-touch":["stretch_auds/me_leftLegoverrighttoetouch.wav"],
        "R.Over toe-touch":["stretch_auds/me_rightlegOverLeftToeTouch.wav"],
        "Sit.Toe-touch":["stretch_auds/me_sittingtoetouchreach.wav","stretch_auds/me_sittingToeTouchReach2.wav"],
        "L.Leg out, toe-touch":["stretch_auds/me_leftLegOutToeTouchReach.wav"],
        "R.Leg out, toe-touch":["stretch_auds/me_rightlegOutToeTouchReach.wav"],
        "Sit L.Extension hold":["stretch_auds/me_sittingLeftLegExtensionHold.wav"],
        "Sit R.Extension hold":["stretch_auds/me_sittingRightLegExtensionHold.wav"],   
        "Center split":["stretch_auds/me_centerSplit.wav"],
        "Left side-lunge":["stretch_auds/me_leftSideLunge.wav"],
        "Right side-lunge":["stretch_auds/me_rightSideLunge.wav"],
        "Left front-split":["stretch_auds/me_leftFrontSplit.wav"],
        "Right front-split":["stretch_auds/me_rightFrontSplit.wav"],

     }

#  -------------------------------------------------- DISPLAY -------------------------------------------------------

#  --------------------------------------------------------------
        self.muscle_vars = {muscle: tk.BooleanVar() for muscle in muscle_groups}
        self.muscle_vars_to_exclude = {muscle: tk.BooleanVar() for muscle in muscle_groups}
        self.trait_vars = {trait: tk.BooleanVar() for trait in traits}
        self.trait_vars_to_exclude = {trait: tk.BooleanVar() for trait in traits}

        self.muscle_include_label = tk.Label(self.tab1, text="Include")
        self.muscle_include_label.config(font=("times", 12), fg="#F9C22E", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.muscle_include_label.grid(row=0, column=0, padx=2, pady=5)
        self.muscle_exclude_label = tk.Label(self.tab1, text="Exlude")
        self.muscle_exclude_label.config(font=("times", 12), fg="#F9C22E", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.muscle_exclude_label.grid(row=0, column=1, padx=2, pady=5)
        self.trait_include_label = tk.Label(self.tab1, text="Include")
        self.trait_include_label.config(font=("times", 12), fg="#ff3", bg="#224", bd=2, relief="solid", padx=5, pady=5) 
        self.trait_include_label.grid(row=0, column=2, padx=2, pady=5)
        self.trait_exclude_label = tk.Label(self.tab1, text="Exlude")
        self.trait_exclude_label.config(font=("times", 12), fg="#ff3", bg="#224", bd=2, relief="solid", padx=5, pady=5) 
        self.trait_exclude_label.grid(row=0, column=3, padx=2, pady=5)



        # # Create checkboxes for inclusion and exclusion
        # for i, muscle in enumerate(muscle_groups):
        #     tk.Checkbutton(self.tab1, text=muscle, variable=self.muscle_vars[muscle]).grid(row=i+1, column=0, sticky='w')
        #     tk.Checkbutton(self.tab1, text=muscle, variable=self.muscle_vars_to_exclude[muscle]).grid(row=i+1, column=1, sticky='w')
        # for i, trait in enumerate(traits):
        #     tk.Checkbutton(self.tab1, text=trait, variable=self.trait_vars[trait]).grid(row=i+1, column=2, sticky='w')
        #     tk.Checkbutton(self.tab1, text=trait, variable=self.trait_vars_to_exclude[trait]).grid(row=i+1, column=3, sticky='w')

        # Checkbutton widgets for muscle inclusion and exclusion
        self.checkbutton_abs_include = tk.Checkbutton(self.tab1, text="abs", variable=self.muscle_vars["abs"])
        self.checkbutton_abs_include.grid(row=1, column=0, sticky='w')
        self.muscle_vars["abs"].set(True)

        self.checkbutton_abs_exclude = tk.Checkbutton(self.tab1, text="abs", variable=self.muscle_vars_to_exclude["abs"])
        self.checkbutton_abs_exclude.grid(row=1, column=1, sticky='w')

        self.checkbutton_biceps_include = tk.Checkbutton(self.tab1, text="biceps", variable=self.muscle_vars["biceps"])
        self.checkbutton_biceps_include.grid(row=2, column=0, sticky='w')
        self.checkbutton_biceps_exclude = tk.Checkbutton(self.tab1, text="biceps", variable=self.muscle_vars_to_exclude["biceps"])
        self.checkbutton_biceps_exclude.grid(row=2, column=1, sticky='w')

        self.checkbutton_forearms_include = tk.Checkbutton(self.tab1, text="forearms", variable=self.muscle_vars["forearms"])
        self.checkbutton_forearms_include.grid(row=3, column=0, sticky='w')
        self.checkbutton_forearms_exclude = tk.Checkbutton(self.tab1, text="forearms", variable=self.muscle_vars_to_exclude["forearms"])
        self.checkbutton_forearms_exclude.grid(row=3, column=1, sticky='w')

        self.checkbutton_glutes_include = tk.Checkbutton(self.tab1, text="glutes", variable=self.muscle_vars["glutes"])
        self.checkbutton_glutes_include.grid(row=4, column=0, sticky='w')
        self.checkbutton_glutes_exclude = tk.Checkbutton(self.tab1, text="glutes", variable=self.muscle_vars_to_exclude["glutes"])
        self.checkbutton_glutes_exclude.grid(row=4, column=1, sticky='w')

        self.checkbutton_hamstrings_include = tk.Checkbutton(self.tab1, text="hamstrings", variable=self.muscle_vars["hamstrings"])
        self.checkbutton_hamstrings_include.grid(row=5, column=0, sticky='w')
        self.checkbutton_hamstrings_exclude = tk.Checkbutton(self.tab1, text="hamstrings", variable=self.muscle_vars_to_exclude["hamstrings"])
        self.checkbutton_hamstrings_exclude.grid(row=5, column=1, sticky='w')

        self.checkbutton_obliques_include = tk.Checkbutton(self.tab1, text="obliques", variable=self.muscle_vars["obliques"])
        self.checkbutton_obliques_include.grid(row=6, column=0, sticky='w')
        self.checkbutton_obliques_exclude = tk.Checkbutton(self.tab1, text="obliques", variable=self.muscle_vars_to_exclude["obliques"])
        self.checkbutton_obliques_exclude.grid(row=6, column=1, sticky='w')

        self.checkbutton_pecs_include = tk.Checkbutton(self.tab1, text="pecs", variable=self.muscle_vars["pecs"])
        self.checkbutton_pecs_include.grid(row=7, column=0, sticky='w')
        self.checkbutton_pecs_exclude = tk.Checkbutton(self.tab1, text="pecs", variable=self.muscle_vars_to_exclude["pecs"])
        self.checkbutton_pecs_exclude.grid(row=7, column=1, sticky='w')

        self.checkbutton_traps_include = tk.Checkbutton(self.tab1, text="traps", variable=self.muscle_vars["traps"])
        self.checkbutton_traps_include.grid(row=8, column=0, sticky='w')
        self.checkbutton_traps_exclude = tk.Checkbutton(self.tab1, text="traps", variable=self.muscle_vars_to_exclude["traps"])
        self.checkbutton_traps_exclude.grid(row=8, column=1, sticky='w')

        self.checkbutton_triceps_include = tk.Checkbutton(self.tab1, text="triceps", variable=self.muscle_vars["triceps"])
        self.checkbutton_triceps_include.grid(row=9, column=0, sticky='w')
        self.checkbutton_triceps_exclude = tk.Checkbutton(self.tab1, text="triceps", variable=self.muscle_vars_to_exclude["triceps"])
        self.checkbutton_triceps_exclude.grid(row=9, column=1, sticky='w')

        # --------traits ----------------------------------------------------------------

        self.checkbutton_adv_include = tk.Checkbutton(self.tab1, text="adv", variable=self.trait_vars["adv"])
        self.checkbutton_adv_include.grid(row=1, column=2, sticky='w')
        self.checkbutton_adv_exclude = tk.Checkbutton(self.tab1, text="adv", variable=self.trait_vars_to_exclude["adv"])
        self.checkbutton_adv_exclude.grid(row=1, column=3, sticky='w')
        self.trait_vars_to_exclude["adv"].set(True)

        self.checkbutton_big_weight_include = tk.Checkbutton(self.tab1, text="big_weight", variable=self.trait_vars["big_weight"])
        self.checkbutton_big_weight_include.grid(row=2, column=2, sticky='w')
        self.checkbutton_big_weight_exclude = tk.Checkbutton(self.tab1, text="big_weight", variable=self.trait_vars_to_exclude["big_weight"])
        self.checkbutton_big_weight_exclude.grid(row=2, column=3, sticky='w')

        self.checkbutton_cardio_include = tk.Checkbutton(self.tab1, text="cardio", variable=self.trait_vars["cardio"])
        self.checkbutton_cardio_include.grid(row=3, column=2, sticky='w')
        self.checkbutton_cardio_exclude = tk.Checkbutton(self.tab1, text="cardio", variable=self.trait_vars_to_exclude["cardio"])
        self.checkbutton_cardio_exclude.grid(row=3, column=3, sticky='w')

        self.checkbutton_dumbbell_include = tk.Checkbutton(self.tab1, text="dumbbell", variable=self.trait_vars["dumbbell"])
        self.checkbutton_dumbbell_include.grid(row=4, column=2, sticky='w')
        self.checkbutton_dumbbell_exclude = tk.Checkbutton(self.tab1, text="dumbbell", variable=self.trait_vars_to_exclude["dumbbell"])
        self.checkbutton_dumbbell_exclude.grid(row=4, column=3, sticky='w')

        self.checkbutton_ground_include = tk.Checkbutton(self.tab1, text="ground", variable=self.trait_vars["ground"])
        self.checkbutton_ground_include.grid(row=5, column=2, sticky='w')
        self.checkbutton_ground_exclude = tk.Checkbutton(self.tab1, text="ground", variable=self.trait_vars_to_exclude["ground"])
        self.checkbutton_ground_exclude.grid(row=5, column=3, sticky='w')
        self.trait_vars_to_exclude["ground"].set(True)

        self.checkbutton_heavy_include = tk.Checkbutton(self.tab1, text="heavy", variable=self.trait_vars["heavy"])
        self.checkbutton_heavy_include.grid(row=6, column=2, sticky='w')
        self.checkbutton_heavy_exclude = tk.Checkbutton(self.tab1, text="heavy", variable=self.trait_vars_to_exclude["heavy"])
        self.checkbutton_heavy_exclude.grid(row=6, column=3, sticky='w')

        self.checkbutton_light_include = tk.Checkbutton(self.tab1, text="light", variable=self.trait_vars["light"])
        self.checkbutton_light_include.grid(row=7, column=2, sticky='w')
        self.checkbutton_light_exclude = tk.Checkbutton(self.tab1, text="light", variable=self.trait_vars_to_exclude["light"])
        self.checkbutton_light_exclude.grid(row=7, column=3, sticky='w')

        self.checkbutton_martial_include = tk.Checkbutton(self.tab1, text="martial", variable=self.trait_vars["martial"])
        self.checkbutton_martial_include.grid(row=8, column=2, sticky='w')
        self.checkbutton_martial_exclude = tk.Checkbutton(self.tab1, text="martial", variable=self.trait_vars_to_exclude["martial"])
        self.checkbutton_martial_exclude.grid(row=8, column=3, sticky='w')

        self.checkbutton_med_include = tk.Checkbutton(self.tab1, text="med", variable=self.trait_vars["med"])
        self.checkbutton_med_include.grid(row=9, column=2, sticky='w')
        self.checkbutton_med_exclude = tk.Checkbutton(self.tab1, text="med", variable=self.trait_vars_to_exclude["med"])
        self.checkbutton_med_exclude.grid(row=9, column=3, sticky='w')

        self.checkbutton_mirrored_include = tk.Checkbutton(self.tab1, text="mirrored", variable=self.trait_vars["mirrored"])
        self.checkbutton_mirrored_include.grid(row=10, column=2, sticky='w')
        self.checkbutton_mirrored_exclude = tk.Checkbutton(self.tab1, text="mirrored", variable=self.trait_vars_to_exclude["mirrored"])
        self.checkbutton_mirrored_exclude.grid(row=10, column=3, sticky='w')

        self.checkbutton_res_band_include = tk.Checkbutton(self.tab1, text="res_band", variable=self.trait_vars["res_band"])
        self.checkbutton_res_band_include.grid(row=11, column=2, sticky='w')
        self.checkbutton_res_band_exclude = tk.Checkbutton(self.tab1, text="res_band", variable=self.trait_vars_to_exclude["res_band"])
        self.checkbutton_res_band_exclude.grid(row=11, column=3, sticky='w')

        self.checkbutton_small_weight_include = tk.Checkbutton(self.tab1, text="small_weight", variable=self.trait_vars["small_weight"])
        self.checkbutton_small_weight_include.grid(row=12, column=2, sticky='w')
        self.checkbutton_small_weight_exclude = tk.Checkbutton(self.tab1, text="small_weight", variable=self.trait_vars_to_exclude["small_weight"])
        self.checkbutton_small_weight_exclude.grid(row=12, column=3, sticky='w')

        self.get_filtered_workout_button = tk.Button(self.tab1, text="Get Workout", command=lambda:self.get_filtered_workout_items())
        self.get_filtered_workout_button.grid(row=len(traits)+1, column=0, columnspan=4)


        # display area tab1
        self.filtered_timer_display = tk.Label(self.tab1, text="[countdown display]")
        self.filtered_timer_display.grid(row=0, column=5, padx=2, pady=5)
        self.filtered_timer_display.config(font=("times", 36), fg="lime", bg="black")

        self.combo_box002 = tk.Listbox(self.tab1, height=10, width=50)
        self.combo_box002.grid(row=1, rowspan=30, column=5, pady=5)
        self.combo_box002.config(font=("Times", 30), width="24", height="15", fg="#F9C22E", bg="#27233A")


# ----------  Set up Tab2 widgets -------------------------------------------------------------------------------------------

        self.stretch_name_label = tk.Label(self.tab2, text="Stretching!")
                                                                # lavander blush X dark-purple
        self.stretch_name_label.config(font=("times", 36), fg="#F9C22E", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.stretch_name_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.stretch_timer_label = tk.Label(self.tab2, text="(seconds per move)")
                                                            #  ice blue
        self.stretch_timer_label.config(font=("arial", 22), fg="#9BF3F0", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.stretch_timer_label.grid(row=1, column=0, padx=5, pady=5)

        self.stretch_time_length_label = tk.Label(self.tab2, text="(est. workout time)")
        self.stretch_time_length_label.grid(row=1, column=1, padx=5)
                                                                #  aquamarine X dark-purple
        self.stretch_time_length_label.config(font=("times", 22), fg="#52FFB8", bg="#27133A")

        self.stretch_pause_button = tk.Button(self.tab2, text="SND TST", command=lambda: self.get_and_play_rand_aud_to_end(self.end_bumper_aud_arr, self.temp_end_bumper_aud_arr))
        self.stretch_pause_button.grid(row=1, column=2, padx=5, pady=5)
        self.stretch_pause_button.config(font=("Times", 14), fg="#BEA7E5", bg="black")

        self.stretch_duration_slider = tk.IntVar()
        self.stretch_duration_slider = tk.Scale(self.tab2, from_=6, to=90, orient=tk.HORIZONTAL, resolution=6, variable=self.stretch_duration_slider, command=self.update_stretch_timing_preview_label)
        self.stretch_duration_slider.set(30)
        self.stretch_duration_slider.grid(row=3, column=0, padx=2)

        self.stretch_start_button = tk.Button(self.tab2, text="Randomize Session", command=self.initialize_stretches_update_display)
        self.stretch_start_button.grid(row=4, column=0, padx=5, pady=5)
        self.stretch_start_button.config(font=("impact", 14), fg="#52FFB8", bg="black")

        # self.stretch_pause_button = tk.Button(self.tab2, text="Start", command=self.start_continuous_session)
        # self.stretch_pause_button.grid(row=7, column=1, padx=5, pady=5)
        # self.stretch_pause_button.config(font=("Times", 14), fg="#9BF3F0", bg="black")

        self.stretch_pause_button = tk.Button(self.tab2, text="Start", command=self.start_continuous_session)
        self.stretch_pause_button.grid(row=4, column=1, padx=5, pady=5)
        self.stretch_pause_button.config(font=("Times", 14), fg="#9BF3F0", bg="black")

        # self.stretch_pause_button = tk.Button(self.tab2, text="test1", command=self.get_karate_exercises(8))
        # self.stretch_pause_button.grid(row=7, column=2, padx=5, pady=5)
        # self.stretch_pause_button.config(font=("Times", 14), fg="#BEA7E5", bg="black")
    
        self.stretch_pause_button = tk.Button(self.tab2, text="Pause/Resume", command=self.toggle_warmup_timer)
        self.stretch_pause_button.grid(row=4, column=2, padx=5, pady=5)
        self.stretch_pause_button.config(font=("Times", 14), fg="#9BF3F0", bg="black")
        
        self.first_col_stretches = tk.Listbox(self.tab2)
        self.first_col_stretches.grid(row=8, column= 0,  padx=4, pady=5)
        self.first_col_stretches.config(font=("Times", 24), width="22", height="16", bg="#27233A") 

        self.second_col_stretches = tk.Listbox(self.tab2)
        self.second_col_stretches.grid(row=8, column= 1, padx=4, pady=5)
        self.second_col_stretches.config(font=("Times", 24), width="22", height="16", bg="#27233A")

        self.third_col_stretches = tk.Listbox(self.tab2)
        self.third_col_stretches.grid(row=8, column= 2, padx=4, pady=5)
        self.third_col_stretches.config(font=("Times", 24), width="22", height="16", bg="#27233A")

#  tab 3 -----------------------------------------------------------------------------------------

        self.boxing_name_label = tk.Label(self.tab3, text="Let's do kickboxing!")
                                                            # lavander blush X dark-purple
        self.boxing_name_label.config(font=("times", 36), fg="#F9C22E", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.boxing_name_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.boxing_pause_button = tk.Button(self.tab3, text="Preview", command=lambda:self.preview_boxing_workout())
        self.boxing_pause_button.grid(row=1, column=0, padx=5, pady=5)
        self.boxing_pause_button.config(font=("times", 14), fg="#BEA7E5", bg="black")

        self.boxing_timer_label = tk.Label(self.tab3, text="Sec/Move")
                                                            #  ice blue
        self.boxing_timer_label.config(font=("times", 22), fg="#9BF3F0", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.boxing_timer_label.grid(row=1, column=1, padx=5, pady=5)

        self.boxing_duration_slider = tk.IntVar()
        self.boxing_duration_slider = tk.Scale(self.tab3, from_=2, to=90, orient=tk.HORIZONTAL, resolution=8, variable=self.boxing_duration_slider, command=self.update_boxing_preview_label)
        self.boxing_duration_slider.set(2)
        self.boxing_duration_slider.grid(row=1, column=2, padx=2)

        # self.boxing_start_button = tk.Button(self.tab2, text="Randomize Session", command=self.initialize_stretches_update_display)
        self.boxing_start_button = tk.Button(self.tab3, text="START", command=self.start_boxing_routine)
        self.boxing_start_button.grid(row=2, column=0, padx=5, pady=5)
        self.boxing_start_button.config(font=("impact", 14), fg="#52FFB8", bg="black")

        self.boxing_time_length_label = tk.Label(self.tab3, text="# of Moves")
        self.boxing_time_length_label.grid(row=2, column=1, padx=5, pady=5)
                                                                #  aquamarine X dark-purple
        self.boxing_time_length_label.config(font=("times", 22), fg="#52FFB8", bg="#27133A")

        self.boxing_move_number_slider = tk.IntVar()
        self.boxing_move_number_slider = tk.Scale(self.tab3, from_=2, to=30, orient=tk.HORIZONTAL, resolution=2, variable=self.boxing_move_number_slider, command=self.update_boxing_preview_label)
        self.boxing_move_number_slider.set(2)
        self.boxing_move_number_slider.grid(row=2, column=2, padx=2)

        self.stretch_pause_button = tk.Button(self.tab3, text="Pause/Resume", command=self.toggle_boxing_timer)
        self.stretch_pause_button.grid(row=3, column=0, padx=5, pady=5)
        self.stretch_pause_button.config(font=("Times", 14), fg="#9BF3F0", bg="black")

        self.boxing_time_preview_label = tk.Label(self.tab3, text="Est. Time: (adjust sliders)")
        self.boxing_time_preview_label.grid(row=3, column=1, columnspan= 3, padx=2, pady=5)
                                                                #  aquamarine X dark-purple
        self.boxing_time_preview_label.config(font=("times", 22), fg="#52FFB8", bg="#27133A")


        self.boxing_timer_display = tk.Label(self.tab3, text="[time display]")
        self.boxing_timer_display.grid(row=4, column=0, columnspan= 4, padx=2, pady=5)
                                                                #  aquamarine X dark-purple
        self.boxing_timer_display.config(font=("times", 34), fg="lime", bg="black")

    # ------ tab4 Initialize widgets ------------------------------------------------------------------------------------
        self.exercise_label = tk.Label(self.tab4, text="Exercise:")
        self.exercise_label.config(font=("times", 24), fg="lime", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.exercise_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.timer_label = tk.Label(self.tab4, text="Time Remaining:")
        self.timer_label.config(font=("courier", 22), fg="lime", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.timer_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.set_number_label = tk.Label(self.tab4, text="Set not started")
        self.set_number_label.config(font=("courier", 22), fg="cyan", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.set_number_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        # Labels for sliders  -----------------------------------------------------------------------

        self.num_sets_label = tk.Label(self.tab4, text="Sets per exercise")
        self.num_sets_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_sets_label.grid(row=3, column=0)

        self.num_motions_label = tk.Label(self.tab4, text="# Motions")
        self.num_motions_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_motions_label.grid(row=3, column=1)

        self.active_duration_label = tk.Label(self.tab4, text="work (s)")
        self.active_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.active_duration_label.grid(row=3, column=2)

        self.rest_duration_label = tk.Label(self.tab4, text="interval (s)")
        self.rest_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.rest_duration_label.grid(row=3, column=3)

        # nyi combobox dropdown for muscle groups -----------------------------------------------------------------------
        # self.num_target_groups = tk.Label(master, text="num target muscle groups")
        # self.num_target_groups.config(font=("Times", 12), fg="#cc3", bg="#225") 
        # self.num_target_groups.grid(row=2, column=1)
        
# Create Scale widgets -----------------------------------------------------------------------
        # Create Tkinter variables to store the values of the sliders
        
        self.num_sets_slider = tk.IntVar()
        self.num_sets_slider = tk.Scale(self.tab4, from_=1, to=8, orient=tk.HORIZONTAL, variable=self.num_sets_slider, command=self.update_workout_timing_preview_label)
        self.num_sets_slider.set(3)
        self.num_sets_slider.grid(row=4, column=0, padx=5)

        self.num_motions = tk.IntVar()
        self.num_motions = tk.Scale(self.tab4, from_=2, to=20, orient=tk.HORIZONTAL,variable=self.num_motions, command=self.update_workout_timing_preview_label)
        self.num_motions.set(3)
        self.num_motions.grid(row=4, column=1, padx=5)
        
        self.active_duration_slider = tk.IntVar()
        self.active_duration_slider = tk.Scale(self.tab4, from_=6, to=90, orient=tk.HORIZONTAL, resolution=5, variable=self.active_duration_slider, command=self.update_workout_timing_preview_label)
        self.active_duration_slider.set(6)
        self.active_duration_slider.grid(row=4, column=2, padx=5)

        self.interval_duration_slider = tk.IntVar()
        self.interval_duration_slider = tk.Scale(self.tab4, from_=6, to=120, orient=tk.HORIZONTAL, resolution=3, variable=self.interval_duration_slider, command=self.update_workout_timing_preview_label)
        self.interval_duration_slider.set(6)
        self.interval_duration_slider.grid(row=4, column=3, padx=5)
        
        self.workout_timing_data_label = tk.Label(self.tab4, text="awaiting input data proper...")
        self.workout_timing_data_label.grid(row=6, column=0, columnspan=4, padx=5)
        self.workout_timing_data_label.config(font=("courier", 18), fg="cyan", bg="black")

        self.start_button = tk.Button(self.tab4, text="Start Session", command=self.start_workout_hard_x_soft_pattern)
        self.start_button.grid(row=7, column=0, padx=5, pady=5)
        self.start_button.config(font=("impact", 14), fg="lime", bg="black")

        self.pause_button = tk.Button(self.tab4, text="Pause/Resume", command=self.toggle_hard_timer)
        self.pause_button.grid(row=7, column=1, padx=5, pady=5)
        self.pause_button.config(font=("Times", 14), fg="yellow", bg="black")

        self.rand_snd_button = tk.Button(self.tab4, text="random sound", command=lambda: self.get_and_play_rand_aud_to_end(self.end_bumper_aud_arr, self.temp_end_bumper_aud_arr))
        self.rand_snd_button.grid(row=7, column=2, padx=5, pady=5)
        self.rand_snd_button.config(font=("impact", 14), fg="cyan", bg="black")

        self.listbox_of_chosen_exercises = tk.Listbox(self.tab4)
        self.listbox_of_chosen_exercises.grid(row=8, column= 0, columnspan=2, padx=2, pady=5)
        self.listbox_of_chosen_exercises.config(font=("Times", 23), width="34", height="12", fg="lime", bg="black") 

        self.listbox_of_interval_activities = tk.Listbox(self.tab4)
        self.listbox_of_interval_activities.grid(row=8, column= 2, columnspan=2, padx=2, pady=5)
        self.listbox_of_interval_activities.config(font=("Times", 23), width="34", height="12", fg="lime", bg="black") 
       
        # self.completed_exercises_text = tk.Text(self.tab4, height=10, width=40)
        # self.completed_exercises_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
























        

























        # Initialize variables
        self.selected_exercises = []
        self.selected_interval_actions = []
        self.selected_stretches = []
        # ------------- NYI need to change muscle group selection
        self.target_muscle_group_keyword = "shoulders"
        self.target_muscle_group_list = exercise_lists.shoulder_exercises
        self.interval_activity_keyword = "abs"
        self.interval_activity_list = exercise_lists.bodyweight_abs_single_motion_list
        self.workout_data_list = []

        self.countdown_done = False
        self.pause = True
        self.remaining_action_time = 0
        self.remaining_interval_time = 0
    
        self.duration_in_mins = 0
        self.is_it_action_time = True
        self.num_exercises = 0
        self.num_sets_per_exercise = 0
        self.current_exercise_index = 0
        self.current_round_index = 0

        # used in tab2, for stretches, the stretch time slider will update this
        self.standing_stretch_only = False
        self.continuous_action_time = 0
        self.current_continuous_action_index = 0

        self.boxing_workout_move_list = ["default string"]
        self.boxing_duration_in_mins = 0





















    def are_all_boxes_empty(self, var_set):
        for var in var_set.values():
            if var.get():  # If the value of the BooleanVar is True (checkbox is checked)
                return False
        return True



    def get_filtered_workout_items(self):
       
        included_muscles = [muscle for muscle, var in self.muscle_vars.items() if var.get()]
        excluded_muscles = [muscle for muscle, var in self.muscle_vars_to_exclude.items() if var.get()]
        included_traits = [trait for trait, var in self.trait_vars.items() if var.get()]
        excluded_traits = [trait for trait, var in self.trait_vars_to_exclude.items() if var.get()]
        print(f" included muscles: {included_muscles}\n excluded musc. {excluded_muscles}\n included traits {included_traits}\n excluded traits {excluded_traits}")
        

        filtered_moves = [
            exercise for exercise in all_exercise_objects
            # Must include at least 1 of the indicated muscle group, or anything if all boxes are empty
            if (all(muscle in exercise.info_list for muscle in included_muscles) or self.are_all_boxes_empty(self.muscle_vars))
            # exclude any exercises with the exclusion tags
            and not any(muscle in exercise.info_list for muscle in excluded_muscles)
            and (all(trait in exercise.info_list for trait in included_traits) or self.are_all_boxes_empty(self.trait_vars))
            and not any(trait in exercise.info_list for trait in excluded_traits)
        ]
        temp_001arr = []
        for item in filtered_moves:
            temp_001arr.append(item.key_name)
        print(temp_001arr)
        print(f"-"*23)
        print(f"Length of selection = {len(temp_001arr)}")

        # Randomly select up to 3 moves
        selected_moves = random.sample(filtered_moves, min(3, len(filtered_moves)))
        # Update the combo box area with the selected moves
        self.combo_box002.delete(0, tk.END)
        combobox_counter = 0
        for move in selected_moves:
            combobox_counter +=1
            for display_name in move.display_name_list:
                    self.combo_box002.insert(tk.END, display_name)
            print(f"move is: {move.display_name_list}")


    # def simply_play_bgm_once(self, targetAudFile):
    #     pygame.mixer.music.load(targetAudFile)
    #     pygame.mixer.music.play(loops=0)     
          
    # Toggle timer countdown
    def toggle_hard_timer(self):
        self.pause = not self.pause
        if not self.pause:
            self.update_timer_hard_x_soft_pattern()
        else:
            pygame.mixer.music.stop()

    def toggle_warmup_timer(self):
        self.pause = not self.pause
        if not self.pause:
            self.update_timer_continuous_action_pattern()
        else:
            pygame.mixer.music.stop()

    def toggle_boxing_timer(self):
        self.pause = not self.pause
        if not self.pause:
            if len(self.temp_active_song_aud_arr) == 0:
                    self.copy_src_arr_to_temp(audio_doc.outsourced_active_song_aud_arr, self.temp_active_song_aud_arr)
# .pop() progressively reduces the length of the active song array
            chosen_bgm = self.temp_active_song_aud_arr.pop()
            duration_of_boxing_movement = self.boxing_duration_slider.get()
            pygame.mixer.music.load(chosen_bgm)
            # Play the background track (the .stop() clauses should halt this...)
            pygame.mixer.music.play()
            self.update_boxing_timer_and_manage_aud_triggers()
        else:
            pygame.mixer.music.stop()

    def update_boxing_preview_label(self, value):
        time_per_boxing_exercise = self.boxing_duration_slider.get()
        num_boxing_moves = self.boxing_move_number_slider.get()
        self.boxing_duration_in_mins = math.ceil((num_boxing_moves*(time_per_boxing_exercise))/60)
        boxing_time_string = f"Est. Time: {self.boxing_duration_in_mins} mins \n{num_boxing_moves} moves at {time_per_boxing_exercise}s each."
        self.boxing_time_preview_label.config(text=boxing_time_string)
    
    def get_boxing_arr(self):
        # need to divide by 2 because all moves are L/R mirrored and come in pairs, but input is for each set to iterate over, not individual
        n_of_moves_halved = int((self.boxing_move_number_slider.get())/2)
        boxing_output_arr = make_martial_arts.get_string_list(n_of_moves_halved)
        # reset the boxing move list to an empty string so we can repopulate it
        self.boxing_workout_move_list = []
        for x in boxing_output_arr:
            self.boxing_workout_move_list.append(x)

    def preview_boxing_workout(self):
        self.get_boxing_arr()
        boxing_move_display_string = "\n".join(self.boxing_workout_move_list[0][:-1])
        self.boxing_name_label.config(text=boxing_move_display_string)
        self.boxing_timer_display.config(text="Time left: " + str(self.boxing_duration_slider.get()), fg="lime", bg="black")

    def start_boxing_routine(self):
        self.pause = False
        self.copy_src_arr_to_temp(audio_doc.outsourced_active_song_aud_arr, self.temp_active_song_aud_arr)
        # if the workout move list item has the default string in it, means no preview was made, so we need to make the moves array and update the display
        if self.boxing_workout_move_list[0] == "default string":
            self.preview_boxing_workout()
        self.remaining_action_time = self.boxing_duration_slider.get()
        self.manage_boxing_audio_cues(self.boxing_workout_move_list[0])
        self.update_boxing_timer_and_manage_aud_triggers()
        # otherwise, we can assume there's the array of moves already exists
# self.current_exercise_index = 0

    def manage_boxing_audio_cues(self, input_list_of_strings):
        for current_word in input_list_of_strings:
            if current_word == "Right":
                rand_right_bark = random.choice(voice_43e_right_auds)
                pygame.mixer.music.stop()
                pygame.mixer.Sound(rand_right_bark).play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
            elif current_word == "Left":
                rand_left_bark = random.choice(voice_43e_left_auds)
                pygame.mixer.music.stop()
                pygame.mixer.Sound(rand_left_bark).play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
            elif current_word == "sound_end_flag":
                # print("sound end flag reached, starting separate thread")
#  NOTE: NYI mute background music with a toggle?
                # if bgm_on == True:
# if the active song array gets depleted, then re-shuffle and regenerate with the following function 
                if len(self.temp_active_song_aud_arr) == 0:
                    self.copy_src_arr_to_temp(audio_doc.outsourced_active_song_aud_arr, self.temp_active_song_aud_arr)
# .pop() progressively reduces the length of the active song array
                chosen_bgm = self.temp_active_song_aud_arr.pop()
                duration_of_boxing_movement = self.boxing_duration_slider.get()
                bgm_thread = threading.Thread(target=self.play_bg_audio_until_end, args=(chosen_bgm,))
                bgm_thread.start() 
            else:
                audio_bark = voice_43e_dictionary[current_word]
                pygame.mixer.music.stop()
                pygame.mixer.Sound(audio_bark).play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)

    def update_boxing_timer_and_manage_aud_triggers(self):
        if self.remaining_action_time == 0:
            # Check if we've reached the end of the line
            
            # len needs -1 because we're tracking from a 0 index
            if self.current_exercise_index == (len(self.boxing_workout_move_list)-1):
                # trigger ending message and jump out of the program if we've reached 0 on the last item
                print("workout over!")
                self.boxing_name_label.config(text=f"{self.boxing_duration_in_mins} min long workout over!")
                self.boxing_timer_display.config(text="Done!")
                self.write_receipt_of_boxing_workout()
                pygame.mixer.music.stop()
                pygame.mixer.Sound(self.workout_end_aud).play()
                return
            # else:
            #     print(f"Movement #{self.current_exercise_index} of {len(self.boxing_workout_move_list)}")
            # increase the targeting index. The 0th index will run the first time through because we're fueling up remaining_action_time in start_boxing_routine()
            self.current_exercise_index += 1
            # target the list of strings for the current move
            
            # input(f"curr idx = {self.current_exercise_index}\ncurrent move {self.boxing_workout_move_list[self.current_exercise_index]}")
            curr_list_of_audio_strings = self.boxing_workout_move_list[self.current_exercise_index]
            
            # replenish action time as a new move starts
            self.remaining_action_time = self.boxing_duration_slider.get()
            # make the display string and update the label area for the name of the movement/combo
            boxing_move_display_string = "\n".join(curr_list_of_audio_strings[:-1])
            self.boxing_name_label.config(text=boxing_move_display_string)
            aud_management_thread = threading.Thread(target=self.manage_boxing_audio_cues, args=(curr_list_of_audio_strings,))
            aud_management_thread.start()
        else:
            self.remaining_action_time -= 1
            self.boxing_timer_display.config(text="Time left: " + str(self.remaining_action_time), fg="lime", bg="black")
        if not self.pause:
            self.master.after(1000, self.update_boxing_timer_and_manage_aud_triggers)

    def write_receipt_of_boxing_workout(self):
        current_time_stamp = datetime.now().strftime("%d-%m_%H-%M") 
        timestamp_filename = "boxing" + current_time_stamp + ".txt"
        with open(timestamp_filename, 'w', encoding='utf-8') as file:
            file.write(f"Boxing exercise! Duration: {self.boxing_duration_in_mins} mins ; at {current_time_stamp}\n")
            counter_var = 0
            for string_set in self.boxing_workout_move_list:
                counter_var += 1
                # only print every other because we have 2 instances of each workout item
                if counter_var % 2 ==0:
                    # ignore the first because it'll be "left/right" and the last is the aud-end flag string always
                    action_output_string = ", ".join(string_set[1:-1])
                    file.write(action_output_string+ "\n")
            file.write("and that's all she wrote!")
        print("Workout textfile completed! Check current folder for receipt of workout!")




















    def update_workout_timing_preview_label(self, value):
        num_exercises = self.num_motions.get()
        num_sets_per_exercise = self.num_sets_slider.get()
        dur_active = self.active_duration_slider.get()
        dur_interval = self.interval_duration_slider.get()
        break_interval = 0
        num_breaks = 0
        # duration_in_mins = math.ceil(((num_sets*(dur_active+dur_interval)) - dur_interval)+(break_interval * num_breaks)/60)
        self.duration_in_mins = math.ceil(((num_exercises*(num_sets_per_exercise*(dur_active+dur_interval)) - dur_interval)+(break_interval * num_breaks))/60)
        workout_stats_string = f"Total Duration: {self.duration_in_mins} minutes \n{num_exercises} exercises; {num_sets_per_exercise} sets/exercise\n {dur_active}s active, {dur_interval}s intervals"
        self.workout_timing_data_label.config(text=workout_stats_string)
    def select_actions_from_arr(self, num_actions, target_arr):
        # from target array, select a random number of unique items represented by the integer : num_actions
        selected_actions = random.sample(target_arr, num_actions)
        return selected_actions
    def get_workout_motions(self, target_muscle_group):
        self.listbox_of_chosen_exercises.delete(0, tk.END)
        self.listbox_of_interval_activities.delete(0, tk.END)
        self.workout_data_list.append(f"workout targeting: {target_muscle_group}")
        # get the text from the data label
        workout_stats = self.workout_timing_data_label.cget("text")
        self.workout_data_list.append(workout_stats)
        # --------------- NYI : Logic for different kinds of sessions in different functions?-----------------------------------------------------------------------------------
        #  !!! NYI muscle group selection with a combobox 
        target_action_list = exercise_lists.shoulder_exercises
        # populate an array object with the main exercises
        self.selected_exercises = self.select_actions_from_arr(self.num_motions.get(), target_action_list)
        for x in self.selected_exercises:
            self.listbox_of_chosen_exercises.insert(tk.END, x)
        self.pause = False
    def select_interval_activities_randomizer(self, interval_activity_source_list):
        # loop and bigger ar based on num of exercises
        big_interval_action_list = []
        for i in range(0, self.num_exercises):
            small_interval_actions_list = self.select_actions_from_arr(self.num_sets_per_exercise, interval_activity_source_list)
            big_interval_action_list.append(small_interval_actions_list)
        self.selected_interval_actions = big_interval_action_list
    def play_bg_audio_for_duration(self, file_path, duration):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        # Duration (seconds) X 1000 for miliseconds read by .wait() 
        pygame.time.wait(duration * 1000)
        # Stop playback after duration
        pygame.mixer.music.stop()
    def play_bg_audio_until_end(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    def copy_src_arr_to_temp(self, src_arr, temp_arr):
        random.shuffle(src_arr)
        for x in src_arr:
            temp_arr.append(x)
    def select_and_play_random_bg_aud(self, src_arr, temp_arr, target_dur):
        pygame.mixer.init()
        # regenerate the temp arr from the source if temp is empty
        #   --- Because we're popping off each item, the temp array loses an item each time it's run, making it less repetitive
        #   --- The copying process will shuffle the array before copying, so it's already random-order, thus just popping below
        if len(temp_arr) == 0:
            self.copy_src_arr_to_temp(src_arr, temp_arr)
        chosen_aud = temp_arr.pop(0)
        self.play_bg_audio_for_duration(chosen_aud, target_dur)
    # for getting duraiton, don't play, just get the audio data itself
    def get_random_aud(self, src_arr, temp_arr):
        if len(temp_arr) == 0:
            self.copy_src_arr_to_temp(src_arr, temp_arr)
        chosen_aud = temp_arr.pop(0)
        return chosen_aud
    def make_aud_thread_for_duration(self, src_arr, temp_arr, target_dur):
        audio_thread = threading.Thread(target=self.select_and_play_random_bg_aud, args=(src_arr, temp_arr, target_dur))
        audio_thread.start()
    # Simply plays the audio until the end, used for bumpers, not bg
    def play_audio_until_end(self, aud_file):
        pygame.mixer.init()
        pygame.mixer.Sound(aud_file).play()
    def get_and_play_rand_aud_to_end(self, src_arr, temp_arr):
        this_stupid_variable = self.get_random_aud(src_arr, temp_arr)
        self.play_audio_until_end(this_stupid_variable)
    def make_aud_thread_to_end(self, src_arr, temp_arr):
        audio_thread = threading.Thread(target=self.get_and_play_rand_aud_to_end, args=(src_arr, temp_arr))
        audio_thread.start() 
    def update_exercise_label(self):
        # from the selected exercises arr, get the current exercise via index
        current_exercise = self.selected_exercises[self.current_exercise_index]
        self.exercise_label.config(text=f"Action:\n {current_exercise}", fg="lime", bg="black")
    def update_interval_label(self):
        current_interval_motion = self.selected_interval_actions[self.current_exercise_index][self.current_round_index]
        self.exercise_label.config(text=f"Interval:\n {current_interval_motion}", fg="purple", bg="yellow")
    def trigger_starter_aud_with_bg_delay(self, duration):
        # Initialize variables for handling the sounds
        half_active_dur = math.floor(duration/2)
        first_bg_track = self.temp_active_song_aud_arr.pop()
        # NOTE: NYI, trigger encouragement at the start of each set, instead of at every time, so use self.round counter here
        starting_encouragement_aud_file = self.start_bumper_aud_arr.pop()
        first_action = self.selected_exercises[0]
        first_exercise_aud_file = random.choice(self.master_exercise_name_audio_dic[first_action])
        middle_sound_effect = pygame.mixer.Sound(self.halfway_alarm)
        # Play starting encouragement audio
        starting_encouragement_sound = pygame.mixer.Sound(starting_encouragement_aud_file)
        starting_encouragement_sound.play()
        while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            pygame.time.Clock().tick(30)
        # Play first exercise audio
        first_exercise_sound = pygame.mixer.Sound(first_exercise_aud_file)
        first_exercise_sound.play()
        while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            pygame.time.Clock().tick(30)
            
        # Load background track
        pygame.mixer.music.load(first_bg_track)
        # Play the background track once
        pygame.mixer.music.play()

        time.sleep(half_active_dur - 3)
        # (play pda beep at halfway point) Should overlap and not interrupt the bigger BG sound
        middle_sound_effect.play()
        # (do not use music.stop because the channel will automatically be overwritten when the interval sound starts)
    def start_workout_hard_x_soft_pattern(self):
        # copy the start auds and shuffle them around in a random order so we can pop them off later
        self.copy_src_arr_to_temp(self.start_bumper_aud_arr, self.temp_start_bumper_aud_arr)
        random.shuffle(self.temp_start_bumper_aud_arr)
        # Do the same for set ender barks
        self.copy_src_arr_to_temp(self.end_bumper_aud_arr, self.temp_end_bumper_aud_arr)
        random.shuffle(self.temp_end_bumper_aud_arr)
        # initialize basic stuff
        self.num_exercises = self.num_motions.get()
        self.num_sets_per_exercise = self.num_sets_slider.get()
        dur_active = self.active_duration_slider.get()
        dur_interval = self.interval_duration_slider.get()
        self.remaining_action_time = dur_active
        self.remaining_interval_time = dur_interval
        self.get_workout_motions(self.target_muscle_group_list)
        self.select_interval_activities_randomizer(self.interval_activity_list)
        self.set_number_label.config(text=f"Set 1 of {self.num_sets_per_exercise}")
        self.exercise_label.config(text=f"Action:\n {self.selected_exercises[0]}")
        # self.selected_exercises is now populated
        # Initialize the bg_audio_array
        self.copy_src_arr_to_temp(self.active_song_aud_arr, self.temp_active_song_aud_arr)
        timer_thread = threading.Thread(target=self.update_timer_hard_x_soft_pattern)
        timer_thread.start()
        init_aud_thread = threading.Thread(target=self.trigger_starter_aud_with_bg_delay, args=(dur_active,))
        init_aud_thread.start()       

    def update_timer_hard_x_soft_pattern(self):
        # top portion contains adjusting the timer while time remains for set
        # if self.is_it_action_time:
        #     self.remaining_action_time -= 1
        #     self.timer_label.config(text="Time left: " + str(self.remaining_action_time), fg="lime", bg="black")
        # else:
        #     self.remaining_interval_time -= 1
        #     self.timer_label.config(text="Time left: " + str(self.remaining_interval_time), fg="yellow", bg="black")
# ---------------------------------------------------------------------------------------------------------------- 
        # when Action timer hits zero 
        if (self.is_it_action_time) and (self.remaining_action_time == 0):
            #  End of active time, switch to Interval time
            self.update_interval_label()
            self.timer_label.config(text="Time left: " + str(self.remaining_interval_time), fg="yellow", bg="black") 
            self.is_it_action_time = False
            # we don't want to initiate the audios if it's the end of the set, checks for end of routine in block later...
            if self.current_round_index != self.num_sets_per_exercise:
                current_interval_act = self.selected_interval_actions[self.current_exercise_index][self.current_round_index]
                current_interval_activity_name_aud_file = random.choice(self.master_exercise_name_audio_dic[current_interval_act])
                interval_intro_aud = pygame.mixer.Sound(current_interval_activity_name_aud_file)

                # Check if encouragements need to regen and re-shuffle
                if self.temp_end_bumper_aud_arr:
                    relax_bark_aud = self.temp_end_bumper_aud_arr.pop()
                else:
                    self.copy_src_arr_to_temp(self.temp_end_bumper_aud_arr, self.temp_end_bumper_aud_arr)
                    random.shuffle(self.temp_end_bumper_aud_arr)
                    relax_bark_aud = self.temp_end_bumper_aud_arr.pop()
                # stop the BG from overriding the relax-bark
                pygame.mixer.music.stop()
                # pygame.mixer.music.set_volume(0.25) # lower volume instead of stopping it entirely
                relax_bark_sound_obj = pygame.mixer.Sound(relax_bark_aud)
                relax_bark_sound_obj.play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
                interval_intro_aud.play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
                self.make_aud_thread_for_duration(self.interval_song_aud_arr, self.temp_interval_song_aud_arr, (self.interval_duration_slider.get()+1))
                # pygame.mixer.music.set_volume(1)
        # when Interval timer hits zero 
        elif self.remaining_interval_time == 0:
            # reset both timing counters here, 
            self.remaining_action_time = self.active_duration_slider.get()  # Reset exercise time-amount
            self.remaining_interval_time = self.interval_duration_slider.get()  # Reset interval time-amount
            self.is_it_action_time = True
            # "round" count increases when the interval action is complete
            self.current_round_index += 1
            self.set_number_label.config(text=f"Set {self.current_round_index + 1} of {self.num_sets_per_exercise}")
            self.update_exercise_label() 
            self.timer_label.config(text="Time left: " + str(self.remaining_action_time), fg="lime", bg="black")
            if self.current_round_index != self.num_sets_per_exercise:
                # NOTE: Diagnostic below... checks on audio file selected from array within the master dictionary
                # print(f"Chose {current_action_aud_file} from : {self.master_exercise_name_audio_dic[current_exercise]}")
                current_exercise = self.selected_exercises[self.current_exercise_index]
                current_action_aud_file = random.choice(self.master_exercise_name_audio_dic[current_exercise]) 
                action_intro_aud = pygame.mixer.Sound(current_action_aud_file)
                pygame.mixer.music.stop()
                action_intro_aud.play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
                self.make_aud_thread_for_duration(self.active_song_aud_arr, self.temp_active_song_aud_arr, (self.active_duration_slider.get()+1))
        else: # If it's not zero, tick down the clock on the display and also tick down the action time var
            if self.is_it_action_time:
                self.remaining_action_time -= 1
                self.timer_label.config(text="Time left: " + str(self.remaining_action_time), fg="lime", bg="black")
            else:
                self.remaining_interval_time -= 1
                self.timer_label.config(text="Time left: " + str(self.remaining_interval_time), fg="yellow", bg="black")     

        if self.current_round_index == self.num_sets_per_exercise:
            # reset round index to 0 so it'll be used as the ordinal for the interval sub-arr
            self.current_round_index = 0
            # increase exercise index to move to the next item in selected_exercises
            self.current_exercise_index += 1
            if self.current_exercise_index >= self.num_exercises:
                print(f"exercise session complete! {self.current_exercise_index} rounds of {self.num_exercises} complete!")
                self.set_number_label.config(text="Workout Complete!")
                self.exercise_label.config(text=f"{self.duration_in_mins}mins exercise complete!", fg="lime", bg="black")
                self.timer_label.config(text=f"Done!")
                pygame.mixer.music.stop()
                pygame.mixer.music.load(self.halfway_alarm)
                pygame.mixer.music.play()
                time.sleep(0.4)
                pygame.mixer.music.load(self.workout_end_aud)
                pygame.mixer.music.play()
                return  # End of exercise routine
# Round is over, the exercise is not complete yet
            else:
                current_exercise = self.selected_exercises[self.current_exercise_index]
                current_action_aud_file = random.choice(self.master_exercise_name_audio_dic[current_exercise]) 
                initial_exercise_for_round__aud = pygame.mixer.Sound(current_action_aud_file)
                encouragement = self.default_encouragement
                # Check if encouragements need to regen and re-shuffle
                if len(self.temp_start_bumper_aud_arr) > 0:
                    encouragement = self.temp_start_bumper_aud_arr.pop()
                else:
                    self.copy_src_arr_to_temp(self.start_bumper_aud_arr, self.temp_start_bumper_aud_arr)
                    random.shuffle(self.temp_start_bumper_aud_arr)
                    encouragement = self.temp_start_bumper_aud_arr.pop()
                # reset number label to one at beginning of new exercise motion
                self.set_number_label.config(text=f"Set {self.current_round_index + 1} of {self.num_sets_per_exercise}")
                # Also call the update to the exercise label !!! yes, this is double-calling the exercise label on the last item of each iteration, FIX LATER: C-bug, optimization
                self.update_exercise_label()
                encouragement_aud = pygame.mixer.Sound(encouragement)
                encouragement_aud.play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)

                initial_exercise_for_round__aud.play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
                self.make_aud_thread_for_duration(self.active_song_aud_arr, self.temp_active_song_aud_arr, (self.active_duration_slider.get()+1))
                # Use a dictionary association to get the audio file for the current exercise in particular (same var. as in the display for the exercise)
                # print(f"{self.num_exercises - self.current_exercise_index} exercise motions remain")
                # print(self.selected_exercises[self.current_exercise_index:])
            print(f"current round index is {self.current_round_index}")
        if not self.pause:
            self.master.after(1000, self.update_timer_hard_x_soft_pattern)
            







































    def get_non_ground_continual_exercise_list_from_objects(self):
            combined_list = []
            list_of_stretch_lists = []
            selected_warmups_name_arr = []

            temp_warmup_keyword_arr = stretches_doc.warmup_keyword_arr

            # for item in random_2_starters:
            #     temp_warmup_keyword_arr.append(item)
    # Get a list of warm-ups by using the keywords on the dictionary, then shuffle the results up
            for keyword in temp_warmup_keyword_arr:
                chosen_warmup = random.choice(stretches_doc.warmup_dic[keyword])
                selected_warmups_name_arr.append(chosen_warmup)
            for special_item in stretches_doc.special_list:
                selected_warmups_name_arr.append(special_item)
            random.shuffle(selected_warmups_name_arr)
    # Get stretch arrays based off keyword
            for x in stretches_doc.stretch_keyword_arr:
                if self.standing_stretch_only == True:
                    # 0th index always is a standing variation
                    chosen_stretch_type = x[0]
                else:
                    chosen_stretch_type = random.choice(x)
                chosen_stretch_motion_arr = random.choice(stretches_doc.stretch_dic[chosen_stretch_type])
                list_of_stretch_lists.append(chosen_stretch_motion_arr)
            random.shuffle(list_of_stretch_lists)

            # print(selected_warmups_name_arr)
            # input(len(selected_warmups_name_arr))

            for i, warmup_move_name in enumerate(selected_warmups_name_arr):
                # first 2 are just warm ups, then stretch+warmup
                if i < 2:
                    # print(f"index 'i' is {i}, not in main portion yet")
                    #  select an appropriate random item from the arrays at the dictionary entry accessed by the appropriate keyword
                    combined_list.append(warmup_move_name)
                else:
                        # sub arrays keeps all hamstring sets or quad sets together even if mirrored. Needs -2 to account for skipping 2 iterations at start for initial duo of warmups
                    target_stretch_sub_arr = list_of_stretch_lists[i-2]
                    random.shuffle(target_stretch_sub_arr)
                        # ^^ also shuffling so it's not always left/right/center as data input is like
                    for individual_stretch in target_stretch_sub_arr:
                        combined_list.append(individual_stretch)
                    combined_list.append(warmup_move_name)
            self.selected_stretches =  combined_list
            print(f"# of stretch motions: {len(self.selected_stretches)}")

# Stretching pattern is rather static due to targeting whole body
    def get_stretching_exercises(self):
        combined_list = []
        list_of_stretch_lists = []
        selected_warmups_name_arr = []
        # temp_warmup_keyword_arr = []

# get 2 random exercises for warm-up, 
        # random_2_starters = random.sample(stretches_doc.warmup_keyword_arr, 2)
        # # Make a temporary array to hold all warmup keywords + the extra 2

        # Delta
        temp_warmup_keyword_arr = stretches_doc.warmup_keyword_arr

        # for item in random_2_starters:
        #     temp_warmup_keyword_arr.append(item)
# Get a list of warm-ups by using the keywords on the dictionary, then shuffle the results up
        for keyword in temp_warmup_keyword_arr:
            chosen_warmup = random.choice(stretches_doc.warmup_dic[keyword])
            selected_warmups_name_arr.append(chosen_warmup)
        for special_item in stretches_doc.special_list:
            selected_warmups_name_arr.append(special_item)
        random.shuffle(selected_warmups_name_arr)
# Get stretch arrays based off keyword
        for x in stretches_doc.stretch_keyword_arr:
            if self.standing_stretch_only == True:
                # 0th index always is a standing variation
                chosen_stretch_type = x[0]
            else:
                chosen_stretch_type = random.choice(x)
            chosen_stretch_motion_arr = random.choice(stretches_doc.stretch_dic[chosen_stretch_type])
            list_of_stretch_lists.append(chosen_stretch_motion_arr)
        random.shuffle(list_of_stretch_lists)

        # print(selected_warmups_name_arr)
        # input(len(selected_warmups_name_arr))

        for i, warmup_move_name in enumerate(selected_warmups_name_arr):
            # first 2 are just warm ups, then stretch+warmup
            if i < 2:
                # print(f"index 'i' is {i}, not in main portion yet")
                #  select an appropriate random item from the arrays at the dictionary entry accessed by the appropriate keyword
                combined_list.append(warmup_move_name)
            else:
                    # sub arrays keeps all hamstring sets or quad sets together even if mirrored. Needs -2 to account for skipping 2 iterations at start for initial duo of warmups
                target_stretch_sub_arr = list_of_stretch_lists[i-2]
                random.shuffle(target_stretch_sub_arr)
                    # ^^ also shuffling so it's not always left/right/center as data input is like
                for individual_stretch in target_stretch_sub_arr:
                    combined_list.append(individual_stretch)
                combined_list.append(warmup_move_name)
        self.selected_stretches =  combined_list
        print(f"# of stretch motions: {len(self.selected_stretches)}")

    def update_list_display_with_hilight(self, target_index_to_hilight):
    #  Clear out listbox area before 
        self.first_col_stretches.delete(0, tk.END)
        self.second_col_stretches.delete(0, tk.END)
        self.third_col_stretches.delete(0, tk.END)
        # Get the first 12 items via slice.
        for i, stretch_name in enumerate(self.selected_stretches):
            # If index is under 16, print in the first column
# NOTE : assumes column height for stretches is 16  
            if i < 16:
                # input(f"idx {i} gets col 1 >> {stretch_name}")
                #  hilight the item when it matches the current "active" motion, showing it's place in the overall workout
                if i == target_index_to_hilight:
                    self.first_col_stretches.insert(tk.END, stretch_name)
                                                                #  saffron
                    self.first_col_stretches.itemconfig(i, {'fg': '#F9C22E'})
                else:                                           
                    self.first_col_stretches.insert(tk.END, stretch_name)
                                                                # wisteria, soft color for dark-purple background
                    self.first_col_stretches.itemconfig(i, {'fg': '#BEA7E5'})
            #  exercise 12+ goes in second column at the listbox display
            elif i < 31:
                # input(f"[!] idx {i} gets col 2 >> {stretch_name}")
                #  Still check if the index matches the indicates one to hilight
                if i == target_index_to_hilight:
                    self.second_col_stretches.insert(tk.END, stretch_name)
                    self.second_col_stretches.itemconfig(i-16, {'fg': '#F9C22E'})
                else:
                    self.second_col_stretches.insert(tk.END, stretch_name)
                    self.second_col_stretches.itemconfig(i-16, {'fg': '#BEA7E5'})
                # listbox.tag_configure("normal_font", font=normal_font)
                # listbox.tag_configure("large_font", font=large_font)
            else:
                # input(f"[@_@!] idx {i} gets col 3! >> {stretch_name}")
                #  Still check if the index matches the indicates one to hilight
                if i == target_index_to_hilight:
                    self.third_col_stretches.insert(tk.END, stretch_name)
                    self.third_col_stretches.itemconfig(i-31, {'fg': '#F9C22E'})
                else:
                    self.third_col_stretches.insert(tk.END, stretch_name)
                    self.third_col_stretches.itemconfig(i-31, {'fg': '#BEA7E5'})

    def update_stretch_timing_preview_label(self, value):
        if len(self.selected_stretches) == 0:
            # NOTE: this is a recursive call to generate the stretching exercises, then call this update again, as well as updating the preview list
            # this generates a preview if messing with the slider before hitting the preview button
            self.initialize_stretches_update_display()
        num_of_stretches = len(self.selected_stretches)
        # initialize stretching time to slider variable
        self.continuous_action_time = self.stretch_duration_slider.get()
        # Calculate the time of the stretching workout
        total_stretch_time_in_seconds = (self.continuous_action_time)*(num_of_stretches)
        total_stretch_set_time_in_mins = math.ceil((total_stretch_time_in_seconds)/60)
        self.stretch_time_length_label.config(text=f"Workout time total: {total_stretch_set_time_in_mins}m")
        
    def initialize_stretches_update_display(self):
        # Get the randomized list of exercises
        self.get_stretching_exercises()
        # display the rolled exercises, hilighting the 0th index
        self.update_list_display_with_hilight(0)

        self.update_stretch_timing_preview_label(self.stretch_duration_slider.get())
        # num_of_stretches = len(self.selected_stretches)
        # # initialize stretching time to slider variable
        # self.continuous_action_time = self.stretch_duration_slider.get()
        # # Calculate the time of the stretching workout
        # total_stretch_time_in_seconds = (self.continuous_action_time)*(num_of_stretches)
        # total_stretch_set_time_in_mins = math.ceil((total_stretch_time_in_seconds)/60)
        # self.stretch_time_length_label.config(text=f"Workout time total: {total_stretch_set_time_in_mins}m")

        # Update the label for the active stretch name; we're starting at index 0, thus the initial target here
        self.stretch_name_label.config(text=f"{self.selected_stretches[0]}")

    def start_continuous_session(self):    
        # Initialize the bg_audio_array
        self.copy_src_arr_to_temp(self.active_song_aud_arr, self.temp_active_song_aud_arr)
        random.shuffle(self.temp_active_song_aud_arr)
        # copy the start auds and shuffle them around in a random order so we can pop them off later
        self.copy_src_arr_to_temp(self.start_bumper_aud_arr, self.temp_start_bumper_aud_arr)
        random.shuffle(self.temp_start_bumper_aud_arr)
        # Do the same for set ender barks
        self.copy_src_arr_to_temp(self.end_bumper_aud_arr, self.temp_end_bumper_aud_arr)
        random.shuffle(self.temp_end_bumper_aud_arr) 
        # Activate the timer by turning the pause Boolean to False
        self.pause = False 
        #  if the selected_stretches arr is not empty, then it was already generated. 
        if self.selected_stretches:
            print("[+] preview generation of stretches detected, skipping regen of stretch set")
        else: # If there's an empty list, we need to make a list with this function.
            self.initialize_stretches_update_display()
        stretch_timer_thread = threading.Thread(target=self.update_timer_continuous_action_pattern)
        stretch_timer_thread.start()
        self.create_and_call_stretch_aud_threads()
    def trigger_starter_stretch_audio(self):
        # start the timer to half so it's not blocked by anything, running in background thread
        current_stretch = self.selected_stretches[self.current_continuous_action_index]
        current_stretch_aud_file = random.choice(self.master_exercise_name_audio_dic[current_stretch])
        stretch_name_audio = pygame.mixer.Sound(current_stretch_aud_file)

        # Start motion encouragement EDITED OUT CURRENTLY (functionality works, but is a bit annoying in practice)
        # if self.temp_start_bumper_aud_arr:
        #     motion_start_encouragement = self.temp_start_bumper_aud_arr.pop()
        # else:
        #     self.copy_src_arr_to_temp(self.start_bumper_aud_arr, self.temp_start_bumper_aud_arr)
        #     random.shuffle(self.temp_start_bumper_aud_arr)
        #     motion_start_encouragement = self.temp_start_bumper_aud_arr.pop()
        # encouragement_1_sound_obj = pygame.mixer.Sound(motion_start_encouragement)
        # encouragement_1_sound_obj.play()
        # while pygame.mixer.get_busy():  # Wait for the sound to finish playing
        #     pygame.time.Clock().tick(30)

        stretch_name_sound_obj = pygame.mixer.Sound(stretch_name_audio)
        stretch_name_sound_obj.play()
        while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            pygame.time.Clock().tick(30)     
    def play_half_and_end_chirps_after_delay(self, duration_time):
        half_duration_in_seconds = math.floor(duration_time/2)
        pygame.time.wait((half_duration_in_seconds*1000)) 
        # at halfway point, Playing statically assigned halfway-alarm
        half_alarm_aud_obj = pygame.mixer.Sound(self.halfway_alarm)
        half_alarm_aud_obj.play()
        # at end, Playing statically assigned end-alarm
        #  - We're only waiting half the duration because we already waited for the first half

        # add 1 second if the time is odd, so the audio triggers correctly at the 0th countdown instead of at 1
        # We still need to offset it slightly early so it's not overlapping with the starter audio
        # NOTE: Bootleg fix for the initial delay of the timer on first run-through. It's consistent thereafter...
        wait_time_to_end = (half_duration_in_seconds*1000)
        if self.current_continuous_action_index == 0:
            # print(f"prev wait time in ms = {wait_time_to_end}")
            # print(f"0th index of stretches detected, lowering wait time to compensate for inconsistent clockwork")
            wait_time_to_end -= 1000
            # print(f"post reduction wait time {wait_time_to_end}")
        
        pygame.time.wait(wait_time_to_end) 
        half_alarm_aud_obj = pygame.mixer.Sound(self.end_alarm)
        half_alarm_aud_obj.play() 
    def create_and_call_stretch_aud_threads(self):
        duration_in_s = self.stretch_duration_slider.get()
        pygame.mixer.music.stop()
        # play the stretch audio
        self.trigger_starter_stretch_audio()

        bark_thread = threading.Thread(target=self.play_half_and_end_chirps_after_delay, args=(duration_in_s, ))
        bark_thread.start()
        # init_aud_thread = threading.Thread(target=self.trigger_starter_stretch_audio)
        # init_aud_thread.start()

        # Get next music track and activate after the other audio threads are done being scum
        if len(self.temp_active_song_aud_arr) == 0:
            # regenerate temp bg audio array if all have been popped off
            self.copy_src_arr_to_temp(self.active_song_aud_arr, self.temp_active_song_aud_arr)
            random.shuffle(self.temp_active_song_aud_arr)
        curr_bg_aud = self.temp_active_song_aud_arr.pop()
        pygame.mixer.music.load(curr_bg_aud)
        pygame.mixer.music.play()
        # bgm_thread = threading.Thread(target=self.simply_play_bgm_once, args=(curr_bg_aud, ))
        # bgm_thread.start()

    def update_timer_continuous_action_pattern(self):
        # If there's still time left on the clock...
        if self.continuous_action_time != 0:
            self.stretch_timer_label.config(text="Time left : " + str(self.continuous_action_time), fg="yellow", bg="black")
            self.continuous_action_time -= 1
        else:
            self.stretch_timer_label.config(text="Time up!", fg="#931621", bg="#0077B6")
            # reset the continuous action time
            # increase the index counter up by one, then update the display
            self.current_continuous_action_index += 1
            if len(self.selected_stretches) == self.current_continuous_action_index:
                print("program completed!")
                pygame.mixer.music.stop()
                pygame.mixer.music.load(self.workout_end_aud)
                pygame.mixer.music.play()
                return "finished"
            # else:
            #     print(f"{len(self.selected_stretches)} =/?= {self.current_continuous_action_index} ?")
            # restore the continuous action time countdowner thing... 
            self.continuous_action_time = self.stretch_duration_slider.get()
            # print(f"type of curr..idx {type(self.current_continuous_action_index)} \n type of len applied to selected stretches arr: {type(len(self.selected_stretches))}\n {self.current_continuous_action_index} of {len(self.selected_stretches)}" )
            # update the exercise label at the top, using the index
            self.stretch_name_label.config(text=f"{self.selected_stretches[self.current_continuous_action_index]}")
            # update listbox display
            self.update_list_display_with_hilight(self.current_continuous_action_index)
            # Make audio thread; use duration of the action time to control for half and end chirps
            
            self.create_and_call_stretch_aud_threads()
        
        if not self.pause:
            self.master.after(1000, self.update_timer_continuous_action_pattern)

def main():
    root = tk.Tk()
    app = ExerciseTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
