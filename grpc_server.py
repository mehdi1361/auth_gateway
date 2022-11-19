#!/usr/bin/env python3
import service.server.auth_pb2_grpc
import json
from service.server.auth_pb2 import CheckTokenRequest, CheckTokenResponse
from service.redis import RedisClient
from core.config import settings

from concurrent import futures
import grpc

class AtuhService(
        service.server.auth_pb2_grpc.AuthServiceServicer
):
    def check_token(self, request, context):
        national_code = RedisClient.get_token(request.token)
        return CheckTokenResponse(
            valid=False if national_code is None else True,
            national_code=national_code
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.server.auth_pb2_grpc.add_AuthServiceServicer_to_server(
        AtuhService(), server
    )
    server.add_insecure_port(f"[::]:{settings.GRPC_PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
