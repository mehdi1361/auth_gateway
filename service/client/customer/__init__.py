import grpc
from service.client.customer import customer_pb2_grpc
from service.client.customer import customer_pb2
from core.config import settings


def client_connection():
    return grpc.insecure_channel(
        f"{settings.CUSTOMER_SERVICE_GRPC_SERVER_URL}:{settings.CUSTOMER_SERVICE_GRPC_SERVER_PORT}"
    )

class CustomerClient:
    @staticmethod
    def login_by_national_code(national_code):
        with client_connection() as channel:
            stub = customer_pb2_grpc.CustomerControllerStub(channel)
            data = stub.LoginByNationalId(
                customer_pb2.LoginByNationalIdRequest(
                    national_id=national_code
                )
            )

            return data


    @staticmethod
    def verified(national_code, verification_code):
        with client_connection() as channel:
            stub = customer_pb2_grpc.CustomerControllerStub(channel)
            data = stub.CustomerVerified(
                customer_pb2.CustomerVerifiedRequest(
                    normal_national_code=national_code,
                    verification_code=verification_code
                )
            )

            return data
