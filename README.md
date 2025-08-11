# Back-Silque

A FastAPI-based backend service with LocalStack S3 integration for development and testing.

## 🚀 Quick Start

### Prerequisites

Before running this project, make sure you have the following installed:

- **Python 3.8+**
- **Docker** (for LocalStack)
- **AWS CLI** (for S3 operations)
- **pip** (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd back-silque
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS CLI** (for LocalStack)
   ```bash
   aws configure
   # Enter any dummy values for AWS Access Key ID and Secret Access Key
   # For LocalStack, these can be: dummy/dummy
   ```

### Development Setup

The project includes a convenient development script that handles all the setup automatically:

```bash
./dev.sh
```

This script will:

- Stop and remove any existing LocalStack containers
- Start a new LocalStack container with S3 service enabled
- Wait for the S3 service to be ready
- Create a default S3 bucket named `clothes-images`
- Start the FastAPI development server

### Manual Setup (Alternative)

If you prefer to set up components manually:

1. **Start LocalStack**

   ```bash
   docker run -d --name localstack-test -p 4566:4566 -e SERVICES=s3 localstack/localstack
   ```

2. **Wait for LocalStack to be ready**

   ```bash
   until aws --endpoint-url=http://localhost:4566 s3 ls >/dev/null 2>&1; do
     echo "Waiting for S3 service..."
     sleep 2
   done
   ```

3. **Create S3 bucket**

   ```bash
   aws --endpoint-url=http://localhost:4566 s3 mb s3://clothes-images
   ```

4. **Start the FastAPI server**
   ```bash
   export PYTHONPATH=.
   fastapi dev main.py
   ```

## 🛠️ Project Structure

```
back-silque/
├── app/                    # Main application package
│   ├── models/            # Database models
│   ├── routers/           # API route handlers
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic services
│   └── database.py        # Database configuration
├── main.py                # FastAPI application entry point
├── dev.sh                 # Development setup script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

The application uses the following environment variables (create a `.env` file if needed):

- Database connection strings
- AWS credentials (for production)
- API keys and secrets

### LocalStack Configuration

- **Endpoint URL**: `http://localhost:4566`
- **Default Bucket**: `clothes-images`
- **Services**: S3 only (for development)

## 📡 API Endpoints

The API is available at:

- **Base URL**: `http://localhost:8000`
- **API Documentation**: `http://localhost:8000/docs`
- **API v1**: `http://localhost:8000/api/v1`

### Available Endpoints

- `GET /` - Health check
- `GET /items/{item_id}` - Example endpoint
- `GET /api/v1/*` - Version 1 API routes

## 🧪 Testing

### S3 Operations

To check S3 bucket contents:

```bash
./dev.sh check-s3 [bucket-name]
```

This will display:

- Bucket contents listing
- Detailed object information
- File sizes and modification dates

## 🐛 Troubleshooting

### Common Issues

1. **LocalStack not starting**

   - Ensure Docker is running
   - Check if port 4566 is available
   - Try removing existing containers: `docker stop localstack-test && docker rm localstack-test`

2. **AWS CLI connection issues**

   - Verify AWS CLI is installed: `aws --version`
   - Check LocalStack is running: `docker ps | grep localstack`
   - Test connection: `aws --endpoint-url=http://localhost:4566 s3 ls`

3. **FastAPI server issues**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version: `python --version`
   - Verify PYTHONPATH is set: `echo $PYTHONPATH`

### Debug Mode

To see detailed error messages, modify the dev.sh script to remove the `>/dev/null 2>&1` redirection:

```bash
until aws --endpoint-url=http://localhost:4566 s3 ls; do
  echo "Waiting for S3 service..."
  sleep 2
done
```

## 📚 Dependencies

Key dependencies include:

- **FastAPI** - Web framework
- **SQLAlchemy** - Database ORM
- **boto3** - AWS SDK for Python
- **LocalStack** - AWS service emulator
- **uvicorn** - ASGI server

See `requirements.txt` for the complete list.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

[Add your license information here]
