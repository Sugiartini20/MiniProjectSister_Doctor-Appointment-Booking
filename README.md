🏥 Doctor Appointment Booking - Proyek Sister
Proyek ini mengimplementasikan arsitektur microservice dengan semua ketentuan tugas Sistem Terdistribusi.

📂 Struktur Proyek
PROJECT SISTER/
├── .vscode/
│ └── settings.json
├── booking-service/
│ ├── pycache/
│ ├── app.py # Main Flask application
│ ├── client.py # gRPC client
│ ├── db.py # Database models
│ ├── Dockerfile
│ ├── processor_pb2_grpc.py # gRPC generated
│ ├── processor_pb2.py # gRPC generated
│ ├── producer.py # RabbitMQ producer
│ └── requirements.txt
├── database/
│ └── init.sql # Database initialization
├── frontend/
│ ├── booking.html # Booking page
│ ├── detail.html # Detail page
│ ├── index.html # Main page
│ └── style.css # Styling
├── notification-service/
│ ├── consumer.py # RabbitMQ consumer
│ ├── Dockerfile
│ └── requirements.txt
├── queue-service/
│ ├── pycache/
│ ├── Dockerfile
│ ├── processor_pb2_grpc.py
│ ├── processor_pb2.py
│ └── server.py # gRPC server
├── docker-compose.yml
└── README.md
📋 Ketentuan yang Sudah Terpenuhi
✅ REST-API
Booking service menyediakan REST API.

✅ RPC (gRPC Stub-based)
Queue Service menggunakan gRPC untuk komunikasi.

✅ Asynchronous Workflow (RabbitMQ)
Notification service consumer pesan dari RabbitMQ.

✅ Persistent Storage (PostgreSQL)
Semua data disimpan di PostgreSQL.

✅ Leader Election (Algoritma Bully)
3 instance Queue Service dengan failover otomatis.

✅ Load Balancing API
Load balancer otomatis menemukan dan mengirim request ke leader.

🚀 Cara Menjalankan
1. Jalankan Database & RabbitMQ
docker-compose up -d
2. Jalankan Queue Service (3 Instances)
Terminal 1:

cd queue-service
$env:PORT="50051"
$env:PEERS="[{""host"":""localhost"",""port"":""50052""},{""host"":""localhost"",""port"":""50053""}]"
python server_bully.py
Terminal 2:

cd queue-service
$env:PORT="50052"
$env:PEERS="[{""host"":""localhost"",""port"":""50051""},{""host"":""localhost"",""port"":""50053""}]"
python server_bully.py
Terminal 3:

cd queue-service
$env:PORT="50053"
$env:PEERS="[{""host"":""localhost"",""port"":""50051""},{""host"":""localhost"",""port"":""50052""}]"
python server_bully.py
3. Jalankan Load Balancer
cd load-balancer
python load_balancer.py
4. Jalankan Booking Service
cd booking-service
$env:LB_URL="http://localhost:5001/queue"
python app.py
5. Jalankan Notification Service
cd notification-service
python consumer.py
6. (Opsional) Jalankan Locust Load Testing
cd locust
locust -H http://127.0.0.1:5000
Buka http://localhost:8089

🌐 Akses Aplikasi
Service	URL
Frontend	Buka frontend/index.html
Booking API	http://localhost:5000
Load Balancer	http://localhost:5001
Locust UI	http://localhost:8089
📚 Teknologi yang Digunakan
Backend: Python (Flask)
RPC: gRPC
Database: PostgreSQL
Message Broker: RabbitMQ
Load Testing: Locust
