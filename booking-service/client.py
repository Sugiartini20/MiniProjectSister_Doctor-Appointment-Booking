import grpc
import processor_pb2
import processor_pb2_grpc

def get_queue_number(patient_name):

    channel = grpc.insecure_channel('localhost:50051')

    stub = processor_pb2_grpc.QueueServiceStub(channel)

    response = stub.GetQueueNumber(
        processor_pb2.QueueRequest(
            patient_name=patient_name
        )
    )

    return response.queue_number