# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Ironman_pb2 as Ironman__pb2


class BackendRenderStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.InitHandler = channel.unary_unary(
        '/helloworld.BackendRender/InitHandler',
        request_serializer=Ironman__pb2.InitCommand.SerializeToString,
        response_deserializer=Ironman__pb2.InitReply.FromString,
        )
    self.RenderHandler = channel.unary_unary(
        '/helloworld.BackendRender/RenderHandler',
        request_serializer=Ironman__pb2.RenderCommand.SerializeToString,
        response_deserializer=Ironman__pb2.RenderReply.FromString,
        )


class BackendRenderServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def InitHandler(self, request, context):
    """Sends initCommand
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RenderHandler(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BackendRenderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'InitHandler': grpc.unary_unary_rpc_method_handler(
          servicer.InitHandler,
          request_deserializer=Ironman__pb2.InitCommand.FromString,
          response_serializer=Ironman__pb2.InitReply.SerializeToString,
      ),
      'RenderHandler': grpc.unary_unary_rpc_method_handler(
          servicer.RenderHandler,
          request_deserializer=Ironman__pb2.RenderCommand.FromString,
          response_serializer=Ironman__pb2.RenderReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.BackendRender', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SystemDispatcherStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Regist = channel.unary_unary(
        '/helloworld.SystemDispatcher/Regist',
        request_serializer=Ironman__pb2.RegistMsg.SerializeToString,
        response_deserializer=Ironman__pb2.RegistResultMsg.FromString,
        )
    self.GetAddress = channel.unary_unary(
        '/helloworld.SystemDispatcher/GetAddress',
        request_serializer=Ironman__pb2.AddressMsg.SerializeToString,
        response_deserializer=Ironman__pb2.AddressReturnMsg.FromString,
        )


class SystemDispatcherServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Regist(self, request, context):
    """register services
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddress(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SystemDispatcherServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Regist': grpc.unary_unary_rpc_method_handler(
          servicer.Regist,
          request_deserializer=Ironman__pb2.RegistMsg.FromString,
          response_serializer=Ironman__pb2.RegistResultMsg.SerializeToString,
      ),
      'GetAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddress,
          request_deserializer=Ironman__pb2.AddressMsg.FromString,
          response_serializer=Ironman__pb2.AddressReturnMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.SystemDispatcher', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
