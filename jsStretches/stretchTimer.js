const audioHalfway = new Audio('./special/pdaBeepBeep.wav');
        const fiveSecCountdown = new Audio('./countdowns/5sCountdownGF.mp3');
        const startCue = new Audio('./start_main_action/go1.wav');
        const timerDisplay = document.getElementById("timer");
        const slider = document.getElementById("slider");
        const startButton = document.getElementById("startButton");
        const leftColumn = document.getElementById("left-column");
        const midLeftColumn = document.getElementById("mid-left-column");
        const midRightColumn = document.getElementById("mid-right-column");
        const rightColumn = document.getElementById("right-column");
        let countdown, taskIndex = 0, taskList = [];
        const totalStretchTime = 0
        let selectedExerciseArr = []

        const stretchList = [
            ["Left Quad Stretch", "Right Quad Stretch"],
            "leg circles",
            "bridge hip abduction",
            "ankle rotations", 
            "Butterfly Stretch",
            "hula-hoop hip rotations",
            "lateral hip abductions",
            ["left model's pose", "right model's pose"],
            ["left front split", "right front split"],
            "Center Splits",  
            ["left calf stretch", "right calf stretch"],
            ["Left Runner's Stretch", "Right Runner's Stretch"],
            "legs out stretch",
            "v-sit center",
            ["v-sit Left", "v-sit Right"],
            "Neck Rolls",
            ["Left tricep stretch", "Right tricep stretch"],
            ["Left arm-across stretch", "Right arm-across stretch"]
            ];

            // abs focus
        const arrayA = ["heels to heavens", "bicycle crunch", "side-suitcase", "squats", "lunge", "basic crunches", "side-bends",
            "windmills", "figure 8 axe", "golf axe-handle", "3/4's crunch", "3/4s boxing sway", "penguin side-bends",  "winddshield wiper", "legs-out full crunch",
            "starfish crunch", "standing cross-crunch", "goose-step toe-touches", "leg lifts", "reverse crunch", "bird-dog plank"
        ];
        // martial focus
        const arrayB = ["3/4s boxing sway", "1-2 punch", "rising uppercut", "superman punch", "elbow-knee", "uppercut-backhand", 
            "boxing roll to cross", "boxing roll to hook", "boxing rolls", 
            "gut-punch, downward elbow", "power backhand","curb stomp!", "front-side kick", "spinning side kick", "donkey kick",
            "back kick", "inward wheel kick", "outward wheel kick", "roundhouse kick", "flying knee strike"
        ];
        // shoulder/back focus
        const arrayC = ["shoulder circles", "flying cobra", "cobra reach","squats", "lunge", "RDL toe-touches",  "shoulder swimmers", "supermans", "standing cross crunch"];
        // leg array
        const arrayD = ["rising uppercut", "squats", "basic lunges", "stepback-switch lunges", "alt. plank-lunge get-ups"];
        // mix light array? to be added

        function formatTime(seconds) {
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            return String(mins).padStart(2, '0') + ":" + String(secs).padStart(2, '0');
        }

        // inputs an array, returns an integer for the number of items total, extrapolating on sub-array items to this overall count
        function countStringsInArray(arr) {
            let count = 0; 
            // Iterate over each item in the array
            arr.forEach(item => {
                if (Array.isArray(item)) {
                    // If the item is an array, add the length of the array to the count
                    count += item.length;
                } else if (typeof item === 'string') {
                    // If the item is a string, increment the count by 1
                    count += 1;
                }
            });
            return count; 
        }

        // Function to handle radio button change
        function handleRadioChange(event) {
            const selectedValue = event.target.value;
            if (selectedValue === 'A') {
                selectedExerciseArr = arrayA
                console.log(selectedExerciseArr);
            } else if (selectedValue === 'B') {
                selectedExerciseArr = arrayB
                console.log(selectedExerciseArr);
            } else if (selectedValue === 'C') {
                selectedExerciseArr = arrayC
                console.log(selectedExerciseArr);
            }
        }

        // Add event listeners to radio buttons
        document.querySelectorAll('input[name="options"]').forEach(radio => {
            radio.addEventListener('change', handleRadioChange);
        });

        function updateTimerDisplay(seconds) {
            timerDisplay.textContent = formatTime(seconds);
        }

        function shuffleArray(array) {
            return array.sort(() => Math.random() - 0.5);
        }

// hide the start button on click
        function hideButton() {
            document.getElementById('startButton').style.display = 'none';
        }
        // Add event listener to the hide start button
        document.getElementById('startButton').addEventListener('click', hideButton);

        function generateExerciseSequence() {
            let sequence = [];
            let shuffledStretches = shuffleArray([...stretchList]);
            let shuffledExercises = shuffleArray([...exerciseList]);
            let exerciseIndex = 0;
            for (let item of shuffledStretches) {
                if (exerciseIndex < shuffledExercises.length) {
                    sequence.push(shuffledExercises[exerciseIndex]);
                    exerciseIndex++;
                }
                if (Array.isArray(item)) {
                    let randomizedPair = shuffleArray([...item]);
                    sequence.push(...randomizedPair);
                } else {
                    sequence.push(item);
                }
            }

            return sequence;
        }
        function displayExercises() {
            taskList = generateExerciseSequence();
            leftColumn.innerHTML = "";
            midLeftColumn.innerHTML = "";
            midRightColumn.innerHTML = "";
            rightColumn.innerHTML = "";
        
            const quarterPoint = Math.ceil(taskList.length / 4);
            taskList.forEach((item, index) => {
                const div = document.createElement("div");
                div.textContent = item;
                div.classList.add(exerciseList.includes(item) ? "exercise" : "stretch");
                
                if (index < quarterPoint) {
                    leftColumn.appendChild(div);
                } else if (index < quarterPoint * 2) {
                    midLeftColumn.appendChild(div);
                } else if (index < quarterPoint * 3) {
                    midRightColumn.appendChild(div);
                } else {
                    rightColumn.appendChild(div);
                }
            });
        }

        function highlightCurrentTask() {
            document.querySelectorAll(".current-task").forEach(el => el.classList.remove("current-task"));
            if (taskIndex < taskList.length) {
                let allItems = [...leftColumn.children, ...midLeftColumn.children, ...midRightColumn.children, ...rightColumn.children];
                allItems[taskIndex].classList.add("current-task");
            }
        }

        function startSequence() {
            taskIndex = 0;
            let timeLeft = parseInt(slider.value);
            updateTimerDisplay(timeLeft);
            startButton.disabled = true;
            slider.disabled = true;
            highlightCurrentTask();
            startCue.play();
            
            countdown = setInterval(() => {
                timeLeft--;
                updateTimerDisplay(timeLeft);
                
                if (timeLeft <= 0) {
                    taskIndex++;
                    if (taskIndex < taskList.length) {
                        timeLeft = parseInt(slider.value);
                        highlightCurrentTask();
                        startCue.play();
                    } else {
                        clearInterval(countdown);
                        startButton.disabled = false;
                        slider.disabled = false;
                    }
                } else if (timeLeft == Math.ceil(parseInt(slider.value)/2)) {
                    audioHalfway.play();
                } else if (timeLeft == 5) {
                    fiveSecCountdown.play(); 
                }
            }, 1000);
        }

        slider.addEventListener("input", () => {
            updateTimerDisplay(slider.value);
        });

        startButton.addEventListener("click", () => {
            displayExercises();
            startSequence();
        });


        musicStyleArr = [
            "Jazz Fusion",
            "Cyber Blues",
            "trap house",
            "dubstep",
            "melodic dubstep",
            "chillstep disco fusion",
            "witch house electro fusion",
            "Techno Swing",
            "Disco",
            "Electro swing",
            "Motown",
            "J pop future funk",
            "J pop EDM",
            "J pop motown",
            "progressive house techno",
            "city pop",
            "Electro-Soul",
            "Futuristic Jazztronica",
            "retro game music funk",
            "retro game music techno",
            "Acid Blues",
            "synthwave, retro game music",
            "synthwave, bounce",
            "Synthwave R&B",
            "Progressive Funk"
        ]
        instrumentsArr = [
            "Electric Piano",
            "Synthesizers",
            "Electric guitar",
            "trombone",
            "bongos",
            "taiko drum",
            "koto",
            "shamisen",
            "Drum Machine",
            "Saxophone",
            "church organ",
            "kalimba",
            "double bass",
            "violin",
            "cello",
            "Bass Guitar",
            "Trumpet",
            "MIDI Controllers",
            "Theremin",
            "square wave",
            "record scratch effect"
        ]
        moodsArr = [
        "Dreamy", 
        "Energetic", 
        "Dark", 
        "relaxing",
        "aggressive",
        "Emotionally Intense", 
        "Uplifting", 
        "Nostalgic", 
        "Mysterious", 
        "Vibrant", 
        "Somber",
        "Introspective", 
        "Cinematic"
        ]
        techniqueArr = [
            "minimal",
            "major scale",
            "pentatonic scales",
            "dynamic melody",
            "Loop-Based Composition",
            "filter sweeps",
            "warm tones",
            "bass boosted",
            "Reverse Reverb Effects",
            "Frequency Modulation",
            "Layered Textures",
            "Automated Panning",
            "Field Recordings",
            "Gate Effect",
            "Vintage Records",
            "layered instrumentals",
            "Stutter Editing"
        ]

        function createTextUpdater(suggestions, elementId) {
            let unusedSuggestions = [...suggestions];
            let lastSuggested = null;
            return function updateText() {
                const element = document.getElementById(elementId);
                if (!element) {
                    console.error("Element not found:", elementId);
                    return;
                }
                if (unusedSuggestions.length === 0) {
                    unusedSuggestions = [...suggestions];
                    if (lastSuggested) {
                        unusedSuggestions = unusedSuggestions.filter(item => item !== lastSuggested);
                    }
                }
                const randomIndex = Math.floor(Math.random() * unusedSuggestions.length);
                const selectedText = unusedSuggestions[randomIndex];
                unusedSuggestions.splice(randomIndex, 1);
                lastSuggested = selectedText;
                element.textContent = selectedText;
                return selectedText;
            };
        }
        
        const displayRandomString = {
            instrument1: createTextUpdater(instrumentsArr, "instrument1"),
            instrument2: createTextUpdater(instrumentsArr, "instrument2"),
            style1: createTextUpdater(musicStyleArr, "style1"),
            mood1: createTextUpdater(moodsArr, "mood1"),
            tech1: createTextUpdater(techniqueArr, "tech1")
        };
        
        document.getElementById("instrument-gen1").onclick = displayRandomString.instrument1;
        document.getElementById("instrument-gen2").onclick = displayRandomString.instrument2;
        document.getElementById("style-gen").onclick = displayRandomString.style1;
        document.getElementById("mood-gen").onclick = displayRandomString.mood1;
        document.getElementById("tech-gen").onclick = displayRandomString.tech1;

        function generateAll() {
            displayRandomString.instrument1();
            displayRandomString.instrument2();
            displayRandomString.style1();
            displayRandomString.mood1();
            displayRandomString.tech1();
        }
        
