# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\"\"\n\x11\x43heckTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\":\n\x12\x43heckTokenResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x15\n\rnational_code\x18\x02 \x01(\t2G\n\x0b\x41uthService\x12\x38\n\x0b\x63heck_token\x12\x12.CheckTokenRequest\x1a\x13.CheckTokenResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKTOKENREQUEST._serialized_start=14
  _CHECKTOKENREQUEST._serialized_end=48
  _CHECKTOKENRESPONSE._serialized_start=50
  _CHECKTOKENRESPONSE._serialized_end=108
  _AUTHSERVICE._serialized_start=110
  _AUTHSERVICE._serialized_end=181
# @@protoc_insertion_point(module_scope)