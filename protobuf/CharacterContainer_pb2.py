# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CharacterContainer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CharacterContainer.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x43haracterContainer.proto\"0\n\x12\x43haracterContainer\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c')
)




_CHARACTERCONTAINER = _descriptor.Descriptor(
  name='CharacterContainer',
  full_name='CharacterContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CharacterContainer.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='CharacterContainer.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['CharacterContainer'] = _CHARACTERCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CharacterContainer = _reflection.GeneratedProtocolMessageType('CharacterContainer', (_message.Message,), dict(
  DESCRIPTOR = _CHARACTERCONTAINER,
  __module__ = 'CharacterContainer_pb2'
  # @@protoc_insertion_point(class_scope:CharacterContainer)
  ))
_sym_db.RegisterMessage(CharacterContainer)


# @@protoc_insertion_point(module_scope)
