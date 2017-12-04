# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import dist_bank_pb2 as dist__bank__pb2


class DistBankStub(object):
  """definition of the service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.LookUpAccount = channel.unary_unary(
        '/dist_bank.DistBank/LookUpAccount',
        request_serializer=dist__bank__pb2.LookUpRequest.SerializeToString,
        response_deserializer=dist__bank__pb2.BalanceRecord.FromString,
        )
    self.Withdraw = channel.unary_unary(
        '/dist_bank.DistBank/Withdraw',
        request_serializer=dist__bank__pb2.WithdrawRequest.SerializeToString,
        response_deserializer=dist__bank__pb2.BalanceRecord.FromString,
        )
    self.Save = channel.unary_unary(
        '/dist_bank.DistBank/Save',
        request_serializer=dist__bank__pb2.SaveRequest.SerializeToString,
        response_deserializer=dist__bank__pb2.BalanceRecord.FromString,
        )
    self.ProbeStatus = channel.unary_unary(
        '/dist_bank.DistBank/ProbeStatus',
        request_serializer=dist__bank__pb2.ProbeRequest.SerializeToString,
        response_deserializer=dist__bank__pb2.Status.FromString,
        )
    self.Synchronize = channel.unary_unary(
        '/dist_bank.DistBank/Synchronize',
        request_serializer=dist__bank__pb2.QueuedOperation.SerializeToString,
        response_deserializer=dist__bank__pb2.SynAck.FromString,
        )


class DistBankServicer(object):
  """definition of the service
  """

  def LookUpAccount(self, request, context):
    """Methods for client-server communication:
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Withdraw(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Save(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProbeStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Synchronize(self, request, context):
    """Methods for server-server communication only, client shouldn't use these!
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DistBankServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'LookUpAccount': grpc.unary_unary_rpc_method_handler(
          servicer.LookUpAccount,
          request_deserializer=dist__bank__pb2.LookUpRequest.FromString,
          response_serializer=dist__bank__pb2.BalanceRecord.SerializeToString,
      ),
      'Withdraw': grpc.unary_unary_rpc_method_handler(
          servicer.Withdraw,
          request_deserializer=dist__bank__pb2.WithdrawRequest.FromString,
          response_serializer=dist__bank__pb2.BalanceRecord.SerializeToString,
      ),
      'Save': grpc.unary_unary_rpc_method_handler(
          servicer.Save,
          request_deserializer=dist__bank__pb2.SaveRequest.FromString,
          response_serializer=dist__bank__pb2.BalanceRecord.SerializeToString,
      ),
      'ProbeStatus': grpc.unary_unary_rpc_method_handler(
          servicer.ProbeStatus,
          request_deserializer=dist__bank__pb2.ProbeRequest.FromString,
          response_serializer=dist__bank__pb2.Status.SerializeToString,
      ),
      'Synchronize': grpc.unary_unary_rpc_method_handler(
          servicer.Synchronize,
          request_deserializer=dist__bank__pb2.QueuedOperation.FromString,
          response_serializer=dist__bank__pb2.SynAck.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dist_bank.DistBank', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
