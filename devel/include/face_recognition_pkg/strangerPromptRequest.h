// Generated by gencpp from file face_recognition_pkg/strangerPromptRequest.msg
// DO NOT EDIT!


#ifndef FACE_RECOGNITION_PKG_MESSAGE_STRANGERPROMPTREQUEST_H
#define FACE_RECOGNITION_PKG_MESSAGE_STRANGERPROMPTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace face_recognition_pkg
{
template <class ContainerAllocator>
struct strangerPromptRequest_
{
  typedef strangerPromptRequest_<ContainerAllocator> Type;

  strangerPromptRequest_()
    {
    }
  strangerPromptRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> const> ConstPtr;

}; // struct strangerPromptRequest_

typedef ::face_recognition_pkg::strangerPromptRequest_<std::allocator<void> > strangerPromptRequest;

typedef boost::shared_ptr< ::face_recognition_pkg::strangerPromptRequest > strangerPromptRequestPtr;
typedef boost::shared_ptr< ::face_recognition_pkg::strangerPromptRequest const> strangerPromptRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace face_recognition_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "face_recognition_pkg/strangerPromptRequest";
  }

  static const char* value(const ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct strangerPromptRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::face_recognition_pkg::strangerPromptRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // FACE_RECOGNITION_PKG_MESSAGE_STRANGERPROMPTREQUEST_H