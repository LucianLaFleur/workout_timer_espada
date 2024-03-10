import tkinter as tk
from datetime import datetime
import random
import pygame
import math
import time
import threading
# https://www.setforset.com/blogs/news/bodyweight-leg-exercises-without-weights
# Initial version: set for arms workout x abs on rest intervals

class ExerciseTimerApp:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Exercise Timer")

        # Set the height and width of the window
        self.master.geometry("900x680")
        # Assign fixed width to column 1
        # self.master.grid_columnconfigure(1, minsize=235)

        #  initialize pygame so I can play music properly
        pygame.init()

        #  Audio collection (safe for sharing)
        # audio_hit_start/
        self.start_bumper_aud_arr = ["audio_hit_start/doYourBestBubblegum.wav", "audio_hit_start/fireupBubblegum1.wav", "audio_hit_start/kickoffBubblegum.wav", "audio_hit_start/letsGetMovingBubblegum1.wav",
       "audio_hit_start/letsGetMovingBubblegum1.wav", "audio_hit_start/showOnRoadBubblegum.wav", "audio_hit_start/time2grindBubblegum.wav"]
        self.temp_start_bumper_aud_arr = []
        # audio_active_songs/
        self.active_song_aud_arr = ["audio_active_songs/bass_fish.wav", "audio_active_songs/battleSuit.wav", "audio_active_songs/desert1.wav", "audio_active_songs/desertTrance2.wav",
        "audio_active_songs/expectationsShort.wav", "audio_active_songs/goinSteady_cut.wav", "audio_active_songs/heilo1.wav", "audio_active_songs/impositionOfUltimatim_short.wav",
        "audio_active_songs/mottai_nai.wav", "audio_active_songs/persist_against_all.wav", "audio_active_songs/sideAlleyShort.wav", "audio_active_songs/workshop1.wav"]
        self.temp_active_song_aud_arr = []
        # audio_hit_half/
        self.half_bumper_aud_arr = ["audio_hit_half/pdaBeepBeep.wav"]
        self.temp_half_bumper_aud_arr = []
        # audio_hit_end/
        self.end_bumper_aud_arr = ["audio_hit_end/catchBreathBubblefum.wav", "audio_hit_end/doneBubblegum2.wav", "audio_hit_end/dontOverexertBubblegum1.wav", "audio_hit_end/finished1bubblegum.wav",
        "audio_hit_end/niceWorkBubblegum1.wav", "audio_hit_end/pauseBubblegum1.wav", "audio_hit_end/slowAndSteady1.wav", "audio_hit_end/takeABreatherBubblegum.wav"]
        self.temp_end_bumper_aud_arr = []
        # audio_interval_songs/
        self.interval_song_aud_arr = ["audio_interval_songs/all_you_can_do_cut.wav", "audio_interval_songs/anhedonia_short.wav",
        "audio_interval_songs/beat4354rs.wav", "audio_interval_songs/knifeOverHeart1.wav", "audio_interval_songs/LoyalObligation_cut.wav",
        "audio_interval_songs/purple_aviators_cut.wav", "audio_interval_songs/technical_complications.wav","audio_interval_songs/VacuousCuriosity.wav", "audio_interval_songs/WhatCannotBeReclaimed.wav"]
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

        self.ticep_exercises = ["tricep dips", "dolphin push-up", "plank to seal-pose", "sphinx dive-bombers", "tricep get-ups","lying side push-up",
        "diamond pushup", "sphynx to plank crawler", "sphynx to pike-push crawler", "sphynx-pike-stand", "benched tricep push"]

        self.shoulder_exercises = ["pike position cross toe-touches", 
                                   "pike push-up", "plank shoulder taps",  "bear crawl",
        "lying lat pull-downs", "snow angel shoulders", "flying cobra", "reaching row", "tension lat pull-downs"
        # lay pull-down and push out is like a lateral row then extend arms at 90 degrees out
        # "kneeling lat pull-down push-out", "slow and low crawl", "supermans", "seal bows",
        ]

        self.master_exercise_name_audio_dic = {
            # Shoulders
        "flying cobra": "exercise_names/flyingCobraBubble.wav",  
        "bear crawl": 'exercise_names/bearCrawlBubble.wav', 
        "lying lat pull-downs": "exercise_names/lyingLatPullDownBubblegum.wav",
        "pike position cross toe-touches":"exercise_names/pikePositionCrossToeBubblegum.wav", 
        "pike push-up":"exercise_names/pikePushUpBubblegum.wav",
        "plank shoulder taps":"exercise_names/plankShoulderTapsbub.wav", 
        "reaching row" : "exercise_names/reachingRowBubble.wav", 
        "snow angel shoulders":"exercise_names/snowAngelShoulders1.wav",
        "tension lat pull-downs":"exercise_names/tensionLatPullDownBubblegum.wav",
        # abs
        "flutter kicks": "exercise_names/flutterkickBubblegum.wav", 
        "full extension cross-crunch":"exercise_names/fullextensioncrossCrunchBubblegum.wav",
        "half-bridge hip-thrusts" : "exercise_names/halfbridgeHipThrustsBubblegum.wav", 
        "heels to the heavens": "exercise_names/heels2HeavensBubblegum.wav",
        "leg lifts, candle pose": "exercise_names/legLiftCandleBubblegum.wav", 
        "oblique heel-taps":"exercise_names/obliqueHeelTaps.wav"
        }
        
        self.abs_exercises = ["flutter kicks", "full extension cross-crunch", "leg lifts, candle pose", "half-bridge hip-thrusts", "heels to the heavens",
            "oblique heel-taps"
            # "boat row", "alternating  hip crunch", "windshield-half to hip raise", "windshield wiper leg lifts",
            # "dancing downward dog", "kneeling torso twists", "seated russian twists", "hip raise, leg extension", "standing windmills", "standing bicycle", 
            # "standing single cross crunch", "power knee-strike", "slo-mo mountain climbers", "oblique leg lift", "leg extension side-suitcase"
            # opposite arm and leg out, then bring in
            # "bird dog crunch", 
            # pike position,single leg back kick extension to plank knee tuck, on same leg, alternating 
            # "axe handle obliques", "banana boat rocker", 
            # mirrored below:
            # "seated single axe handle", "figure-eight obliques"
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
        
        

        # Initialize widgets
        self.exercise_label = tk.Label(master, text="Exercise:")
        self.exercise_label.config(font=("times", 24), fg="lime", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.exercise_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.timer_label = tk.Label(master, text="Time Remaining:")
        self.timer_label.config(font=("courier", 22), fg="lime", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.timer_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.set_number_label = tk.Label(master, text="Set not started")
        self.set_number_label.config(font=("courier", 22), fg="cyan", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.set_number_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        # Labels for sliders  -----------------------------------------------------------------------
        self.num_sets_label = tk.Label(master, text="Sets per exercise")
        self.num_sets_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_sets_label.grid(row=3, column=0)

        self.num_motions_label = tk.Label(master, text="# Motions")
        self.num_motions_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_motions_label.grid(row=3, column=1)

        self.active_duration_label = tk.Label(master, text="work (s)")
        self.active_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.active_duration_label.grid(row=3, column=2)

        self.rest_duration_label = tk.Label(master, text="interval (s)")
        self.rest_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.rest_duration_label.grid(row=3, column=3)

        # nyi checkbox for muscle groups -----------------------------------------------------------------------
        # self.num_target_groups = tk.Label(master, text="num target muscle groups")
        # self.num_target_groups.config(font=("Times", 12), fg="#cc3", bg="#225") 
        # self.num_target_groups.grid(row=2, column=1)
        
        # Create Scale widgets -----------------------------------------------------------------------
        # Create Tkinter variables to store the values of the sliders
        
        self.num_sets_slider = tk.IntVar()
        self.num_sets_slider = tk.Scale(master, from_=1, to=8, orient=tk.HORIZONTAL, variable=self.num_sets_slider, command=self.update_workout_timing_preview_label)
        self.num_sets_slider.set(3)
        self.num_sets_slider.grid(row=4, column=0, padx=5)

        self.num_motions = tk.IntVar()
        self.num_motions = tk.Scale(master, from_=2, to=20, orient=tk.HORIZONTAL,variable=self.num_motions, command=self.update_workout_timing_preview_label)
        self.num_motions.set(3)
        self.num_motions.grid(row=4, column=1, padx=5)
        
        self.active_duration_slider = tk.IntVar()
        self.active_duration_slider = tk.Scale(master, from_=5, to=90, orient=tk.HORIZONTAL, resolution=5, variable=self.active_duration_slider, command=self.update_workout_timing_preview_label)
        self.active_duration_slider.set(10)
        self.active_duration_slider.grid(row=4, column=2, padx=5)

        self.interval_duration_slider = tk.IntVar()
        self.interval_duration_slider = tk.Scale(master, from_=3, to=120, orient=tk.HORIZONTAL, resolution=3, variable=self.interval_duration_slider, command=self.update_workout_timing_preview_label)
        self.interval_duration_slider.set(12)
        self.interval_duration_slider.grid(row=4, column=3, padx=5)
        
        self.workout_timing_data_label = tk.Label(master, text="awaiting input data proper...")
        self.workout_timing_data_label.grid(row=6, column=0, columnspan=4, padx=5)
        self.workout_timing_data_label.config(font=("courier", 18), fg="cyan", bg="black")

        self.start_button = tk.Button(master, text="Start Session", command=self.start_workout)
        self.start_button.grid(row=7, column=0, padx=5, pady=5)
        self.start_button.config(font=("impact", 14), fg="lime", bg="black")

        self.pause_button = tk.Button(master, text="Pause/Resume", command=self.toggle_timer)
        self.pause_button.grid(row=7, column=1, padx=5, pady=5)
        self.pause_button.config(font=("Times", 14), fg="yellow", bg="black")

        self.rand_snd_button = tk.Button(master, text="random sound", command=lambda: self.get_and_play_rand_aud_to_end(self.start_bumper_aud_arr, self.temp_start_bumper_aud_arr))
        self.rand_snd_button.grid(row=7, column=2, padx=5, pady=5)
        self.rand_snd_button.config(font=("impact", 14), fg="cyan", bg="black")

        # self.interrupt_snd_button = tk.Button(master, text="random sound", command=self.select_and_play_random_bg_aud(self.active_song_aud_arr, self.temp_active_song_aud_arr, 10))
        # self.interrupt_snd_button.grid(row=7, column=2, padx=5, pady=5)
        # self.interrupt_snd_button.config(font=("impact", 14), fg="cyan", bg="black")

        self.listbox_of_chosen_exercises = tk.Listbox(master)
        self.listbox_of_chosen_exercises.grid(row=8, column= 0, columnspan=2, padx=2, pady=5)
        self.listbox_of_chosen_exercises.config(font=("Times", 16), width="40", height="12", fg="orange", bg="black") 

        self.listbox_of_interval_activities = tk.Listbox(master)
        self.listbox_of_interval_activities.grid(row=8, column= 2, columnspan=2, padx=2, pady=5)
        self.listbox_of_interval_activities.config(font=("Times", 16), width="40", height="12", fg="lime", bg="black") 
       
        # self.complete_exercises_text = tk.Text(master, height=10, width=40)
        # self.complete_exercises_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

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
        self.countup_timer = 0
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
        print(f"all interval sub arrs: {self.selected_interval_actions}")

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
    
    def halfway_sound_audio_thread(self, duration):
        half_active_dur = math.floor(duration.get()/2)
        # starter_half_alarm = self.get_random_aud(self.half_bumper_aud_arr, self.temp_half_bumper_aud_arr)
        starter_half_alarm = "audio_hit_half/pdaBeepBeep.wav"
        halfway_alarm_thread = threading.Timer(half_active_dur, self.play_audio_until_end(starter_half_alarm))
        halfway_alarm_thread.start()
        
    def start_workout(self):
        # initialize basic stuff
        self.num_exercises = self.num_motions.get()
        self.num_sets_per_exercise = self.num_sets_slider.get()
        dur_active = self.active_duration_slider.get()
        dur_interval = self.interval_duration_slider.get()
        self.remaining_action_time = dur_active
        self.remaining_interval_time = dur_interval
        self.countup_timer = 0
        self.get_workout_motions(self.target_muscle_group_list)
        self.select_interval_activities_randomizer(self.interval_activity_list)
        self.set_number_label.config(text=f"Set 1 of {self.num_sets_per_exercise}")
        self.exercise_label.config(text=f"Action:\n {self.selected_exercises[0]}")
        # self.selected_exercises is now populated
        # self.run_starting_round_concurrently()
        timer_thread = threading.Thread(target=self.update_timer)
        timer_thread.start()
        self.make_aud_thread_for_duration(self.active_song_aud_arr, self.temp_active_song_aud_arr, (self.active_duration_slider.get())-1)
    
    def update_exercise_label(self):
        # from the selected exercises arr, get the current exercise via index
        current_exercise = self.selected_exercises[self.current_exercise_index]
        self.exercise_label.config(text=f"Action:\n {current_exercise}", fg="lime", bg="black")

    def update_interval_label(self):
        current_interval_motion = self.selected_interval_actions[self.current_exercise_index][self.current_round_index]
        self.exercise_label.config(text=f"Interval:\n {current_interval_motion}", fg="purple", bg="yellow")

    def update_timer(self):
        # top portion contains adjusting the timer while time remains for set
        if self.is_it_action_time:
            self.remaining_action_time -= 1
            self.timer_label.config(text="Time left: " + str(self.remaining_action_time), fg="lime", bg="black")
        else:
            self.remaining_interval_time -= 1
            self.timer_label.config(text="Time left: " + str(self.remaining_interval_time), fg="yellow", bg="black")
# ---------------------------------------------------------------------------------------------------------------- 
        # when Action timer hits zero 
        if (self.is_it_action_time) and (self.remaining_action_time == 0):
            #  End of active time, switch to Interval time
            self.update_interval_label()
            self.is_it_action_time = False
            # we don't want to initiate the audios if it's the end of the set, checks for end of routine in block later...
            if self.current_round_index != self.num_sets_per_exercise:
                current_interval_act = self.selected_interval_actions[self.current_exercise_index][self.current_round_index]
                current_interval_aud_file = self.master_exercise_name_audio_dic[current_interval_act]
                self.play_audio_until_end(current_interval_aud_file)
                # self.halfway_sound_audio_thread(self.interval_duration_slider)
                self.make_aud_thread_for_duration( self.interval_song_aud_arr,  self.temp_interval_song_aud_arr, (self.interval_duration_slider.get()))
        # when Interval timer hits zero 
        elif self.remaining_interval_time == 0:
            current_exercise = self.selected_exercises[self.current_exercise_index]
            input(current_exercise)
            print("--------")
            input(self.master_exercise_name_audio_dic[current_exercise])
            current_action_aud_file = self.master_exercise_name_audio_dic[current_exercise]
            self.play_audio_until_end(current_action_aud_file)
            self.make_aud_thread_for_duration(self.active_song_aud_arr, self.temp_active_song_aud_arr, (self.interval_duration_slider.get()))
            # End Interval, start active
            self.update_exercise_label()    
            # reset both timing counters here, 
            self.remaining_action_time = self.active_duration_slider.get()  # Reset exercise time-amount
            self.remaining_interval_time = self.interval_duration_slider.get()  # Reset interval time-amount
            self.is_it_action_time = True
            # "round" count only increases when the interval action is complete
            self.current_round_index += 1
            self.set_number_label.config(text=f"Set {self.current_round_index + 1} of {self.num_sets_per_exercise}")

        if self.current_round_index == self.num_sets_per_exercise:
            # reset round index to 0 so it'll be used as the ordinal for the interval sub-arr
            self.current_round_index = 0
            # increase exercise index to move to the next item in selected_exercises
            self.current_exercise_index += 1
            print(f"current round index is {self.current_round_index}")
            print(f"{self.remaining_interval_time}")
            print(f"Current exercise motion is {self.current_exercise_index +1} of {self.num_exercises}")
            if self.current_exercise_index >= self.num_exercises:
                print(f"exercise session complete! {self.current_exercise_index} rounds of {self.num_exercises} complete!")
                self.set_number_label.config(text=f"Workout Complete!")
                self.exercise_label.config(text=f"{self.duration_in_mins}mins exercise complete!", fg="lime", bg="black")
                self.timer_label.config(text=f"Done!")
                return  # End of exercise routine
            else:
                # Use a dictionary association to get the audio file for the current exercise in particular (same var. as in the display for the exercise)
               
                # reset number label to one at beginning of new exercise motion
                self.set_number_label.config(text=f"Set {self.current_round_index + 1} of {self.num_sets_per_exercise}")
                # Also call the update to the exercise label !!! yes, this is double-calling the exercise label on the last item of each iteration, FIX LATER: C-bug, optimization
                self.update_exercise_label()
                # NYI update this to be the interrupted one
                print(f"{self.num_exercises - self.current_exercise_index} exercise motions remain")
                print(self.selected_exercises[self.current_exercise_index:])
            print(f"current round index is {self.current_round_index}")
        if not self.pause:
            self.master.after(1000, self.update_timer)
        # on completing a full set of rounds interval, increase index by 1 to move to the next 
                # self.current_exercise_index += 1
        
    # Toggle timer countdown
    def toggle_timer(self):
        self.pause = not self.pause
        if not self.pause:
            self.update_timer()

def main():
    root = tk.Tk()
    app = ExerciseTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
