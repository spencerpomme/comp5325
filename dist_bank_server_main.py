# MainServer.py
# The main server of the service.

from concurrent import futures
import time
import grpc
import dist_bank_pb2_grpc
import dist_bank_pb2
import dist_bank_resources

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DistBank(route_guide_pb2_grpc.DistBankServicer):
    """
    Provides methods that implement functionality of dist bank server.
    """
    def __init__(self):
        self.db = dist_bank_resources.read_route_guide_database()

    # TODO: Implement other methods.