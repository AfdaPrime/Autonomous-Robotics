#!/usr/bin/env python3
# install dulu nie sebelum run: 
# pip install gtts
# sudo apt-get install mpg123

# klu x de pip, install nie dulu:
# sudo apt-get update
# sudo apt-get install python-pip



import rospy
from gtts import gTTS
import os
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f"Received text: {data.data}")
    mytext = data.data
    language = 'en'
    myobj = gTTS(text=mytext+" is nearby", lang=language, slow=False)
    myobj.save("/tmp/welcome.mp3")
    os.system("mpg123 /tmp/welcome.mp3")

def listener():
    rospy.init_node('gtts_node', anonymous=True)
    rospy.Subscriber('gtts_text', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

  
# lps install, pergi dkt package.xml and tmbh 2 dependency nie
# <build_depend>gtts</build_depend>
# <exec_depend>gtts</exec_depend>
