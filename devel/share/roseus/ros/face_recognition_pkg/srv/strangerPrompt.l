;; Auto-generated. Do not edit!


(when (boundp 'face_recognition_pkg::strangerPrompt)
  (if (not (find-package "FACE_RECOGNITION_PKG"))
    (make-package "FACE_RECOGNITION_PKG"))
  (shadow 'strangerPrompt (find-package "FACE_RECOGNITION_PKG")))
(unless (find-package "FACE_RECOGNITION_PKG::STRANGERPROMPT")
  (make-package "FACE_RECOGNITION_PKG::STRANGERPROMPT"))
(unless (find-package "FACE_RECOGNITION_PKG::STRANGERPROMPTREQUEST")
  (make-package "FACE_RECOGNITION_PKG::STRANGERPROMPTREQUEST"))
(unless (find-package "FACE_RECOGNITION_PKG::STRANGERPROMPTRESPONSE")
  (make-package "FACE_RECOGNITION_PKG::STRANGERPROMPTRESPONSE"))

(in-package "ROS")





(defclass face_recognition_pkg::strangerPromptRequest
  :super ros::object
  :slots ())

(defmethod face_recognition_pkg::strangerPromptRequest
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

(defclass face_recognition_pkg::strangerPromptResponse
  :super ros::object
  :slots (_respond ))

(defmethod face_recognition_pkg::strangerPromptResponse
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

(defclass face_recognition_pkg::strangerPrompt
  :super ros::object
  :slots ())

(setf (get face_recognition_pkg::strangerPrompt :md5sum-) "fd16295e9691f9b17f9af4d745cb5798")
(setf (get face_recognition_pkg::strangerPrompt :datatype-) "face_recognition_pkg/strangerPrompt")
(setf (get face_recognition_pkg::strangerPrompt :request) face_recognition_pkg::strangerPromptRequest)
(setf (get face_recognition_pkg::strangerPrompt :response) face_recognition_pkg::strangerPromptResponse)

(defmethod face_recognition_pkg::strangerPromptRequest
  (:response () (instance face_recognition_pkg::strangerPromptResponse :init)))

(setf (get face_recognition_pkg::strangerPromptRequest :md5sum-) "fd16295e9691f9b17f9af4d745cb5798")
(setf (get face_recognition_pkg::strangerPromptRequest :datatype-) "face_recognition_pkg/strangerPromptRequest")
(setf (get face_recognition_pkg::strangerPromptRequest :definition-)
      "---
string respond
")

(setf (get face_recognition_pkg::strangerPromptResponse :md5sum-) "fd16295e9691f9b17f9af4d745cb5798")
(setf (get face_recognition_pkg::strangerPromptResponse :datatype-) "face_recognition_pkg/strangerPromptResponse")
(setf (get face_recognition_pkg::strangerPromptResponse :definition-)
      "---
string respond
")



(provide :face_recognition_pkg/strangerPrompt "fd16295e9691f9b17f9af4d745cb5798")


