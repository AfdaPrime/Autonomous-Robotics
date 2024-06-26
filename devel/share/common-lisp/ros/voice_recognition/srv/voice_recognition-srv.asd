
(cl:in-package :asdf)

(defsystem "voice_recognition-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "strangerPrompt" :depends-on ("_package_strangerPrompt"))
    (:file "_package_strangerPrompt" :depends-on ("_package"))
  ))