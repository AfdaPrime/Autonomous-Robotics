

## How to run the robot's program

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

   

## Tips when using the robot

 - When giving out voice command wait for the microphone to be calibrated.
 - There may be instances where the robot is having a harder time picking up the user's audio. Just keep giving out voice commands loudly and clearly until the robot picks it up eventually.
