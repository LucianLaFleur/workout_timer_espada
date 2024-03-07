import tkinter as tk
from datetime import datetime
import random
import time
import math
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

        # List of exercises
        # biceb and general arms stuff
        self.arm_exercises = ["walking push-ups", "sumo-squat push-ups", "T-plank alternating push-ups",  
        "crunching bicep curl", "pike push-up", "plank-tuck walk-up", "kong-vault tuck", "alternating crab bridge reaches",
        "plank-tuck push-up", "planche push-up", "push-up pop-ups", "frog stand to ukemi", "Congo Combo (alt. macaco pikes)", 
        "reverse-palm push-up", "dive-bomber push-up", "lying reverse biceb curl", "Alternating Moscow T-planks", 
        "towel reverse biceb curl", "lying towel hammer curl",
        # mirrored below
        "lying side bicep suitcase", "single-arm crab-reach", "uppercut-cross", "side-chop cross", "palm to karate chop"]
        self.shoulder_exercises = ["pike position cross toe-touches", "pike push-up", "plank shoulder taps", "slow and low crawl", "bear crawl",
        "lying lat pull-downs", "snow angel shoulders", "flying cobra", "reaching row", "supermans", "seal bows"
        "kneeling lat pull-down push-out"
        # like a lateral row then extend arms at 90 degrees out
        ]
        self.ticep_exercises = ["tricep dips", "plank to seal-pose", "sphinx dive-bombers", "tricep get-ups","lying side push-up",
        "diamond pushup", "sphynx to plank crawler", "sphynx to pike-push crawler", "sphynx-pike-stand", "benched tricep push"]
        self.abs_exercises = ["flutter kicks", "candle pose leg lifts", "full extension cross-crunch", "half-bridge hip-thrusts", "heels to the heavens",
            "leg extension rowboat crunch", "oblique heel-taps", "aletrnating hip crunch", "dragon-flag ukemi", "windshield wiper leg lifts",
            "dancing downward dog", 
            # pike position,single leg back kick extension to plank knee tuck, on same leg, alternating 
            "axe handle obliques", "banana boat rocker (rev. supers)"
            # mirrored below:
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
        
        self.set_number_label = tk.Label(master, text="Set not started")
        self.set_number_label.config(font=("courier", 22), fg="cyan", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.set_number_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.timer_label = tk.Label(master, text="Time Remaining:")
        self.timer_label.config(font=("courier", 22), fg="lime", bg="black", bd=2, relief="solid", padx=5, pady=5) 
        self.timer_label.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        # Labels for sliders  -----------------------------------------------------------------------
        self.num_sets_label = tk.Label(master, text="Sets per exercise")
        self.num_sets_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_sets_label.grid(row=2, column=0)

        self.num_motions_label = tk.Label(master, text="# Motions")
        self.num_motions_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.num_motions_label.grid(row=2, column=1)

        self.active_duration_label = tk.Label(master, text="work (s)")
        self.active_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.active_duration_label.grid(row=2, column=2)

        self.rest_duration_label = tk.Label(master, text="interval (s)")
        self.rest_duration_label.config(font=("Times", 12), fg="#cc3", bg="#225") 
        self.rest_duration_label.grid(row=2, column=3)

        # nyi checkbox for muscle groups -----------------------------------------------------------------------
        # self.num_target_groups = tk.Label(master, text="num target muscle groups")
        # self.num_target_groups.config(font=("Times", 12), fg="#cc3", bg="#225") 
        # self.num_target_groups.grid(row=2, column=1)
        
        # Create Scale widgets -----------------------------------------------------------------------
        # Create Tkinter variables to store the values of the sliders
        
        self.num_sets_slider = tk.IntVar()
        self.num_sets_slider = tk.Scale(master, from_=1, to=5, orient=tk.HORIZONTAL, variable=self.num_sets_slider, command=self.update_workout_timing_preview_label)
        self.num_sets_slider.set(3)
        self.num_sets_slider.grid(row=3, column=0, padx=5)

        self.num_motions = tk.IntVar()
        self.num_motions = tk.Scale(master, from_=2, to=20, orient=tk.HORIZONTAL,variable=self.num_motions, command=self.update_workout_timing_preview_label)
        self.num_motions.set(3)
        self.num_motions.grid(row=3, column=1, padx=5)
        
        self.active_duration_slider = tk.IntVar()
        self.active_duration_slider = tk.Scale(master, from_=2, to=90, orient=tk.HORIZONTAL, resolution=2, variable=self.active_duration_slider, command=self.update_workout_timing_preview_label)
        self.active_duration_slider.set(4)
        self.active_duration_slider.grid(row=3, column=2, padx=5)

        self.rest_between_set_duration_slider = tk.IntVar()
        self.rest_between_set_duration_slider = tk.Scale(master, from_=5, to=120, orient=tk.HORIZONTAL, resolution=5, variable=self.rest_between_set_duration_slider, command=self.update_workout_timing_preview_label)
        self.rest_between_set_duration_slider.set(6)
        self.rest_between_set_duration_slider.grid(row=3, column=3, padx=5)
        
        self.workout_timing_data_label = tk.Label(master, text="awaiting input data proper...")
        self.workout_timing_data_label.grid(row=6, column=0, columnspan=4, padx=5)
        self.workout_timing_data_label.config(font=("courier", 18), fg="cyan", bg="black")

        self.start_button = tk.Button(master, text="Start Session", command=self.run_all_the_things)
        self.start_button.grid(row=7, column=0, padx=5, pady=5)
        self.start_button.config(font=("impact", 14), fg="lime", bg="black")

        self.pause_button = tk.Button(master, text="Pause/Resume", command=self.toggle_timer)
        self.pause_button.grid(row=7, column=1, padx=5, pady=5)
        self.pause_button.config(font=("Times", 14), fg="yellow", bg="black")

        self.rand_snd_button = tk.Button(master, text="random sound", command=self.toggle_timer)
        self.rand_snd_button.grid(row=7, column=2, padx=5, pady=5)
        self.rand_snd_button.config(font=("impact", 14), fg="cyan", bg="black")

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
        self.target_muscle_group_list = self.ticep_exercises
        self.interval_activity_keyword = "abs"
        self.interval_activity_list = self.abs_exercises
        self.workout_data_list = []

        self.countdown_done = False
        self.pause = True
        self.remaining_action_time = 0
        self.remaining_interval_time = 0
        self.countup_timer = 0
        self.is_it_action_time = True
        self.num_exercises = 0
        self.num_sets_per_exercise = 0
        self.current_exercise_index = 0
        self.current_round_index = 0

    def update_workout_timing_preview_label(self, value):
        #  STATIC VAL BELOW FOR EXERCISES
        num_exercises = self.num_motions.get()
        num_sets_per_exercise = self.num_sets_slider.get()
        dur_active = self.active_duration_slider.get()
        dur_interval = self.rest_between_set_duration_slider.get()
        break_interval = 0
        num_breaks = 0
        # duration_in_mins = math.ceil(((num_sets*(dur_active+dur_interval)) - dur_interval)+(break_interval * num_breaks)/60)
        duration_in_mins = math.ceil(((num_exercises*(num_sets_per_exercise*(dur_active+dur_interval)) - dur_interval)+(break_interval * num_breaks))/60)
        workout_stats_string = f"Total Duration: {duration_in_mins} minutes \n{num_sets_per_exercise} sets, {dur_active}s active, {dur_interval}s intervals"
        self.workout_timing_data_label.config(text=workout_stats_string)

    def select_actions_from_arr(self, num_actions, target_arr):
        # from target array, select a random number of unique items represented by the integer : num_actions
        selected_actions = random.sample(target_arr, num_actions)
        return selected_actions

    # Countdown for each exercise
    #  For one action, one interval, targeting a single muscle group

    def get_workout_motions(self, target_muscle_group):
        self.listbox_of_chosen_exercises.delete(0, tk.END)
        self.listbox_of_interval_activities.delete(0, tk.END)
        self.workout_data_list.append(f"workout targeting: {target_muscle_group}")
        # get the text from the data label
        workout_stats = self.workout_timing_data_label.cget("text")
        self.workout_data_list.append(workout_stats)
        # --------------- NYI : Logic for different kinds of sessions in different functions?-----------------------------------------------------------------------------------
        #  !!! NYI muscle group selection with a combobox (if combobox = arms, then self.arm_exercises...)
        target_action_list = self.arm_exercises
        # populate an array object with the main exercises
        self.selected_exercises = self.select_actions_from_arr(self.num_motions.get(), target_action_list)
        for x in self.selected_exercises:
            self.listbox_of_chosen_exercises.insert(tk.END, x)
        self.pause = False
        print(f"chosen exercises are: {self.selected_exercises}")

    def select_interval_activities_randomizer(self, interval_activity_source_list):
        # loop and bigger ar based on num of exercises
        big_interval_action_list = []
        for i in range(0, self.num_exercises):
            small_interval_actions_list = self.select_actions_from_arr(self.num_sets_per_exercise, interval_activity_source_list)
            big_interval_action_list.append(small_interval_actions_list)
        input(f" testing for list of sublists : {big_interval_action_list}")

    def run_all_the_things(self):
        # initialize basic stuff
        self.num_exercises = self.num_motions.get()
        self.num_sets_per_exercise = self.num_sets_slider.get()
        dur_active = self.active_duration_slider.get()
        dur_interval = self.rest_between_set_duration_slider.get()
        self.remaining_action_time = dur_active
        self.remaining_interval_time = dur_interval
        self.countup_timer = 0

        self.get_workout_motions(self.target_muscle_group_list)
        self.select_interval_activities_randomizer(self.interval_activity_list)
        self.set_number_label.config(text=f"Set 1 of {self.num_sets_per_exercise}")
        self.exercise_label.config(text=f"Action: {self.selected_exercises[0]}")

        # self.selected_exercises is now populated
        self.update_timer()
    
    # def update_exercise_label(self):
    #     current_exercise = self.exercises[self.current_exercise_index]
    #     print("1111112")
    #     self.exercise_label.config(text=f"Action: {current_work_motion}")
    # #     self.set_number_label.config(text=f"Set {motion_number} of {self.num_sets_slider.get()}")

    # def update_set_label(self):
    #     print("00003")

    def update_timer(self):
        if self.remaining_action_time > 0:
            self.remaining_action_time -= 1
            self.timer_label.config(text="Time left: " + str(self.remaining_action_time))
        elif self.remaining_interval_time > 0:
            self.remaining_interval_time -= 1
            self.timer_label.config(text="Time left: " + str(self.remaining_interval_time))
        else:
            # Move to the next set or exercise
        # self.current_exercise_index = 0
        # self.current_round_index = 0
            self.current_round_index += 1
            if self.current_round_index >= self.num_sets_per_exercise:
                self.current_round_index = 0
                self.current_exercise_index += 1
                if self.current_exercise_index >= self.num_exercises:
                    return  # End of exercise routine
            self.remaining_action_time = self.active_duration_slider.get()  # Reset exercise timer
            self.remaining_interval_time = self.rest_between_set_duration_slider.get()  # Reset interval timer
            self.update_labels()
        self.master.after(1000, self.update_timer)
    # Toggle timer countdown
    def toggle_timer(self):
        self.pause = not self.pause
        if not self.pause:
            # (use regex to get the amount of time remaining from the timer label to re-start)
            self.countdown(int(self.timer_label.cget("text").split(": ")[-1]))
    def print_workout_to_txt(self):
        # unformatted, lame time object
        raw_time = datetime.now()
        # Extracting datetime components...
        month = raw_time.strftime('%m')  
        day = raw_time.strftime('%d')   
        # year = raw_time.strftime('%Y')   
        hour = raw_time.strftime('%H') 
        minutes = raw_time.strftime('%M')  
        outfile_name = f"{self.target_muscle_group}_workout_on_{day}日{month}月_{hour}:{minutes}"
        with open(outfile_name, 'a', encoding='utf-8') as doc:
            for line in self.workout_data_list:
                doc.write(line)

def main():
    root = tk.Tk()
    app = ExerciseTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# DEAD CODE TO PROVE A POINT ABOUT ITERATIVE DEV ------------------------------
     
    # def do_workout_motion(self, motion_number):
    #     current_work_motion = self.selected_exercises[motion_number - 1]
    #     self.exercise_label.config(text=f"Action: {current_work_motion}")
    #     self.set_number_label.config(text=f"Set {motion_number} of {self.num_sets_slider.get()}")
    #     work_time = self.active_duration_slider.get()
    #     self.countdown_time(work_time)

    # def iter_test(self):
    #     work_time = self.active_duration_slider.get()
    #     sets_per_exercise = self.num_sets_slider.get()
    #     self.potato(self.counter_alpha)
    #     self.set_number_label.config(text=f"Set {self.counter_alpha} of {self.num_sets_slider.get()}")
    #     self.counter_alpha += 1
    #     if self.counter_alpha < sets_per_exercise:
    #         self.master.after((work_time * 1000), self.iter_test())

    # def potato(self, counter_var):
    #     self.get_workout_motions()
    #     self.get_interval_activities()
    #     work_time = self.active_duration_slider.get()
    #     current_work_motion = self.selected_exercises[counter_var - 1]
    #     self.exercise_label.config(text=f"Action: {current_work_motion}")
    #     self.set_number_label.config(text=f"Set {counter_var} of {self.num_sets_slider.get()}")
    #     self.countdown_time(work_time)
        
        # self.workout_data_list.append(main_motion)
        # input(f"move to {interval_activities_for_this_set[workout_set-1]}")

    # def countdown_time(self, remaining_time):
    #     if remaining_time < 0:
    #         print("time Up")
    #     else:
    #         self.timer_label.config(text=f"Time Remaining: {remaining_time}")
    #         if not self.pause:
    #             # Recursive self-call after 1 second
    #             self.current_timer = self.master.after(1000, self.countdown_time, remaining_time - 1)

# ------------------------------------------------------------------------------------

    # def countdown(self, remaining):
    #     if remaining <= 0:
    #         self.next_activity_in_sequence()
    #     else:
    #         self.timer_label.config(text="Time Remaining: {}".format(remaining))
    #         if not self.pause:
    #             # Recursive self-call after 1 second
    #             self.current_timer = self.master.after(1000, self.countdown, remaining - 1)
        
        #  def countup_time(self):
        # num_exercises = self.num_motions.get()
        # num_sets_per_exercise = self.num_sets_slider.get()
        # dur_active = self.active_duration_slider.get()
        # dur_interval = self.rest_between_set_duration_slider.get()
        # # if reduced to zero, the action or interval gets replenished, and boolean is switched
        
        #     #  terminating logic NYI -------------------------------------
        # if num_exercises < 0:
        #     input("num exercises remaining became sub-zero")
        # else:
        #     #  tick down action timer if action is active, otherwise, do it for the interval timer
        #     #  ALWAYS tick UP the countup_timer up-time counter
        #     if self.is_it_action_time:
        #         self.timer_label.config(text=f"Time Remaining: {self.remaining_action_time}")
        #         if not self.pause:
        #             self.countup_timer += 1
        #             self.remaining_action_time -= 1
        #             if self.remaining_interval_time == 0:
        #                 self.is_it_action_time = False
        #                 self.remaining_interval_time += dur_interval
        #             self.current_timer = self.master.after(1000, self.countup_time)
        #     else:
        #         # reduce interval time if not action
        #         self.timer_label.config(text=f"Time Remaining: {self.remaining_interval_time}")  
        #         if not self.pause:
        #             self.countup_timer += 1
        #             self.remaining_interval_time -= 1
        #             if self.remaining_interval_time == 0:
        #                 self.is_it_action_time = True
        #                 self.remaining_action_time += dur_active
        #             self.current_timer = self.master.after(1000, self.countup_time)

        # def update_labels(self):
        # # Update labels to display current exercise and interval activities
        # current_exercise = self.exercises[self.current_exercise_index]
        # current_interval_activities = self.all_interval_actions[
        #     self.current_exercise_index * self.num_sets_per_exercise + self.current_set_index
        # ]
        # self.current_exercise_label.config(text="Current Exercise: " + current_exercise)
        # self.current_interval_label.config(text="Interval Activities: " + current_interval_activities)

            # def select_exercises_1action_1rest(self, num_actions, action_arr, interval_activity_arr):
    #     output_exercise_arr = []
    #     output_interval_arr = []
    #     selected_work_actions = random.sample(action_arr, num_actions)
    #     selected_interval_activities = random.sample(interval_activity_arr, num_actions)
    #     for x in range(0, num_actions):
    #         output_exercise_arr.append(selected_work_actions[x])
    #         self.listbox_of_chosen_exercises.insert(tk.END, selected_work_actions[x])
    #         output_interval_arr.append(selected_interval_activities[x])
    #         self.listbox_of_chosen_exercises.insert(tk.END, selected_interval_activities[x])
        
        
    # add param for passing an activity list dynamically -------------------------------------
    # def get_interval_activities(self):
    #     # get the number of sets per exercise motion from the sets slider
    #     sets_per_exercise = self.num_sets_slider.get()
    #     # NYI static assume the abs set is the interval activity
    #     interval_activity_list = self.abs_exercises
    #     #  Get a number of activities sampled from the interval activity list indicated
    #     self.current_interval_actions = self.select_actions_from_arr(sets_per_exercise, interval_activity_list)
    #     for x in self.current_interval_actions:
    #         self.listbox_of_interval_activities.insert(tk.END, x)
        
    #  NYI add label-updates here with a counter for each one, so the countdown ticks a bunch of stuff together
    # def countup_time(self):
            #  terminating logic NYI -------------------------------------
        # add conditional for "if not complete", else, if not pause
        # if not self.pause:
        # if reduced to zero, the action or interval gets replenished, and boolean is switched
            # self.timer_label.config(text=f"Time Remaining: {self.remaining_action_time}")
            # self.current_timer = self.master.after(1000, self.countup_time)

        # else:
        #     #  tick down action timer if action is active, otherwise, do it for the interval timer
        #     #  ALWAYS tick UP the countup_timer up-time counter
        #     if self.is_it_action_time:

#  NYI ---- select different muscle groups: primary group, secondary group, rest action
#  nyi ---- muscle confusion function
    #  nyi ---- light-cardio item on rest

       # Sets until break
    # break duration 

    # NYI make the text interruptable so you can punch-out a text-file with a timestamp while paused or ended
