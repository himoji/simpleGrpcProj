# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbank.proto\x12\x10\x63om.example.grpc\":\n\x0e\x64\x65positRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61sh_amount\x18\x02 \x01(\x05\";\n\x0fwithdrawRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61sh_amount\x18\x02 \x01(\x05\"I\n\x0bsendRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61sh_amount\x18\x02 \x01(\x05\x12\x10\n\x08taker_id\x18\x03 \x01(\x05\"#\n\x12validationResponce\x12\r\n\x05valid\x18\x01 \x01(\t2\xfb\x01\n\x04\x62\x61nk\x12Q\n\x07\x64\x65posit\x12 .com.example.grpc.depositRequest\x1a$.com.example.grpc.validationResponce\x12S\n\x08withdraw\x12!.com.example.grpc.withdrawRequest\x1a$.com.example.grpc.validationResponce\x12K\n\x04send\x12\x1d.com.example.grpc.sendRequest\x1a$.com.example.grpc.validationResponceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bank_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DEPOSITREQUEST']._serialized_start=32
  _globals['_DEPOSITREQUEST']._serialized_end=90
  _globals['_WITHDRAWREQUEST']._serialized_start=92
  _globals['_WITHDRAWREQUEST']._serialized_end=151
  _globals['_SENDREQUEST']._serialized_start=153
  _globals['_SENDREQUEST']._serialized_end=226
  _globals['_VALIDATIONRESPONCE']._serialized_start=228
  _globals['_VALIDATIONRESPONCE']._serialized_end=263
  _globals['_BANK']._serialized_start=266
  _globals['_BANK']._serialized_end=517
# @@protoc_insertion_point(module_scope)