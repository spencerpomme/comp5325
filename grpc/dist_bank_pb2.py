# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dist_bank.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dist_bank.proto',
  package='dist_bank',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64ist_bank.proto\x12\tdist_bank\"\x1c\n\rLookUpRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\"3\n\x0fWithdrawRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x13\n\x0bwith_amount\x18\x02 \x01(\x02\"/\n\x0bSaveRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x13\n\x0bsave_amount\x18\x02 \x01(\x02\"N\n\rBalanceRecord\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x02\x12\r\n\x05index\x18\x03 \x01(\x05\x12\x10\n\x08res_info\x18\x04 \x01(\t\"\x1b\n\x0cProbeRequest\x12\x0b\n\x03hey\x18\x01 \x01(\t\"\x17\n\x06Status\x12\r\n\x05\x61live\x18\x01 \x01(\x05\"\xae\x01\n\x0fQueuedOperation\x12/\n\x0blook_up_req\x18\x01 \x01(\x0b\x32\x18.dist_bank.LookUpRequestH\x00\x12\x32\n\x0cwithdraw_req\x18\x02 \x01(\x0b\x32\x1a.dist_bank.WithdrawRequestH\x00\x12*\n\x08save_req\x18\x03 \x01(\x0b\x32\x16.dist_bank.SaveRequestH\x00\x42\n\n\x08requests\"\x1c\n\x06SynAck\x12\x12\n\nsuccessful\x18\x01 \x01(\x05\x32\xce\x02\n\x08\x44istBank\x12\x45\n\rLookUpAccount\x12\x18.dist_bank.LookUpRequest\x1a\x18.dist_bank.BalanceRecord\"\x00\x12\x42\n\x08Withdraw\x12\x1a.dist_bank.WithdrawRequest\x1a\x18.dist_bank.BalanceRecord\"\x00\x12:\n\x04Save\x12\x16.dist_bank.SaveRequest\x1a\x18.dist_bank.BalanceRecord\"\x00\x12;\n\x0bProbeStatus\x12\x17.dist_bank.ProbeRequest\x1a\x11.dist_bank.Status\"\x00\x12>\n\x0bSynchronize\x12\x1a.dist_bank.QueuedOperation\x1a\x11.dist_bank.SynAck\"\x00\x62\x06proto3')
)




_LOOKUPREQUEST = _descriptor.Descriptor(
  name='LookUpRequest',
  full_name='dist_bank.LookUpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dist_bank.LookUpRequest.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=58,
)


_WITHDRAWREQUEST = _descriptor.Descriptor(
  name='WithdrawRequest',
  full_name='dist_bank.WithdrawRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dist_bank.WithdrawRequest.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_amount', full_name='dist_bank.WithdrawRequest.with_amount', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=111,
)


_SAVEREQUEST = _descriptor.Descriptor(
  name='SaveRequest',
  full_name='dist_bank.SaveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dist_bank.SaveRequest.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_amount', full_name='dist_bank.SaveRequest.save_amount', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=160,
)


_BALANCERECORD = _descriptor.Descriptor(
  name='BalanceRecord',
  full_name='dist_bank.BalanceRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dist_bank.BalanceRecord.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='balance', full_name='dist_bank.BalanceRecord.balance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='dist_bank.BalanceRecord.index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_info', full_name='dist_bank.BalanceRecord.res_info', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=240,
)


_PROBEREQUEST = _descriptor.Descriptor(
  name='ProbeRequest',
  full_name='dist_bank.ProbeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hey', full_name='dist_bank.ProbeRequest.hey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=269,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='dist_bank.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alive', full_name='dist_bank.Status.alive', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=294,
)


_QUEUEDOPERATION = _descriptor.Descriptor(
  name='QueuedOperation',
  full_name='dist_bank.QueuedOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='look_up_req', full_name='dist_bank.QueuedOperation.look_up_req', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='withdraw_req', full_name='dist_bank.QueuedOperation.withdraw_req', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_req', full_name='dist_bank.QueuedOperation.save_req', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='requests', full_name='dist_bank.QueuedOperation.requests',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=297,
  serialized_end=471,
)


_SYNACK = _descriptor.Descriptor(
  name='SynAck',
  full_name='dist_bank.SynAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successful', full_name='dist_bank.SynAck.successful', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=501,
)

_QUEUEDOPERATION.fields_by_name['look_up_req'].message_type = _LOOKUPREQUEST
_QUEUEDOPERATION.fields_by_name['withdraw_req'].message_type = _WITHDRAWREQUEST
_QUEUEDOPERATION.fields_by_name['save_req'].message_type = _SAVEREQUEST
_QUEUEDOPERATION.oneofs_by_name['requests'].fields.append(
  _QUEUEDOPERATION.fields_by_name['look_up_req'])
_QUEUEDOPERATION.fields_by_name['look_up_req'].containing_oneof = _QUEUEDOPERATION.oneofs_by_name['requests']
_QUEUEDOPERATION.oneofs_by_name['requests'].fields.append(
  _QUEUEDOPERATION.fields_by_name['withdraw_req'])
_QUEUEDOPERATION.fields_by_name['withdraw_req'].containing_oneof = _QUEUEDOPERATION.oneofs_by_name['requests']
_QUEUEDOPERATION.oneofs_by_name['requests'].fields.append(
  _QUEUEDOPERATION.fields_by_name['save_req'])
_QUEUEDOPERATION.fields_by_name['save_req'].containing_oneof = _QUEUEDOPERATION.oneofs_by_name['requests']
DESCRIPTOR.message_types_by_name['LookUpRequest'] = _LOOKUPREQUEST
DESCRIPTOR.message_types_by_name['WithdrawRequest'] = _WITHDRAWREQUEST
DESCRIPTOR.message_types_by_name['SaveRequest'] = _SAVEREQUEST
DESCRIPTOR.message_types_by_name['BalanceRecord'] = _BALANCERECORD
DESCRIPTOR.message_types_by_name['ProbeRequest'] = _PROBEREQUEST
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['QueuedOperation'] = _QUEUEDOPERATION
DESCRIPTOR.message_types_by_name['SynAck'] = _SYNACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LookUpRequest = _reflection.GeneratedProtocolMessageType('LookUpRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOOKUPREQUEST,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.LookUpRequest)
  ))
_sym_db.RegisterMessage(LookUpRequest)

WithdrawRequest = _reflection.GeneratedProtocolMessageType('WithdrawRequest', (_message.Message,), dict(
  DESCRIPTOR = _WITHDRAWREQUEST,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.WithdrawRequest)
  ))
_sym_db.RegisterMessage(WithdrawRequest)

SaveRequest = _reflection.GeneratedProtocolMessageType('SaveRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAVEREQUEST,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.SaveRequest)
  ))
_sym_db.RegisterMessage(SaveRequest)

BalanceRecord = _reflection.GeneratedProtocolMessageType('BalanceRecord', (_message.Message,), dict(
  DESCRIPTOR = _BALANCERECORD,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.BalanceRecord)
  ))
_sym_db.RegisterMessage(BalanceRecord)

ProbeRequest = _reflection.GeneratedProtocolMessageType('ProbeRequest', (_message.Message,), dict(
  DESCRIPTOR = _PROBEREQUEST,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.ProbeRequest)
  ))
_sym_db.RegisterMessage(ProbeRequest)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.Status)
  ))
_sym_db.RegisterMessage(Status)

QueuedOperation = _reflection.GeneratedProtocolMessageType('QueuedOperation', (_message.Message,), dict(
  DESCRIPTOR = _QUEUEDOPERATION,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.QueuedOperation)
  ))
_sym_db.RegisterMessage(QueuedOperation)

SynAck = _reflection.GeneratedProtocolMessageType('SynAck', (_message.Message,), dict(
  DESCRIPTOR = _SYNACK,
  __module__ = 'dist_bank_pb2'
  # @@protoc_insertion_point(class_scope:dist_bank.SynAck)
  ))
_sym_db.RegisterMessage(SynAck)



_DISTBANK = _descriptor.ServiceDescriptor(
  name='DistBank',
  full_name='dist_bank.DistBank',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=504,
  serialized_end=838,
  methods=[
  _descriptor.MethodDescriptor(
    name='LookUpAccount',
    full_name='dist_bank.DistBank.LookUpAccount',
    index=0,
    containing_service=None,
    input_type=_LOOKUPREQUEST,
    output_type=_BALANCERECORD,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Withdraw',
    full_name='dist_bank.DistBank.Withdraw',
    index=1,
    containing_service=None,
    input_type=_WITHDRAWREQUEST,
    output_type=_BALANCERECORD,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Save',
    full_name='dist_bank.DistBank.Save',
    index=2,
    containing_service=None,
    input_type=_SAVEREQUEST,
    output_type=_BALANCERECORD,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ProbeStatus',
    full_name='dist_bank.DistBank.ProbeStatus',
    index=3,
    containing_service=None,
    input_type=_PROBEREQUEST,
    output_type=_STATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Synchronize',
    full_name='dist_bank.DistBank.Synchronize',
    index=4,
    containing_service=None,
    input_type=_QUEUEDOPERATION,
    output_type=_SYNACK,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISTBANK)

DESCRIPTOR.services_by_name['DistBank'] = _DISTBANK

# @@protoc_insertion_point(module_scope)
