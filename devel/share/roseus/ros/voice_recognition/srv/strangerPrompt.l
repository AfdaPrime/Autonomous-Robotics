;; Auto-generated. Do not edit!


(when (boundp 'voice_recognition::strangerPrompt)
  (if (not (find-package "VOICE_RECOGNITION"))
    (make-package "VOICE_RECOGNITION"))
  (shadow 'strangerPrompt (find-package "VOICE_RECOGNITION")))
(unless (find-package "VOICE_RECOGNITION::STRANGERPROMPT")
  (make-package "VOICE_RECOGNITION::STRANGERPROMPT"))
(unless (find-package "VOICE_RECOGNITION::STRANGERPROMPTREQUEST")
  (make-package "VOICE_RECOGNITION::STRANGERPROMPTREQUEST"))
(unless (find-package "VOICE_RECOGNITION::STRANGERPROMPTRESPONSE")
  (make-package "VOICE_RECOGNITION::STRANGERPROMPTRESPONSE"))

(in-package "ROS")





(defclass voice_recognition::strangerPromptRequest
  :super ros::object
  :slots ())

(defmethod voice_recognition::strangerPromptRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass voice_recognition::strangerPromptResponse
  :super ros::object
  :slots (_respond ))

(defmethod voice_recognition::strangerPromptResponse
  (:init
   (&key
    ((:respond __respond) "")
    )
   (send-super :init)
   (setq _respond (string __respond))
   self)
  (:respond
   (&optional __respond)
   (if __respond (setq _respond __respond)) _respond)
  (:serialization-length
   ()
   (+
    ;; string _respond
    4 (length _respond)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _respond
       (write-long (length _respond) s) (princ _respond s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _respond
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _respond (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass voice_recognition::strangerPrompt
  :super ros::object
  :slots ())

(setf (get voice_recognition::strangerPrompt :md5sum-) "fd16295e9691f9b17f9af4d745cb5798")
(setf (get voice_recognition::strangerPrompt :datatype-) "voice_recognition/strangerPrompt")
(setf (get voice_recognition::strangerPrompt :request) voice_recognition::strangerPromptRequest)
(setf (get voice_recognition::strangerPrompt :response) voice_recognition::strangerPromptResponse)

(defmethod voice_recognition::strangerPromptRequest
  (:response () (instance voice_recognition::strangerPromptResponse :init)))

(setf (get voice_recognition::strangerPromptRequest :md5sum-) "fd16295e9691f9b17f9af4d745cb5798")
(setf (get voice_recognition::strangerPromptRequest :datatype-) "voice_recognition/strangerPromptRequest")
(setf (get voice_recognition::strangerPromptRequest :definition-)
      "---
string respond
")

(setf (get voice_recognition::strangerPromptResponse :md5sum-) "fd16295e9691f9b17f9af4d745cb5798")
(setf (get voice_recognition::strangerPromptResponse :datatype-) "voice_recognition/strangerPromptResponse")
(setf (get voice_recognition::strangerPromptResponse :definition-)
      "---
string respond
")



(provide :voice_recognition/strangerPrompt "fd16295e9691f9b17f9af4d745cb5798")


