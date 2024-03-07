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
                            "plank-tuck push-up", "planche push-up"
                            "push-up pop-ups", "frog stand to ukemi",
                            "Congo Combo (alt. macaco pikes)", "reverse-palm push-up", "dive-bomber push-up",
                            "lying reverse biceb curl", "Alternating Moscow T-planks", "towel reverse biceb curl", "lying towel hammer curl",
                            # mirrored below
                            "lying side bicep crunch", "single-arm crab-reach", "uppercut-cross", "side-chop cross", "palm to karate chop"]
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
        self.exercise_label.config(font=("Arial", 14), fg="orange", bg="black", bd=2, relief="solid", padx=5, pady=5) 
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
        self.active_duration_slider.set(8)
        self.active_duration_slider.grid(row=3, column=2, padx=5)

        self.rest_between_set_duration_slider = tk.IntVar()
        self.rest_between_set_duration_slider = tk.Scale(master, from_=5, to=120, orient=tk.HORIZONTAL, resolution=5, variable=self.rest_between_set_duration_slider, command=self.update_workout_timing_preview_label)
        self.rest_between_set_duration_slider.set(6)
        self.rest_between_set_duration_slider.grid(row=3, column=3, padx=5)
        
        self.workout_timing_data_label = tk.Label(master, text="awaiting input data proper...")
        self.workout_timing_data_label.grid(row=6, column=0, columnspan=4, padx=5)
        self.workout_timing_data_label.config(font=("courier", 18), fg="cyan", bg="black")

        self.start_button = tk.Button(master, text="Start Session", command=self.start_workout_set)
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
        self.current_exercise = None
        self.current_timer = None
        self.completed_exercises_this_set = 0
        self.remaining_exercises_this_set = 0
        self.selected_exercises = []
        #  NYI static value below
        self.target_muscle_group = "shoulders"
        self.workout_data_list = []

        self.countdown_done = False
        self.pause = True

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
            
    #     return output_exercise_arr, output_interval_arr
    
    def select_actions_from_arr(self, num_actions, target_arr):
        # from target array, select a random number of unique items represented by the integer : num_actions
        selected_actions = random.sample(target_arr, num_actions)
        return selected_actions

    # Countdown for each exercise
    #  For one action, one interval, targeting a single muscle group
    def start_workout_set(self):
        self.workout_data_list.append(f"workout targeting: {self.target_muscle_group}")
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
        sets_per_exercise = self.num_sets_slider.get()
        
        interval_activity_list = self.abs_exercises
        #  select interval activities

    # def get_and_display_interval_activities(self):
    #     self.select_actions_from_arr()
    #     chosen_interval_activities = []
    #     for item in self.selected_exercises:
    #         for n in range(0, sets_per_exercise):
    #             chosen_interval_action = random.choice(interval_activity_list)
    #             chosen_interval_activities.append(chosen_interval_action)

        
    #     work_time = self.active_duration_slider.get()
    #     rest_time = self.rest_between_set_duration_slider.get()

    #     for main_motion in chosen_exercises:
    #         print(main_motion)
    #         interval_activities_for_this_set = self.select_actions_from_arr(sets_per_exercise, interval_activity_list)
    #         print(interval_activities_for_this_set)
    #         for x in interval_activities_for_this_set:
    #             self.listbox_of_interval_activities.insert(tk.END, x)
    #     # For each set of workouts formed from doing the action for the number of times indicated by the num-sets slider
    #         for workout_set in range(1, (sets_per_exercise+1)):
    #             self.exercise_label.config(text=f"Round {workout_set}/{sets_per_exercise} : {main_motion}")
    #             while True:
    #                 print("4rethg98q43w895h4twh45t")
    #                 self.timer_label.config(text=f"Time Remaining: {work_time}")
    #                 if not self.pause:
    #                     work_time -= 1
    #                     time.sleep(1)
    # # TRIGGER FOR END OF WORK TIME
    # # NYI trigger for half end of time... 
    #                 if work_time == 0:
    #                     self.timer_label.config(text=f"Time up!")
    #                     time.sleep(1)
    #                     work_time = self.active_duration_slider.get()
    #                     break
    #             self.workout_data_list.append(main_motion)
    #             input(f"move to {interval_activities_for_this_set[workout_set-1]}")
            # input(interval_activities_for_this_set)
            # completed_sets = 0
# ------------------------------------------------------------------------------------
# self.workout_data_list
            # listbox.delete(0, tk.END)
        

        # self.set_number_label.config(f"Set X of {sets_per_exercise}")

        # if num_completed_sets_for_this_exercise == sets_per_exercise:
        #     input("Ending set... NYI")
        # else:
        #     current_exercise = self.selected_exercises[0].pop(0)
        #     current_interval = self.selected_exercises[1].pop(0)
        #     # wrapper for repeated sets
        #     for muscle_set in range(0, sets_per_exercise):
        #         remaining_work_time = work_time
        #         self.exercise_label.config(text=f"Action! : {current_exercise}")
        #     # WORK countdown
        #         if not self.pause:
        #             remaining_work_time -= 1
        #             self.timer_label.config(text=f"Time Remaining: {remaining_work_time}")
        #             time.sleep(1)
        #             if remaining_work_time <0:
        #                 print("0023123 time ended")
        #     # INTERVAL countdown
        #         self.exercise_label.config(text=f"RoundInterval : {current_interval}")
        #         self.countdown(rest_time)

        # #    NYI for all items done 
        # # else:
        # #     self.exercise_label.config(text="Finished")
        # #     self.timer_label.config(text="Time up!")


    def countdown(self, remaining):
        if remaining <= 0:
            self.next_activity_in_sequence()
        else:
            self.timer_label.config(text="Time Remaining: {}".format(remaining))
            if not self.pause:
                # Recursive self-call after 1 second
                self.current_timer = self.master.after(1000, self.countdown, remaining - 1)

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

#  NYI ---- select different muscle groups: primary group, secondary group, rest action
#  nyi ---- muscle confusion function
    #  nyi ---- light-cardio item on rest

       # Sets until break
    # break duration 

    # NYI make the text interruptable so you can punch-out a text-file with a timestamp while paused or ended

#     Week 1: 10 reps x 3 sets (30 seconds rest)
# Week 2: 12 reps x 3 sets (30 seconds rest)
# Week 3: 15 reps x 3 sets (30 seconds rest)
# Week 4: 15 reps x 3 sets (20 seconds rest)
# Week 5: 15 reps x 3 sets (20 seconds rest) *couldn’t improve this week, it happens*
# Week 6: 15 reps x 4 sets (20 seconds rest)
