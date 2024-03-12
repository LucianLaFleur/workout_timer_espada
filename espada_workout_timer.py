import tkinter as tk
from tkinter import ttk
# from datetime import datetime
import random
import pygame
import math
import time
import threading
import audio_doc
import stretches_doc

# -------------- Color scheme note for other tabs -----------------------------------
   # Main color BG: DARK PURPLE: #27233A 
    # # carmine #931621
    #  saffron #F9C22E
    # timberwolf grey #D5C7BC
    # hunter green #34623F
    #  lemon chiffon #FEF6C9
    #  wisteria #BEA7E5
    #  field drab (olive, dark) #73683B
    #  ice blue #9BF3F0
    # honolulu blue #0077B6
    # sienna 	#A0522D
# -------------- / Color scheme note  -----------------------------------------------

class ExerciseTimerApp:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Exercise Timer")

        # Set the width and height of the window
        self.master.geometry("1105x820")
        # Assign fixed width to column 1
        # self.master.grid_columnconfigure(1, minsize=235)

        # Create a Notebook widget to manage tabs
        self.tab_manager = ttk.Notebook(master)
        self.tab_manager.pack(fill="both", expand=True)
        
        self.tab1 = ttk.Frame(self.tab_manager)
        self.tab_manager.add(self.tab1, text="Hard x Soft")

        self.tab2 = ttk.Frame(self.tab_manager)
        self.tab_manager.add(self.tab2, text="Stretches")

        #  initialize pygame so I can play music properly
        pygame.init()
        # Load Stretches from stretches_doc.py --------------------------------------------------------------------------------------------------
        # self.stretches_arr = stretches_doc
        # ---------------------------------------------------------------------------------------------------------
        #  Audio collection (safe for sharing)
        self.default_encouragement = "audio_hit_start/letsGetMovingBubblegum1.wav"
        self.halway_alarm = "audio_hit_half/pdaBeepBeep.wav"
        # self.half_bumper_aud_arr = ["audio_hit_half/pdaBeepBeep.wav"]
        # self.temp_half_bumper_aud_arr = []
        self.workout_end_aud = "audio_special_ender/exitBumperGonnaMakeIt.wav"
        # ---------------------------------------------------------------------------------------------------------
        # audio_hit_start/
        self.start_bumper_aud_arr = ["audio_hit_start/doYourBestBubblegum.wav", "audio_hit_start/fireupBubblegum1.wav", "audio_hit_start/kickoffBubblegum.wav", "audio_hit_start/letsGetMovingBubblegum1.wav",
       "audio_hit_start/letsGetMovingBubblegum1.wav", "audio_hit_start/showOnRoadBubblegum.wav", "audio_hit_start/time2grindBubblegum.wav"]
        self.temp_start_bumper_aud_arr = []
        # audio_active_songs/
        self.active_song_aud_arr = audio_doc.outsourced_active_song_aud_arr
        self.temp_active_song_aud_arr = []   
        # audio_hit_end/
        self.end_bumper_aud_arr = [
        # "audio_hit_end/catchBreathBubblefum.wav",
        # "audio_hit_end/doneBubblegum2.wav", 
        # "audio_hit_end/dontOverexertBubblegum1.wav"
        # 
        "audio_hit_end/niceWorkBubblegum1.wav", 
        # "audio_hit_end/pauseBubblegum1.wav", 
        # "audio_hit_end/slowAndSteady1.wav", 
        # "audio_hit_end/takeABreatherBubblegum.wav",
        "audio_hit_end/mori_nicework.wav",
        "audio_hit_end/mori_onemoreDone.wav",
        "audio_hit_end/mori_take_a_breather.wav",
        
        "audio_hit_end/mori_switch_to_low_intensity.wav",
        # "audio_hit_end/bubblegumPauseForAMoment.wav",
        # "audio_hit_end/bubblegum_oneMoreDown.wav",
        # "audio_hit_end/bubblegum_slow_and_Steady.wav",
        # "audio_hit_end/bubblegum_niceWorkThatOne.wav",
        "audio_hit_end/bubblegum_takeABreather.wav",
        "audio_hit_end/bubble_thatonesdone.wav"
        # "audio_hit_end/.wav",
        ]

        # self.end_of_workout_arr = [
        # "audio_hit_end/finished1bubblegum.wav",
        # "audio_hit_end/mori_nice_jobrestforabit.wav",
        # "audio_hit_end/bubblegum_time_to_rest.wav"
        # ]

        self.temp_end_bumper_aud_arr = []
        # audio_interval_songs/
        self.interval_song_aud_arr = ["audio_interval_songs/all_you_can_do_cut.wav", 
        "audio_interval_songs/anhedonia_short.wav",
        "audio_interval_songs/beat4354rs.wav", 
        "audio_interval_songs/knifeOverHeart1.wav", 
        "audio_interval_songs/LoyalObligation_cut.wav",
        "audio_interval_songs/purple_aviators_cut.wav", 
        "audio_interval_songs/technical_complications.wav",
        "audio_interval_songs/VacuousCuriosity.wav", 
        "audio_interval_songs/DailyRounds.wav", 
        "audio_interval_songs/WhatCannotBeReclaimed.wav"]
        self.temp_interval_song_aud_arr = []
        # audio_special_ender/
        self.special_ender_aud_arr = []
        self.temp_special_ender_aud_arr = []

        # List of exercises
        # biceb and general arms stuff
        self.arm_exercises = ["walking push-ups", "sumo-squat push-ups", "T-plank alternating push-ups",  
        "crunching bicep curl", "pike push-up", "plank-tuck walk-up", "alternating plank-tuck", "alternating crab bridge reaches",
        "plank-tuck push-up", "planche push-up", "push-up pop-ups", "frog stand to ukemi",  
        "reverse-palm push-up", "dive-bomber push-up", "lying reverse biceb curl", "Alternating Moscow T-planks", 
        "towel reverse biceb curl", "lying towel hammer curl", "shoulder tension circles", "walk the plank"
        # walk the plank is inchworm
        # mirrored below
        "lying side bicep suitcase", "single-arm crab-reach", "uppercut-cross", "side-chop cross", "palm to karate chop"]

        self.ticep_exercises = [
        "tricep dips", 
        "dolphin push-up", 
        "plank to seal-pose", 
        "sphinx dive-bombers", 
        "alternating leg tricep dips",
        "elbows-back push-ups",
        "tricep get-ups",
        "lying side push-up",
        "diamond pushup", 
        "sphynx to plank crawler", 
        "sphynx to pike-push crawler", 
        "sphynx-pike-stand", 
        # "tricep push" #requires bench
        ]

        self.shoulder_exercises = ["pike position cross toe-touches", 
        "pike push-up", "plank shoulder taps",  "bear crawl", "slow and low crawl","supermans",
        "lying lat pull-downs", "snow angel shoulders", "flying cobra", "reaching row", "tension lat pull-downs", 
        "lat pull-down push-out" 
        # lat pull-down and push out is like a lateral row then extend arms at 90 degrees out
        # "back-splash reach-outs", "pike walkout push-ups", "alternating shoulder swimmers", "superman swimmers"
        ]

        self.master_exercise_name_audio_dic = {
        # Shoulders
        "bear crawl": ['exercise_names/bearCrawlBubble.wav'], 
        "boat row" : ["exercise_names/23B_boatRow.wav"],
        "flying cobra": ["exercise_names/elf_flying_cobra.wav", "exercise_names/flyingCobraBubble.wav"],
        "lat pull-down push-out" : ["exercise_names/elf_kneeling_lat_pull_down_push_outs.wav"],
        "lying lat pull-downs": ["exercise_names/lyingLatPullDownBubblegum.wav"],
        "pike position cross toe-touches":["exercise_names/elf_pike_position_cross_toe_touches.wav", "exercise_names/pikePositionCrossToeBubblegum.wav"], 
        "pike push-up":["exercise_names/elf_pike_push_up.wav", "exercise_names/pikePushUpBubblegum.wav"],
        "plank shoulder taps":["exercise_names/elf_plank_shoulder_taps.wav", "exercise_names/plankShoulderTapsbub.wav"], 
        "reaching row" : ["exercise_names/reachingRowBubble.wav"], 
        "slow and low crawl": ["exercise_names/elf_slow_and_low_crawl.wav"],
        "snow angel shoulders":["exercise_names/snowAngelShoulders1.wav"],
        "supermans": ["exercise_names/elf_supermans.wav"],
        "tension lat pull-downs":["exercise_names/tensionLatPullDownBubblegum.wav","exercise_names/elf_tension_lat_pull_downs.wav"],
        
        # abs
        "flutter kicks": ["exercise_names/flutterkickBubblegum.wav"], 
        "full extension cross-crunch":["exercise_names/23B_fullExtensionCrossCrunch.wav", "exercise_names/fullextensioncrossCrunchBubblegum.wav"],
        "half windshield wiper combo": ["exercise_names/23b_halfwayWindshieldWiperCombo.wav"],
        "half-bridge hip-thrusts" : ["exercise_names/halfbridgeHipThrustsBubblegum.wav"], 
        "heels to the heavens": ["exercise_names/23b_heelsToHeavens.wav", "exercise_names/heels2HeavensBubblegum.wav"],
        "leg lifts, candle pose": ["exercise_names/23B_legLiftsCandlePose.wav", "exercise_names/legLiftCandleBubblegum.wav"], 
        "oblique heel-taps":["exercise_names/23b_obliqueHeelTaps.wav", "exercise_names/obliqueHeelTaps.wav"],
        "sideways hip raise": ["exercise_names/23B_sidewaysHipRaise.wav"],
        "windshield wiper leg lifts": ["exercise_names/23b_windshieldWiperLegLifts.wav"],
        "hatchet cross tension": ["exercise_names/23b_hatchetMotionxCross.wav"],
        "hip raise, leg extension": ["exercise_names/23B_hipRaiseLegExtension.wav"],
        "seated russian twists": ["exercise_names/23B_seatedRussianTwists.wav"]
        # "exercise_names/.wav"
        }
        
        self.abs_exercises = [
            "boat row",
            # "flutter kicks", 
            # "reverse plank, flutter kicks"
            "full extension cross-crunch", 
            # "half-bridge hip-thrusts", 
            "heels to the heavens",
            "leg lifts, candle pose",
            "oblique heel-taps",
            # The side-suitcase thing, also called a side hip crunch,
            "sideways hip raise",
            "half windshield wiper combo",
            "windshield wiper leg lifts",
            "hip raise, leg extension",
            "seated russian twists"
            # "dancing downward dog", "kneeling torso twists", "standing windmills", "standing bicycle", 
            # "standing single cross crunch", "power knee-strike", "slo-mo mountain climbers", "oblique leg lift", "leg extension side-suitcase"
            # opposite arm and leg out, then bring in
            # "bird dog crunch", 
            # pike position,single leg back kick extension to plank knee tuck, on same leg, alternating 
            # "axe handle obliques", "banana boat rocker", 
            # mirrored below:
            # "seated single axe handle", 
            # "figure-eight obliques"
            # hands are clasped for the figure-eight obliques
            ]
        
        # "empty tension bicep curl"
        #  dumbbells: seated single-arm curl

        #  at gym: chin-ups

        # leg motions/other:
        # "pike plank uppercuts", "squat to rising uppercut", 
        # "sunrise squats"
        # low squat, tiptoe reach
        
        # six o'clock tick-tock, leg lift one at a time motion...
        












#  --------- DISPLAY ---------------------------------

# ------ tab1 Initialize widgets ------------------------------------------------------------------------------------
        self.exercise_label = tk.Label(self.tab1, text="Exercise:")
        self.exercise_label.config(font=("times", 24), fg="lime", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.exercise_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.timer_label = tk.Label(self.tab1, text="Time Remaining:")
        self.timer_label.config(font=("courier", 22), fg="lime", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.timer_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.set_number_label = tk.Label(self.tab1, text="Set not started")
        self.set_number_label.config(font=("courier", 22), fg="cyan", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.set_number_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        # Labels for sliders  -----------------------------------------------------------------------

        self.num_sets_label = tk.Label(self.tab1, text="Sets per exercise")
        self.num_sets_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_sets_label.grid(row=3, column=0)

        self.num_motions_label = tk.Label(self.tab1, text="# Motions")
        self.num_motions_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_motions_label.grid(row=3, column=1)

        self.active_duration_label = tk.Label(self.tab1, text="work (s)")
        self.active_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.active_duration_label.grid(row=3, column=2)

        self.rest_duration_label = tk.Label(self.tab1, text="interval (s)")
        self.rest_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.rest_duration_label.grid(row=3, column=3)

        # nyi combobox dropdown for muscle groups -----------------------------------------------------------------------
        # self.num_target_groups = tk.Label(master, text="num target muscle groups")
        # self.num_target_groups.config(font=("Times", 12), fg="#cc3", bg="#225") 
        # self.num_target_groups.grid(row=2, column=1)
        
# Create Scale widgets -----------------------------------------------------------------------
        # Create Tkinter variables to store the values of the sliders
        
        self.num_sets_slider = tk.IntVar()
        self.num_sets_slider = tk.Scale(self.tab1, from_=1, to=8, orient=tk.HORIZONTAL, variable=self.num_sets_slider, command=self.update_workout_timing_preview_label)
        self.num_sets_slider.set(3)
        self.num_sets_slider.grid(row=4, column=0, padx=5)

        self.num_motions = tk.IntVar()
        self.num_motions = tk.Scale(self.tab1, from_=2, to=20, orient=tk.HORIZONTAL,variable=self.num_motions, command=self.update_workout_timing_preview_label)
        self.num_motions.set(3)
        self.num_motions.grid(row=4, column=1, padx=5)
        
        self.active_duration_slider = tk.IntVar()
        self.active_duration_slider = tk.Scale(self.tab1, from_=6, to=90, orient=tk.HORIZONTAL, resolution=5, variable=self.active_duration_slider, command=self.update_workout_timing_preview_label)
        self.active_duration_slider.set(6)
        self.active_duration_slider.grid(row=4, column=2, padx=5)

        self.interval_duration_slider = tk.IntVar()
        self.interval_duration_slider = tk.Scale(self.tab1, from_=6, to=120, orient=tk.HORIZONTAL, resolution=3, variable=self.interval_duration_slider, command=self.update_workout_timing_preview_label)
        self.interval_duration_slider.set(6)
        self.interval_duration_slider.grid(row=4, column=3, padx=5)
        
        self.workout_timing_data_label = tk.Label(self.tab1, text="awaiting input data proper...")
        self.workout_timing_data_label.grid(row=6, column=0, columnspan=4, padx=5)
        self.workout_timing_data_label.config(font=("courier", 18), fg="cyan", bg="black")

        self.start_button = tk.Button(self.tab1, text="Start Session", command=self.start_workout_hard_x_soft_pattern)
        self.start_button.grid(row=7, column=0, padx=5, pady=5)
        self.start_button.config(font=("impact", 14), fg="lime", bg="black")

        self.pause_button = tk.Button(self.tab1, text="Pause/Resume", command=self.toggle_timer)
        self.pause_button.grid(row=7, column=1, padx=5, pady=5)
        self.pause_button.config(font=("Times", 14), fg="yellow", bg="black")

        self.rand_snd_button = tk.Button(self.tab1, text="random sound", command=lambda: self.get_and_play_rand_aud_to_end(self.end_bumper_aud_arr, self.temp_end_bumper_aud_arr))
        self.rand_snd_button.grid(row=7, column=2, padx=5, pady=5)
        self.rand_snd_button.config(font=("impact", 14), fg="cyan", bg="black")

        self.listbox_of_chosen_exercises = tk.Listbox(self.tab1)
        self.listbox_of_chosen_exercises.grid(row=8, column= 0, columnspan=2, padx=2, pady=5)
        self.listbox_of_chosen_exercises.config(font=("Times", 23), width="34", height="12", fg="lime", bg="black") 

        self.listbox_of_interval_activities = tk.Listbox(self.tab1)
        self.listbox_of_interval_activities.grid(row=8, column= 2, columnspan=2, padx=2, pady=5)
        self.listbox_of_interval_activities.config(font=("Times", 23), width="34", height="12", fg="lime", bg="black") 
       
        # self.completed_exercises_text = tk.Text(self.tab1, height=10, width=40)
        # self.completed_exercises_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
























# ----------  Set up Tab2 widgets -------------------------------------------------------------------------------------------

        self.stretch_name_label = tk.Label(self.tab2, text="Stretching!")
                                                                # lavander blush X dark-purple
        self.stretch_name_label.config(font=("times", 24), fg="#F8E5EE", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.stretch_name_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.stretch_timer_label = tk.Label(self.tab2, text="Time not yet started")
                                                            #  aquamarine X dark-purple
        self.stretch_timer_label.config(font=("arial", 22), fg="#52FFB8", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
        self.stretch_timer_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.stretch_duration_slider = tk.IntVar()
        self.stretch_duration_slider = tk.Scale(self.tab2, from_=20, to=90, orient=tk.HORIZONTAL, resolution=5, variable=self.stretch_duration_slider, command=self.update_workout_timing_preview_label)
        self.stretch_duration_slider.set(30)
        self.stretch_duration_slider.grid(row=3, column=0, padx=2)

        self.stretch_time_length_label = tk.Label(self.tab2, text="(Generate a preivew for estimated workout time)")
        self.stretch_time_length_label.grid(row=3, column=1, columnspan=3, padx=5)
        self.stretch_time_length_label.config(font=("times", 16), fg="#F8E5EE", bg="#27133A")

        # self.stretch_half_label = tk.Label(self.tab1, text="Set not started")
        # self.stretch_half_label.config(font=("courier", 22), fg="cyan", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        # self.stretch_half_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)


        self.stretch_start_button = tk.Button(self.tab2, text="Randomize Session", command=self.preview_stretching_routine)
        self.stretch_start_button.grid(row=7, column=0, padx=5, pady=5)
        self.stretch_start_button.config(font=("impact", 14), fg="lime", bg="black")

        self.stretch_pause_button = tk.Button(self.tab2, text="NYI Start")
        self.stretch_pause_button.grid(row=7, column=1, padx=5, pady=5)
        self.stretch_pause_button.config(font=("Times", 14), fg="yellow", bg="black")

        self.stretch_pause_button = tk.Button(self.tab2, text="SND TST", command=lambda: self.get_and_play_rand_aud_to_end(self.end_bumper_aud_arr, self.temp_end_bumper_aud_arr))
        self.stretch_pause_button.grid(row=7, column=2, padx=5, pady=5)
        self.stretch_pause_button.config(font=("Times", 14), fg="yellow", bg="black")

        self.stretch_pause_button = tk.Button(self.tab2, text="Pause/Resume", command=self.toggle_timer)
        self.stretch_pause_button.grid(row=7, column=3, padx=5, pady=5)
        self.stretch_pause_button.config(font=("Times", 14), fg="yellow", bg="black")

        self.first_half_stretches = tk.Listbox(self.tab2)
        self.first_half_stretches.grid(row=8, column= 0, columnspan=2, padx=2, pady=5)
        self.first_half_stretches.config(font=("Times", 23), width="34", height="12", fg="lime", bg="black") 

        self.second_half_stretches = tk.Listbox(self.tab2)
        self.second_half_stretches.grid(row=8, column= 2, columnspan=2, padx=2, pady=5)
        self.second_half_stretches.config(font=("Times", 23), width="34", height="12", fg="lime", bg="black")



















        # Initialize variables
        self.selected_exercises = []
        self.selected_interval_actions = []
        # ------------- NYI need to change muscle group selection
        self.target_muscle_group_keyword = "shoulders"
        self.target_muscle_group_list = self.shoulder_exercises
        self.interval_activity_keyword = "abs"
        self.interval_activity_list = self.abs_exercises
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
    
    # def plain_interrupt_and_resume(self, primary_file, interrupt_file, interrupt_time, total_duration):
    #     # Start playing the primary audio
    #     self.play_bg_audio_for_duration(primary_file, total_duration - interrupt_time)

    #     # Wait for interrupt_time seconds and then interrupt with another audio
    #     pygame.time.wait(interrupt_time * 1000)
    #     self.play_bg_audio_for_duration(interrupt_file, total_duration - interrupt_time)
    # Toggle timer countdown
    def toggle_timer(self):
        self.pause = not self.pause
        if not self.pause:
            self.update_timer_hard_x_soft_pattern()
    def update_workout_timing_preview_label(self, value):
        #  STATIC VAL BELOW FOR EXERCISES
        num_exercises = self.num_motions.get()
        num_sets_per_exercise = self.num_sets_slider.get()
        dur_active = self.active_duration_slider.get()
        dur_interval = self.interval_duration_slider.get()
        break_interval = 0
        num_breaks = 0
        # duration_in_mins = math.ceil(((num_sets*(dur_active+dur_interval)) - dur_interval)+(break_interval * num_breaks)/60)
        self.duration_in_mins = math.ceil(((num_exercises*(num_sets_per_exercise*(dur_active+dur_interval)) - dur_interval)+(break_interval * num_breaks))/60)
        workout_stats_string = f"Total Duration: {self.duration_in_mins} minutes \n{num_sets_per_exercise} sets, {dur_active}s active, {dur_interval}s intervals"
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
        #  !!! NYI muscle group selection with a combobox (if combobox = arms, then self.arm_exercises...)
        target_action_list = self.shoulder_exercises
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
        middle_sound_effect = pygame.mixer.Sound(self.halway_alarm)
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
            # print(f"current round index is {self.current_round_index}")
            # print(f"Current exercise motion is {self.current_exercise_index +1} of {self.num_exercises}")
            if self.current_exercise_index >= self.num_exercises:
                print(f"exercise session complete! {self.current_exercise_index} rounds of {self.num_exercises} complete!")
                self.set_number_label.config(text="Workout Complete!")
                self.exercise_label.config(text=f"{self.duration_in_mins}mins exercise complete!", fg="lime", bg="black")
                self.timer_label.config(text=f"Done!")
                pygame.mixer.music.stop()
                pygame.mixer.music.load(self.halway_alarm)
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
                pygame.mixer.music.stop()
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
        # on completing a full set of rounds interval, increase index by 1 to move to the next 
                # self.current_exercise_index += 1    
            

























    # ----------------------------------------------------------------------------------------------------------------------------------------------
 
    def get_stretching_exercises(self):
        stretch_keyword_arr = stretches_doc.master_stretch_keyword_arr
        chosen_stretching_types = [] 
        output_list_of_stretches = []
        for mini_array in stretch_keyword_arr:
            #  NYI standing only stretch: toggle with self.standing_stretch_only_bool
            # selected_term = mini_array[0]
            selected_term = random.choice(mini_array)
            chosen_stretching_types.append(selected_term)
        random.shuffle(chosen_stretching_types)
        for x in chosen_stretching_types:
            chosen_stretch_possibilities = stretches_doc.master_stretch_dic[x]
            chosen_stretch_sub_arr= random.choice(chosen_stretch_possibilities)
            for movement in chosen_stretch_sub_arr:
                output_list_of_stretches.append(movement)
        return output_list_of_stretches
    
    def update_display_listing_stretches(self, stretch_list):
    #  Clear out listbox area before 
        self.first_half_stretches.delete(0, tk.END)
        self.second_half_stretches.delete(0, tk.END)
        if len(stretch_list) < 13:
            for stretch_name in stretch_list:
                self.first_half_stretches.insert(tk.END, stretch_name)
        else:
            # Get the first 12 items via slice.
            for first_chunk_stretch in (stretch_list[:12]):
                self.first_half_stretches.insert(tk.END, first_chunk_stretch)
            for second_chunk_stretch in (stretch_list[12:]):
                self.second_half_stretches.insert(tk.END, second_chunk_stretch)
    
    def preview_stretching_routine(self):
        # copy the start auds and shuffle them around in a random order so we can pop them off later
        self.copy_src_arr_to_temp(self.start_bumper_aud_arr, self.temp_start_bumper_aud_arr)
        random.shuffle(self.temp_start_bumper_aud_arr)
        # Do the same for set ender barks
        self.copy_src_arr_to_temp(self.end_bumper_aud_arr, self.temp_end_bumper_aud_arr)
        random.shuffle(self.temp_end_bumper_aud_arr)

        # get the exercises for the continuous set:
        #  ------------ NOTE: modify with conditional for other continuous exercises?
        stretch_list = self.get_stretching_exercises()
        self.update_display_listing_stretches(stretch_list)
        

        num_of_stretches = len(stretch_list)
        each_stretch_duration = self.stretch_duration_slider.get()
        print(f"\t-- duration for each stretch: {each_stretch_duration}")
        total_stretch_time_in_seconds = (each_stretch_duration)*(num_of_stretches)
        total_stretch_set_time_in_mins = math.ceil((total_stretch_time_in_seconds)/60)
        print(f" [+] Total stretch time in mins: {total_stretch_set_time_in_mins}")
        self.stretch_time_length_label.config(text=f"Workout time total: {total_stretch_set_time_in_mins}m")
    
# ----------------------------------------------------------------------------------------------------------------------------------------------   
    
def main():
    root = tk.Tk()
    app = ExerciseTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
