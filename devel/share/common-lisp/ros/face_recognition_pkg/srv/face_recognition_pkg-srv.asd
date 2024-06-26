
(cl:in-package :asdf)

(defsystem "face_recognition_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "strangerPrompt" :depends-on ("_package_strangerPrompt"))
    (:file "_package_strangerPrompt" :depends-on ("_package"))
  ))