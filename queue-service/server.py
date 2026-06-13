import grpc
from concurrent import futures
import processor_pb2
import processor_pb2_grpc

queue_counter = 0

class QueueService(processor_pb2_grpc.QueueServiceServicer):

    def GetQueueNumber(self, request, context):
        global queue_counter

        queue_counter += 1

        return processor_pb2.QueueResponse(
            queue_number=queue_counter
        )


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

processor_pb2_grpc.add_QueueServiceServicer_to_server(
    QueueService(),
    server
)

server.add_insecure_port('[::]:50051')

print("Queue Service Running...")

server.start()

server.wait_for_termination() 