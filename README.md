

## To run the program

enter the command in the terminal
`roslaunch robot_launch ros_robot.launch`

## Pre-requisites

    pip install opencv-python
    pip install numpy 
    pip install face_recognition 
    pip install gtts 
    pip install pygame 
    pip install SpeechRecognition 
    pip install pyaudio 
    pip install keyboard
    sudo apt-get install mpg123

*To ensure pip is installed

    sudo apt-get update
    sudo apt-get install python-pip

After installing gtts, go to package.xml and add these 2 dependencies:

    <build_depend>gtts</build_depend>
    <exec_depend>gtts</exec_depend>

   

## When running:
The robot will:
 1. Detect and recognize faces in real-time. 
 2. Announce familiar faces.

>  "[The person's saved name]  is nearby"

 3. When unknown face is nearby:
 Prompt user for input when an unknown face is detected.

> "Do you wish to proceed to save contact?"

 4. If user answer yes; save new contacts.

>  User: "What's their name?"  
>  Robot: "[The user provides the name to
> save the contact]"  
> User: "Contact saved. Nice to meet you [provided
> name]"

 
 5. If user answer no; identify strangers.

>  "Saving contact cancelled."

 
 6. Loop and continuously monitor for new faces.

## Tips when using the robot

 - When giving out voice command wait for the microphone to be calibrated.

>  "Please wait. Calibrating microphone..."  
>  "Microphone calibrated."

 - There may be instances where the robot is having a harder time picking up the user's audio. Just keep giving out voice commands loudly and clearly until the robot picks it up eventually.
