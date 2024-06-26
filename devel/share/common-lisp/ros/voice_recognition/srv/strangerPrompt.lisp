; Auto-generated. Do not edit!


(cl:in-package voice_recognition-srv)


;//! \htmlinclude strangerPrompt-request.msg.html

(cl:defclass <strangerPrompt-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass strangerPrompt-request (<strangerPrompt-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <strangerPrompt-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'strangerPrompt-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name voice_recognition-srv:<strangerPrompt-request> is deprecated: use voice_recognition-srv:strangerPrompt-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <strangerPrompt-request>) ostream)
  "Serializes a message object of type '<strangerPrompt-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <strangerPrompt-request>) istream)
  "Deserializes a message object of type '<strangerPrompt-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<strangerPrompt-request>)))
  "Returns string type for a service object of type '<strangerPrompt-request>"
  "voice_recognition/strangerPromptRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'strangerPrompt-request)))
  "Returns string type for a service object of type 'strangerPrompt-request"
  "voice_recognition/strangerPromptRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<strangerPrompt-request>)))
  "Returns md5sum for a message object of type '<strangerPrompt-request>"
  "fd16295e9691f9b17f9af4d745cb5798")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'strangerPrompt-request)))
  "Returns md5sum for a message object of type 'strangerPrompt-request"
  "fd16295e9691f9b17f9af4d745cb5798")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<strangerPrompt-request>)))
  "Returns full string definition for message of type '<strangerPrompt-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'strangerPrompt-request)))
  "Returns full string definition for message of type 'strangerPrompt-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <strangerPrompt-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <strangerPrompt-request>))
  "Converts a ROS message object to a list"
  (cl:list 'strangerPrompt-request
))
;//! \htmlinclude strangerPrompt-response.msg.html

(cl:defclass <strangerPrompt-response> (roslisp-msg-protocol:ros-message)
  ((respond
    :reader respond
    :initarg :respond
    :type cl:string
    :initform ""))
)

(cl:defclass strangerPrompt-response (<strangerPrompt-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <strangerPrompt-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'strangerPrompt-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name voice_recognition-srv:<strangerPrompt-response> is deprecated: use voice_recognition-srv:strangerPrompt-response instead.")))

(cl:ensure-generic-function 'respond-val :lambda-list '(m))
(cl:defmethod respond-val ((m <strangerPrompt-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader voice_recognition-srv:respond-val is deprecated.  Use voice_recognition-srv:respond instead.")
  (respond m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <strangerPrompt-response>) ostream)
  "Serializes a message object of type '<strangerPrompt-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'respond))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'respond))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <strangerPrompt-response>) istream)
  "Deserializes a message object of type '<strangerPrompt-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'respond) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'respond) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<strangerPrompt-response>)))
  "Returns string type for a service object of type '<strangerPrompt-response>"
  "voice_recognition/strangerPromptResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'strangerPrompt-response)))
  "Returns string type for a service object of type 'strangerPrompt-response"
  "voice_recognition/strangerPromptResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<strangerPrompt-response>)))
  "Returns md5sum for a message object of type '<strangerPrompt-response>"
  "fd16295e9691f9b17f9af4d745cb5798")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'strangerPrompt-response)))
  "Returns md5sum for a message object of type 'strangerPrompt-response"
  "fd16295e9691f9b17f9af4d745cb5798")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<strangerPrompt-response>)))
  "Returns full string definition for message of type '<strangerPrompt-response>"
  (cl:format cl:nil "string respond~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'strangerPrompt-response)))
  "Returns full string definition for message of type 'strangerPrompt-response"
  (cl:format cl:nil "string respond~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <strangerPrompt-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'respond))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <strangerPrompt-response>))
  "Converts a ROS message object to a list"
  (cl:list 'strangerPrompt-response
    (cl:cons ':respond (respond msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'strangerPrompt)))
  'strangerPrompt-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'strangerPrompt)))
  'strangerPrompt-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'strangerPrompt)))
  "Returns string type for a service object of type '<strangerPrompt>"
  "voice_recognition/strangerPrompt")