// Global variable to track the timer interval (so we can stop it later)
let midHeaderGenerated = false
// Global state
const fruits = ["apple", "strawberry", "cherry", "coconut", "banana", "lime", "lemon"]
const red_things = ["apple", "cherry", "brick", "rust", "fire", "red paint", "red panda"]
// const forearmExercises = []
// const tricepExercises = []
// can be done with light weight effectively
const lightBicepExercises = [
    "wide curl", "drag curl", "alt. hammer curl", "basic hammer curl", "sing.arm support-curl", "paired-together hammer curl",
    "bicep to overhead press", "Z-curl", "forearm raise", "reverse curl, forward down", "crouch curls"]
const chestExercises = [
    "alligator push-ups", "alt. archer pushups", "push up to side plank", "push up alt. shoulder taps",
    "planche push up", "chest fly", "close-hand,  rev. palm push-up"
]
let legs = ["Squats", "Lunges","Calf Raises", "Deadlifts", "Leg Press",  "Step-Ups"]
let abs = ["Crunches", "Plank", "Russian Twists", "Leg Raises", "Bicycle Kicks", 
    "standing cross crunch", "cross toe-taps"]
let arms = ["Bicep Curls", "Triceps Dips", "Hammer Curls", 
    "Push-ups", "Over.Tri.Extensions", "Chin-ups"]

const exercisesDic = {
    "legs": ["Squats", "Lunges","Calf Raises", "Deadlifts", "Leg Press",  "Step-Ups"],
    "abs": ["Upper Ab Crunch", "Leg ext. crunch", "Side suitcase", "Single-side plank", 
        "Basic Plank", "Starfish Crunch", "Leg Raises", "Windshield Wiper", "Squat cross crunch", 
        "Knee Raises"],
    "arms": ["Bicep Curls", "Triceps Dips", "Hammer Curls", 
        "Push-ups", "Overhead Triceps Extensions", "Chin-ups"]
    // bicepsForearms: [],
    // tricepsForearms: [],
    // bicepsDelts: [],
    // tricepsDelts: [],
    // tricepsChest: [],
    // bicepsChest:[],
    // bicepsTriceps: [],
    // forearmDelts:[],
    // forearmChest:[],
    // deltsChest:[]
};

let light_exercises = ["tree-choppers", "side-bends", "leg-lifts", "starfish crunch", "elbow strike", "knee strike", "downward elbow", "3/4 sway", "roll and jab", 
    "side suitcase", "penguin side-bends", "neck rotations", "hula hip-rotations", "wrist rolls", "leg up, hip circles"]

let timerInterval;
let timerType = "Action" // Tracks which timer is active keywords: "Action", "LightMotion", "Rest"
let isPaused = false;
let currentSetsRemaining = 999;
let currentActionsRemaining = 999;
let currentTimeRemaining = 999;
let isFirstRound = true;
let isStartOfPhase = true; // flag for managing phase triggers with a simple bool

const pauseBtn = document.getElementById('pause-btn');
// pauseBtn.disabled = true; gibbon3
const actionDurationSlider = document.getElementById('action-duration-slider'); //slider1
const lightDurationSlider = document.getElementById('light-duration-slider'); //slider2
const actionsPerSetSlider = document.getElementById('actions-per-set-slider');
const setsPerWorkoutSlider = document.getElementById('sets-per-workout-slider');
const restDurationSlider = document.getElementById('rest-duration-slider');

// helper function to play random audio and track state to not repeat junk
function createAudioTracker(sourceAudios) {
    let unusedAudios = [...sourceAudios];
    let lastPlayedAudio = null;
    // Return a function that plays a random audio + updates state
    return function play() {
      // Reset pool if empty (all clips played once)
      if (unusedAudios.length === 0) {
        unusedAudios = [...sourceAudios];
        // Avoid repeating the last played audio
        if (lastPlayedAudio) {
          unusedAudios = unusedAudios.filter(audio => audio !== lastPlayedAudio);
        }
      }
      const randomIndex = Math.floor(Math.random() * unusedAudios.length);
      const selectedAudio = unusedAudios[randomIndex];
      // Update state
      unusedAudios.splice(randomIndex, 1);
      lastPlayedAudio = selectedAudio;
      // Play the audio
      selectedAudio.currentTime = 0;
      selectedAudio.play().catch(e => console.error("Playback failed:", e));
      return selectedAudio; // Optional: Return the played audio if needed
    };
  }
// dummy randomizer, dupes are allowed:
function playRandAudioSimple(arr){
    const randomIndex = Math.floor(Math.random() * arr.length);
    const selectedAudio = arr[randomIndex];
    selectedAudio.currentTime = 0; // Reset if already played
    selectedAudio.play();
  }  
// Audio elements (load these in HTML)
const workoutStartAudio1 = new Audio('./start_main_action/allPrimarySystemsOnline.wav');
const workoutStartAudio2 = new Audio('./start_set/vary_pda.wav');
const workoutStartAudio3 = new Audio('./start_main_action/cyclops_powerUp.wav');
const workoutStartAudio4 = new Audio('./start_set/cyclops_allSystemsOnline.mp3');
const workoutStartAudio5 = new Audio('./start_set/haradrim_horn.wav');
const workoutStartAudio6 = new Audio('./start_set/horn_of_gondolin.wav');
const workoutStartAudio7 = new Audio('./start_set/t_rex_roar.wav');
// const workoutStartAudio8 = new Audio('./start_set/tempered_steel.wav');
// const workoutStartAudio9 = new Audio('./start_set/trainHornSteam2.wav');
// const workoutStartAudio10 = new Audio('./start_set/valor.wav');
// const workoutStartAudio11 = new Audio('./start_set/adversity1.wav');
const allWorkoutStartAuds = [workoutStartAudio1, workoutStartAudio2, workoutStartAudio3, workoutStartAudio4, workoutStartAudio5, 
    workoutStartAudio6, workoutStartAudio7,  
    // workoutStartAudio8, workoutStartAudio9, workoutStartAudio10, workoutStartAudio11
]

const actionStartAudio1 = new Audio('./start_main_action/go1.wav');
const actionStartAudio2 = new Audio('./start_main_action/backInAction.wav');
const actionStartAudio3 = new Audio('./start_main_action/doYourBestBubblegum.wav');
const actionStartAudio4 = new Audio('./start_main_action/chiaki_lets_go.wav');
const actionStartAudio5 = new Audio('./start_main_action/fiora_this_how_we_do_it.wav');
const actionStartAudio6 = new Audio('./start_main_action/fireupBubblegum1.wav');
const actionStartAudio7 = new Audio('./start_main_action/lady_go_to_work_boys.wav');
const actionStartAudio8 = new Audio('./start_main_action/letsGetMovingBubblegum1.wav');
const actionStartAudio9 = new Audio('./start_main_action/showOnRoadBubblegum.wav');
const actionStartAudio10 = new Audio('./start_main_action/Phyrra_have_to_try_harder.wav');
let allActionStartAuds = [actionStartAudio1, actionStartAudio2, actionStartAudio3, actionStartAudio4, actionStartAudio5, actionStartAudio6, actionStartAudio7, actionStartAudio8, actionStartAudio9, actionStartAudio10]
let unusedActionAudios = [...allActionStartAuds]; // Clone to track remaining audios

// function playRandomActionAudio() {
//     if (unusedAudios.length === 0) {
//       // Reset pool if all audios have been played
//       unusedAudios = [...allActionStartAuds];
//       // Filter out the last played audio to prevent repeats
//       unusedAudios = unusedAudios.filter(audio => audio !== lastPlayedActionAudio);
//     }
//     // Randomly select from remaining audios
//     const randomIndex = Math.floor(Math.random() * unusedAudios.length);
//     const selectedAudio = unusedAudios[randomIndex];
//     // Update tracking
//     unusedAudios.splice(randomIndex, 1); // Remove from pool
//     lastPlayedActionAudio = selectedAudio;     // Remember last played
//     // Play the audio
//     selectedAudio.currentTime = 0; // Reset if already played
//     selectedAudio.play();
//   }

  
const playActionAudio = createAudioTracker(allActionStartAuds);

const lightStartAudio = new Audio('./start_light/mori_switch_to_low_intensity.wav');
const restStartAudio = new Audio('./start_rest/Schnee_and_done.wav');
const audioHalfway = new Audio('./special/pdaBeepBeep.wav');
const audioFiveSecAction = new Audio('./countdowns/cyclops5sCountdown.wav');
const audioFiveSecLight = new Audio('./countdowns/5sCountdownGF.mp3');
const audioFiveSecRest = new Audio('./countdowns/zh5s_reporter.wav');
const pauseStart = new Audio('./punctuation/kh_money_get.wav');
const pauseEnd = new Audio('./punctuation/kh_replenish_item.wav');
//  End of light could be encouragement for new action?
const lightOverPunctuation = new Audio('./punctuation/blake_rifle_gunshot_fire.wav');
// end of Main Action could be switch to low intensity?
const actionOverPunctuation = new Audio('./punctuation/rwby_sniper_rifle3.wav');
const breakOverPunctionation = new Audio('./punctuation/lvlup.wav');

const timeForBreak = new Audio('./start_rest/Schnee_and_done.wav');

all_auds_arr = [audioFiveSecAction, audioFiveSecLight, audioFiveSecRest]

function stopAllSounds() {
    all_auds_arr.forEach(audio => {
      audio.pause();         // Stop playback
      audio.currentTime = 0; // Reset to start
    });
  }
// update with master array index? gibbon2
function manageHeaderText(){
    const headerText = document.getElementById("header-text");
    const remainingActionsTextarea = document.getElementById("actions-left");
    const roundsRemaining = document.getElementById("rounds-left");
    //  NYI name of exercise display
    headerText.textContent = "content changed";
    remainingActionsTextarea.textContent = `${String(currentActionsRemaining)}`;
    roundsRemaining.innerHTML = `${String(currentSetsRemaining)}`
}
function playTwoConsecutiveAudios(firstAudio, secondAudio){
    firstAudio.play();  
    firstAudio.addEventListener('ended', () => {  
    console.log(`${firstAudio} finished. Playing ${secondAudio}...`);  
    secondAudio.play();  
    });  
}

function getRandomUniqueItem(targetArr, excludedItems) {
    const available = targetArr.filter(item => !excludedItems.includes(item));
    // in the case of
    if (available.length === 0) {
        alert("no new items, choosing randomly")
        available[Math.floor(Math.random() * targetArr.length)];
    }
    return available[Math.floor(Math.random() * available.length)];
}

function attachWorkoutButtonHandlers(container, srcArr, myCurrentArray) {
    const wrappers = container.querySelectorAll('.workout-item-wrapper');

    wrappers.forEach((wrapper, index) => {
        const btnA = wrapper.querySelector('.btn-a');
        const btnB = wrapper.querySelector('.btn-b');
        const contentSpan = wrapper.querySelector('.workout-item-content');    
        // Safety check
        if (!btnA || !btnB || !contentSpan) return;

        btnA.addEventListener('click', () => {
            const newItem = getRandomUniqueItem(srcArr, myCurrentArray);
            myCurrentArray[index] = newItem;
            contentSpan.textContent = newItem;
        });

        btnB.addEventListener('click', () => {            
            let clickedExerciseText = contentSpan.textContent
            let currExerciseArr = localStorage.getItem('selectedExerciseArray')
            console.log(`${currExerciseArr}`);
            showExerciseSelector(currExerciseArr, clickedExerciseText);
        });
    });
}

// Render function to create each workout item block
// srcArr here refers to the dictionary entry
    // we can get the current active array from local storage
function renderWorkoutItem(arr_item, columnClass) {
    const wrapper = document.createElement('div');
    wrapper.className = `workout-item-wrapper ${columnClass}`;
    wrapper.innerHTML = `
        <button class="btn-a">A</button>
        <span class="workout-item-content">${arr_item}</span>
        <button class="btn-b">B</button>
    `;
    return wrapper;
}
function handleMidHeaderGeneration(){
    const topDisplayElement = document.getElementById('top-display');
    let mid_header = `
    <div id ="mid-header" class="middle-header">
      <div class="dropdown-wrapper">
        <label for="action1-select">Action 1:</label>
        <select id="action1-select">
          <option>Legs</option>
          <option>Arms</option>
          <option>Abs</option>
        </select>
      </div>
      <div class="dropdown-wrapper">
        <label for="action2-select">Action 2:</label>
        <select id="action2-select">
          <option>None</option>
          <option>Legs</option>
          <option>Arms</option>
          <option>Abs</option>
        </select>
      </div>
      <div class="dropdown-wrapper">
        <label for="placeholder1-select">Placeholder 1:</label>
        <select id="placeholder1-select">
          <option>foo</option>
          <option>bar</option>
          <option>baz</option>
        </select>
      </div>
      <div class="dropdown-wrapper">
        <label for="placeholder2-select">Placeholder 2:</label>
        <select id="placeholder2-select">
          <option>foo</option>
          <option>bar</option>
          <option>baz</option>
        </select>
      </div>
    </div>
    `

    // Insert the HTML after the the top display
    topDisplayElement.insertAdjacentHTML('afterend', mid_header);
    midHeaderGenerated = true

//  diagnostic strings ------------------------------------------------------------------------------------------------------------------------------------
    
    const sets = parseInt(document.getElementById('sets-per-workout-slider').value);
    const num_actions = parseInt(document.getElementById('actions-per-set-slider').value)
    console.log(`sets: ${sets}/ main actions: ${num_actions} / light actions ${num_actions - 1}`);
}
function renderWorkroutItemSelect(in_arr, num_actions) {
    item_content = ""
    for (let i = 0; i < num_actions; i++) {
        const arr_item = in_arr[i];
        const columnClass = i % 2 === 0 ? "left-column" : "right-column";
        let workoutItemHTMLObj = renderWorkoutItem(arr_item, columnClass)
        item_content += workoutItemHTMLObj.outerHTML;
    }
    return item_content
}

function buildDisplayFromArr(in_arr) {
    let num_actions = localStorage.getItem("mainActionsNumStored")

    if (!midHeaderGenerated) {
        handleMidHeaderGeneration();
    }
    
    let content = "";
    
    let item_display_html = renderWorkroutItemSelect(in_arr, num_actions)
    content += item_display_html;
  content += `
    <div class="mid-footer-item left-column">
      <button id="back-to-sliders-btn" onclick="refreshPlaceholder()">Back to sliders</button>
    </div>
    <div class="mid-footer-item right-column">
      <button id="start-workout-btn" onclick="startTimer()">start</button>
    </div>
  `;
  return content;
}

function getRandomItems(array, num) {
    // Create a copy of the array and shuffle it
    const shuffled = [...array].sort(() => 0.5 - Math.random());
    const result = [];
    let index = 0;

    // Loop until we've collected the required number of items
    for (let i = 0; i < num; i++) {
        // If we've exhausted the shuffled array, shuffle it again
        if (index >= shuffled.length) {
            index = 0;
            shuffled.sort(() => 0.5 - Math.random());
        }
        result.push(shuffled[index]);
        index++;
    }
    return result;
}

// Function to attach the event listener to the "Select Exercises" button
function attachInitialButtonHandler() {
  const selectBtn = document.getElementById("exercise-select-btn");
  if (selectBtn) {
    selectBtn.addEventListener("click", function () {
        // set all the slider values to local storage
        const nMainActions = parseInt(document.getElementById('actions-per-set-slider').value);
        const actionDuration = parseInt(document.getElementById('action-duration-slider').value);
        const lightDuration = parseInt(document.getElementById('light-duration-slider').value);
        const nSets = parseInt(document.getElementById('sets-per-workout-slider').value);
        let nRests = nSets - 1
        const restDuration = parseInt(document.getElementById('rest-duration-slider').value);
        localStorage.setItem('mainActionsNumStored', JSON.stringify(nMainActions));
        // deactivated unused light-action tracking... causing confusion to the developer to have extraneous stuff
        // let nLightActions = nMainActions - 1
        // localStorage.setItem('lightActionsNumStored', JSON.stringify(nLightActions));
        localStorage.setItem('actionDurationStored', JSON.stringify(actionDuration));
        localStorage.setItem('lightDurationStored', JSON.stringify(lightDuration));
        localStorage.setItem('setNumStored', JSON.stringify(nSets));
        localStorage.setItem('restNumStored', JSON.stringify(nRests));
        localStorage.setItem('restDurationStored', JSON.stringify(restDuration));

        const randomItemsFirstGen = getRandomItems(exercisesDic["legs"], nMainActions);
        localStorage.setItem('selectedExerciseArray', JSON.stringify(randomItemsFirstGen));
        const middleDisplay = document.getElementById("middle-display");
        middleDisplay.innerHTML = buildDisplayFromArr(randomItemsFirstGen); 
        attachWorkoutButtonHandlers(middleDisplay, exercisesDic["legs"], randomItemsFirstGen);
        handleActionDropdowns();
    //   attachWorkoutButtonHandlers(container, srcArr, myCurrentArray)
      // quail
    });
  } 
}

function handleActionDropdowns() {
    const action1Select = document.getElementById("action1-select");
    const action2Select = document.getElementById("action2-select");

    function handleAction1Change() {
        const selected1 = action1Select.value.toLowerCase();
        const num = parseInt(localStorage.getItem("mainActionsNumStored")) || 0;
        // console.log(`selection 1 name ${selected1}`)
        // console.log(`selection 1 arr ${exercisesDic[selected1]}`)
        if (exercisesDic[selected1]) {
            const randomItems = getRandomItems(exercisesDic[selected1], num);
            // console.log("Action 1 Random Items:", randomItems);
            localStorage.setItem('selectedExerciseArray', JSON.stringify(randomItems));
            const middleDisplay = document.getElementById("middle-display");
            middleDisplay.innerHTML = buildDisplayFromArr(randomItems); 
            attachWorkoutButtonHandlers(middleDisplay, exercisesDic[selected1], randomItems);
        }
        updateDropdownOptions(action1Select, action2Select);
    }

    function handleAction2Change() {
        const selected1 = action1Select.value.toLowerCase();
        const selected2 = action2Select.value.toLowerCase();
        const num = parseInt(localStorage.getItem("mainActionsNumStored")) || 0;
        if (selected2 === "None" || !exercisesDic[selected1] || !exercisesDic[selected2]) return;
        const action1Items = getRandomItems(exercisesDic[selected1], num);
        const action2Items = getRandomItems(exercisesDic[selected2], num);

        const mixedItems = [];
        for (let i = 0; i < num; i++) {
            mixedItems.push(i % 2 === 0 ? action1Items[i % action1Items.length] : action2Items[i % action2Items.length]);
        }
        console.log("Mixed Action 2 Items:", mixedItems);
        const middleDisplay = document.getElementById("middle-display");
        middleDisplay.innerHTML = buildDisplayFromArr(mixedItems);
        attachWorkoutButtonHandlers(middleDisplay, exercisesDic[selected1], mixedItems);
        localStorage.setItem('selectedExerciseArray', JSON.stringify(mixedItems));
    }

    // After selection an option, disable it in the other dropdown
    function updateDropdownOptions(sourceSelect, targetSelect) {
        const selectedValue = sourceSelect.value;
        Array.from(targetSelect.options).forEach(option => {
            option.disabled = option.value === selectedValue;
        });
    }
    // Add event listeners to the dropdowns
    action1Select.addEventListener("change", () => {
        handleAction1Change();
        handleAction2Change(); // re-check action 2 if needed, safety code call
    });
    action2Select.addEventListener("change", () =>{
        handleAction2Change();
    });
    handleAction1Change();
    handleAction2Change();
}

function refreshPlaceholder() {
    location.reload()
};

function showExerciseSelector(selectedExerciseArr, clickedExerciseMove) {
    if (document.getElementById('exercise-popup')) return;

    const popup = document.createElement('div');
    popup.classList.add('ad-hoc-selector-window');

    const muscleSelect = document.createElement('select');
    muscleSelect.classList.add('muscle-select');

    for (const group in exercisesDic) {
        const option = document.createElement('option');
        option.value = group;
        option.textContent = group.charAt(0).toUpperCase() + group.slice(1);
        muscleSelect.appendChild(option);
    }

    const exerciseSelect = document.createElement('select');
    exerciseSelect.classList.add("exercise-select");

    const updateExerciseList = () => {
        const selectedGroup = muscleSelect.value;
        const exercises = [...exercisesDic[selectedGroup]].sort();

        exerciseSelect.innerHTML = '';

        // Add a placeholder option
        const placeholder = document.createElement('option');
        placeholder.textContent = '— Select —';
        placeholder.disabled = true;
        placeholder.selected = true;
        exerciseSelect.appendChild(placeholder);

        exercises.forEach(ex => {
            const option = document.createElement('option');
            option.value = ex;
            option.textContent = ex;
            exerciseSelect.appendChild(option);
        });
    };

    updateExerciseList();
    muscleSelect.addEventListener('change', updateExerciseList);

    exerciseSelect.addEventListener('change', () => {
        const newExercise = exerciseSelect.value;

        // Get from localStorage (clean read)
        let storedArr = JSON.parse(localStorage.getItem('selectedExerciseArray') || '[]');

        // Find the clicked item and replace
        const index = storedArr.indexOf(clickedExerciseMove);
        if (index !== -1) {
            storedArr[index] = newExercise;
            localStorage.setItem('selectedExerciseArray', JSON.stringify(storedArr));
            console.log('Updated array:', storedArr);  // ✅ shows new array with target item replaced
            const middleDisplay = document.getElementById("middle-display");
            middleDisplay.innerHTML = buildDisplayFromArr(storedArr);
            attachWorkoutButtonHandlers(middleDisplay, exercisesDic["legs"], storedArr);
        } else {
            console.warn(`"${clickedExerciseMove}" not found in localStorage array.`);
        }

        document.body.removeChild(popup);
    });

    const closeButton = document.createElement('button');
    closeButton.classList.add("ad-hoc-close-btn");
    closeButton.textContent = 'Close';
    closeButton.addEventListener('click', () => {
        console.log('manual exit');
        document.body.removeChild(popup);
    });
    const randButton = document.createElement('button');
    randButton.classList.add("ad-hoc-rand-btn");
    randButton.textContent = 'random';
    randButton.addEventListener('click', () => {
        console.log('placeholder to randomize');
    });

    popup.appendChild(muscleSelect);
    popup.appendChild(exerciseSelect);
    popup.appendChild(randButton);
    popup.appendChild(closeButton);
    document.body.appendChild(popup);
}



// Start the app once DOM is loaded
window.addEventListener("DOMContentLoaded", function () { 
    attachInitialButtonHandler();
    // Get all slider values to calculate time
    const nMainActions = parseInt(document.getElementById('actions-per-set-slider').value);
    let nLightActions = nMainActions - 1
    const actionDuration = parseInt(document.getElementById('action-duration-slider').value);
    const lightDuration = parseInt(document.getElementById('light-duration-slider').value);
    const nSets = parseInt(document.getElementById('sets-per-workout-slider').value);
    let nRests = nSets - 1
    const restDuration = parseInt(document.getElementById('rest-duration-slider').value);
    // Update infoLine1: "[n1] actions at [actionDuration]s = [total]"
    const mainActionTotal = nMainActions * actionDuration;
    const lightActionTotal = nLightActions * lightDuration;
// update header with total info
    document.getElementById('header-text').innerHTML = `<span id=time-preview> Total:${formatSeconds((mainActionTotal + lightActionTotal) * nSets + (nRests*restDuration))}<span>`;
    document.getElementById('total-time-footer').textContent = `Total:${formatSeconds((mainActionTotal + lightActionTotal) * nSets + (nRests*restDuration))}`
});

// Reusable function to format seconds as "MMmSSs"
function formatSeconds(totalSeconds) {
    const minutes = Math.floor(totalSeconds / 60).toString().padStart(2, '0');
    const seconds = (totalSeconds % 60).toString().padStart(2, '0');
    return `${minutes}m${seconds}s`;
}

// Get all sliders and their associated value displays
const sliders = document.querySelectorAll('.slider');
const valueDisplays = document.querySelectorAll('.slider-value');
// Initialize all displays
sliders.forEach(slider => {
const display = document.querySelector(`[data-for="${slider.id}"]`);
display.textContent = slider.value;
});

// Update header with preview of time total, dynamic calculations
document.addEventListener('input', (e) => {
if (e.target.classList.contains('slider')) {
    const slider = e.target;
    const sliderValue = parseInt(slider.value);
    // Update the slider's display (existing logic)
    const display = document.querySelector(`[data-for="${slider.id}"]`);
    if (display) display.textContent = sliderValue;
    // Get all slider values
    const nMainActions = parseInt(document.getElementById('actions-per-set-slider').value);
    let nLightActions = nMainActions - 1
    const actionDuration = parseInt(document.getElementById('action-duration-slider').value);
    const lightDuration = parseInt(document.getElementById('light-duration-slider').value);
    const nSets = parseInt(document.getElementById('sets-per-workout-slider').value);
    let nRests = nSets - 1
    const restDuration = parseInt(document.getElementById('rest-duration-slider').value);
    // Update infoLine1: "[n1] actions at [actionDuration]s = [total]"
    const mainActionTotal = nMainActions * actionDuration;
    const lightActionTotal = nLightActions * lightDuration;
// update header with total info
    document.getElementById('header-text').innerHTML = `<span id=time-preview> Total:${formatSeconds((mainActionTotal + lightActionTotal) * nSets + (nRests*restDuration))}<span>`;
    document.getElementById('total-time-footer').textContent = `Total:${formatSeconds((mainActionTotal + lightActionTotal) * nSets + (nRests*restDuration))}`
}
});
















function resetHeaderStyles(){
    const topDisplayArea = document.getElementById('top-display');
    topDisplayArea.classList.remove('intense-phase');
    topDisplayArea.classList.remove('rest-phase');
    topDisplayArea.classList.remove('light-phase');
    topDisplayArea.classList.add("active-phase")
}




// Start/resume the active timer
function startTimer() {
    pauseBtn.disabled = false;
    pauseBtn.enabled = true;
    
    resetHeaderStyles();
    const clockDisplay = document.querySelector('.digital-clock');
    const nActions = localStorage.getItem('mainActionsNumStored');
    const mainActionDuration = localStorage.getItem('actionDurationStored');
    const lightMotionDuration = localStorage.getItem('lightDurationStored');
    const setsPerWorkout = localStorage.getItem('setNumStored');
    const restDuration = localStorage.getItem('restDurationStored');

    // make temp copies to count down from
    currentSetsRemaining = setsPerWorkout;
    currentActionsRemaining = nActions;
    currentTimeRemaining =  mainActionDuration; // always start with a main action, so fulfill the timer;
    
    // clear the timer interval if there is one
    clearInterval(timerInterval)

    // Update display immediately, adding the active-phase styling ---- 
    const topDisplayArea = document.getElementById('top-display');
    topDisplayArea.classList.add('active-phase');
    updateClockDisplay(clockDisplay, currentTimeRemaining);
    // ---- first time around the loop, 
        // Trigger the workout start audio here
    playRandAudioSimple(allWorkoutStartAuds);
    // update the header info for the first time;
    manageHeaderText();   
    /// ----------------------------------------------------------------------
    //  Manage interval logic
    /// ----------------------------------------------------------------------
    timerInterval = setInterval(() => {
        if (!isPaused) {
            currentTimeRemaining --;
// Manage audio alerts
            // manage action-phase behavior for timer
            if (timerType === "Action") {
                // if it's the start of the countdown
                if (isStartOfPhase) {
// NYI -- Play action name audio...
                    //  if we're at the last action of a set of actions...
                    if (currentActionsRemaining == 1) {
                        topDisplayArea.classList.remove('light-phase');    
                        topDisplayArea.classList.add('intense-phase');
                        console.log("Begin last action session detected")
// NYI ---- special audio array for last one in the set? 
                        //  placeholder to play normal action audio on last set...
                        playActionAudio();
                        isStartOfPhase = false;
                    } else if (currentActionsRemaining == nActions) {
                        try {
                            topDisplayArea.classList.remove('rest-phase');
                        } catch (error) {
                            console.log("can't remove rest phase; maybe you're at the start of the program?")
                        }
                        topDisplayArea.classList.add('active-phase');
                        console.log("Begin first action detected")
                        // This skips the workout-start bark on the very first round (avoids overlapping sounds triggers with action start + workout start)
                        // plays all actions, otherwise, e.g. on a normal action start after starting the program
                        if (!isFirstRound) {
                            playActionAudio();
                        }
                        isStartOfPhase = false;
                    } else {
                        topDisplayArea.classList.remove('light-phase');
                        topDisplayArea.classList.add('active-phase');
                        console.log("Begin middle action detected");
                        playActionAudio();
                    }
                }
                if (currentTimeRemaining === Math.ceil(mainActionDuration / 2)){
                    // trigger for sound playing halfway through a workout
                    audioHalfway.play();
                }
                if (currentTimeRemaining === 5) {
                    // trigger for last 5 seconds to play
                    audioFiveSecAction.play();    
                }   
                if (currentTimeRemaining === 0) { 
                    // NYI - at the very end of a timer, a punchline could be triggered here?
                    console.log("action timer reaching zero detected, maybe?")   
                } 
        // manage what happens in the lightMotion (short rest) phase of the timer
            } else if (timerType === "LightMotion") {
                // need to add one because of the auto-decrement happening before this is triggered; checks that we're at the start of a light motion
                if (isStartOfPhase) {
                    console.log("Begin light motion detected")
                    topDisplayArea.classList.remove('active-phase');
                    topDisplayArea.classList.add('light-phase');
                    isStartOfPhase = false;
                    // NYI audio for starting light action phase? Like generic sound saying "break?" or a sound effect?;
                }
                if (currentTimeRemaining === Math.ceil(lightMotionDuration / 2)) { 
                    audioHalfway.play();
                } 
                if (currentTimeRemaining === 5) {
                    audioFiveSecLight.play(); 
                }    
            //  Manage long-rest behavior
            } else if (timerType === "Rest") {
                if (isStartOfPhase) {
                    console.log("Begin rest-phase detected")
                    topDisplayArea.classList.remove('intense-phase');    
                    topDisplayArea.classList.add('rest-phase');
                    isStartOfPhase = false; // flip the switch to false
                }
                if (currentTimeRemaining === Math.ceil(restDuration / 2)) { 
                    audioHalfway.play();
                } 
                if (currentTimeRemaining === 5) {
                    audioFiveSecRest.play(); 
                }    
            }
// Switch timers displays when whatever current time reaches 0 (applies to all timer types)
            if (currentTimeRemaining <= 0) {
                isStartOfPhase = true // flip the bool to true, allowing the start conditional of the next phase on the next loop to trigger
                clockDisplay.textContent = "00:00";
                console.log(`Timer ${timerType} finished! Switching to next...`);
// Reset the global integers for the timers to start a new timer-phase
// All these inputs are needed to track where we are in the workout track (thus needing the actions, sets, and associated times for each phase)
                ({currentTimeRemaining, currentActionsRemaining, currentSetsRemaining, timerType} = switchTimer(mainActionDuration, lightMotionDuration, restDuration, nActions));
                console.log(`switchTimer() called --> now, the timer is ${timerType} with a time of ${currentTimeRemaining}`);
                console.log(`${currentActionsRemaining} actions remain, ${currentSetsRemaining} sets remain`);
            } else {
                updateClockDisplay(clockDisplay, currentTimeRemaining); // update the clock display every second
            }
        }
    }, 1000);
}

function togglePause() {
    const pauseButton = document.getElementById('pause-btn');
    const headerLeft = document.querySelector('.header_left');
    const topDisplayArea = document.getElementById('top-display');
    isPaused = !isPaused;
    pauseButton.textContent = isPaused ? "Resume" : "Pause";

    // Toggle the "is-paused" class for styling
    if (isPaused) {
        // stop and reset all active audio
        stopAllSounds();
        pauseStart.play();
        headerLeft.classList.add('is-paused');
        topDisplayArea.classList.add('is-paused');
    } else {
        pauseEnd.play();
        headerLeft.classList.remove('is-paused');
        topDisplayArea.classList.remove('is-paused');
    }
}

// Switch between Timers once the countdown reaches zero
function switchTimer (mainActionDuration2, lightMotionDuration2, restDuration2, nActions2) {
    if (currentSetsRemaining != 0) {
        //  NYI change the header to show the correct phase here...
        const topDisplayArea = document.getElementById('top-display');
// Initiate light motion: --- If it's an Action type and there's more than one action remaining, switch to light motion
        if ((timerType == "Action") && (currentActionsRemaining > 1) ) {
            actionOverPunctuation.play()
            currentActionsRemaining --;
            // console.log("move to light-motion triggered")
            timerType = "LightMotion";
            currentTimeRemaining = lightMotionDuration2
            manageHeaderText();
            return {currentTimeRemaining:currentTimeRemaining, currentActionsRemaining: currentActionsRemaining, currentSetsRemaining:currentSetsRemaining, timerType:timerType};
            // NYI --------- Play audio when starting up light motion..........................................
            // Also NYI, change the  
            // ........................................
            // playTwoConsecutiveAudios
            // ........................................
    // initiate action phase ----------------------------------------------
        } else if (timerType == "LightMotion") { // don't need to track light motions, since they're derived from main actions
            lightOverPunctuation.play()
            timerType = "Action";
            topDisplayArea.classList.remove('light-phase');
            topDisplayArea.classList.add('active-phase');
            console.log("move to Main Action triggered")
            // reset timer to main action's timer
            currentTimeRemaining = mainActionDuration2;
            return {currentTimeRemaining:currentTimeRemaining, currentActionsRemaining: currentActionsRemaining, currentSetsRemaining:currentSetsRemaining, timerType:timerType};
        }
    // initiate rest --------------- If the timer type is action, and it's the last one, then that's the last of the set and move to rest / higher conditional makes sure there's at least one more set
        else if ((timerType == "Action") && (currentActionsRemaining == 1) && currentSetsRemaining != 1) {
            timeForBreak.play()
            timerType = "Rest";
            topDisplayArea.classList.remove('active-phase');
            topDisplayArea.classList.add('rest-phase');
            console.log("rest triggered")
            currentSetsRemaining --;
            currentActionsRemaining = nActions2;
            console.log(`remaining actions within the function is ${currentActionsRemaining}`)
            currentTimeRemaining = restDuration2;
            manageHeaderText();
            return {currentTimeRemaining:currentTimeRemaining, currentActionsRemaining: currentActionsRemaining, currentSetsRemaining:currentSetsRemaining, timerType:timerType};
        } else if (timerType == "Rest"){
            breakOverPunctionation.play()
// new action startup aud goes here gibbon5
            topDisplayArea.classList.remove('rest-phase');
            topDisplayArea.classList.add('active-phase');
            timerType = "Action";
            console.log("move to new action set after rest triggered")
            // reset timer to main action's timer
            currentTimeRemaining = mainActionDuration2;
            return {currentTimeRemaining:currentTimeRemaining, currentActionsRemaining: currentActionsRemaining, currentSetsRemaining:currentSetsRemaining, timerType:timerType};
        } else if ((timerType == "Action") && (currentActionsRemaining == 1) && (currentSetsRemaining == 1)) {
// NYI workout end audio goes here
            timeForBreak.play()
            console.log("all sets complete; timer done!");
            // stop the interval from ticking and infinately triggering
            clearInterval(timerInterval);
            return {currentTimeRemaining:0, currentActionsRemaining: 0, currentSetsRemaining:0, timerType:"Action"};
        }
    } else {
        console.log("odd conditional encountered, check code please... 0004");
        clearInterval(timerInterval); // safety clearing for removing interval in odd circumstance to avoid loops
        return {currentTimeRemaining:0, currentActionsRemaining: 0, currentSetsRemaining:0, timerType:"Action"};
    }
}  

// Formats seconds into "MM:SS" for target element
function updateClockDisplay(element, seconds) {
    const mins = Math.floor(seconds / 60).toString().padStart(2, '0');
    const secs = (seconds % 60).toString().padStart(2, '0');
    element.textContent = `${mins}:${secs}`;
}


// --------------- NYI -----------------------

//  example : output for numberOfSets = 3 should be `pattern1Array = 
// [“squats”, “lunges”, “calf raises”, “squats”, “lunges”, “calf raises”, “squats”, “lunges”, “calf raises”]`
function repeatEntireArray(exercises, sets) {
    return Array(sets).fill(exercises).flat();
}

//  Example output  for numberOfSets = 3 `pattern2Array = 
// [“squats”, “squats”, “squats”, “lunges”, “lunges”, “lunges”, “calf raises”, “calf raises”, “calf raises”]`
function repeatEachItem(exercises, sets) {
    return exercises.flatMap(exercise => Array(sets).fill(exercise));
}
