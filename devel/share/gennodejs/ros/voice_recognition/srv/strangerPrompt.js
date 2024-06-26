// Auto-generated. Do not edit!

// (in-package voice_recognition.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class strangerPromptRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type strangerPromptRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type strangerPromptRequest
    let len;
    let data = new strangerPromptRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'voice_recognition/strangerPromptRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new strangerPromptRequest(null);
    return resolved;
    }
};

class strangerPromptResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.respond = null;
    }
    else {
      if (initObj.hasOwnProperty('respond')) {
        this.respond = initObj.respond
      }
      else {
        this.respond = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type strangerPromptResponse
    // Serialize message field [respond]
    bufferOffset = _serializer.string(obj.respond, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type strangerPromptResponse
    let len;
    let data = new strangerPromptResponse(null);
    // Deserialize message field [respond]
    data.respond = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.respond);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'voice_recognition/strangerPromptResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fd16295e9691f9b17f9af4d745cb5798';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string respond
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new strangerPromptResponse(null);
    if (msg.respond !== undefined) {
      resolved.respond = msg.respond;
    }
    else {
      resolved.respond = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: strangerPromptRequest,
  Response: strangerPromptResponse,
  md5sum() { return 'fd16295e9691f9b17f9af4d745cb5798'; },
  datatype() { return 'voice_recognition/strangerPrompt'; }
};
