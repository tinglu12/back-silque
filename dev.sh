#!/bin/bash

# FastAPI Development Server Script
# Sets PYTHONPATH to include current directory and starts the dev server
# Usage: ./dev.sh [check-s3] [bucket-name]

# Function to check S3 bucket contents
check_s3() {
    local bucket_name=${1:-"clothes-images"}
    local endpoint_url="http://localhost:4566"
    
    echo "🔍 Checking S3 bucket: $bucket_name"
    echo "📍 Endpoint: $endpoint_url"
    echo ""
    
    echo "📦 Bucket contents:"
    aws --endpoint-url=$endpoint_url s3 ls s3://$bucket_name
    
    echo ""
    echo "📊 Detailed info:"
    aws --endpoint-url=$endpoint_url s3api list-objects --bucket $bucket_name --query 'Contents[].{Key:Key,Size:Size,LastModified:LastModified}' --output table
    
    echo ""
    echo "✅ Done!"
}

# Check if user wants to check S3 instead of starting server
if [[ "$1" == "check-s3" ]]; then
    check_s3 "$2"
    exit 0
fi

echo "🚀 Starting FastAPI development server..."
echo "📁 Working directory: $(pwd)"
echo "🔧 Setting PYTHONPATH to include current directory"


CONTAINER_NAME="localstack-test"
BUCKET_NAME="clothes-images"

echo "Stopping and removing any existing LocalStack container..."
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

echo "Removing dangling Docker images to free space..."
docker image prune -f

echo "Starting LocalStack container with only S3 service enabled..."
docker run -d --name $CONTAINER_NAME -p 4566:4566 -e SERVICES=s3 localstack/localstack

echo "Waiting for LocalStack S3 to be ready..."
until aws --endpoint-url=http://localhost:4566 s3 ls >/dev/null 2>&1; do
  echo "Waiting for S3 service..."
  sleep 2
done

echo "Creating bucket '$BUCKET_NAME'..."
aws --endpoint-url=http://localhost:4566 s3 mb s3://$BUCKET_NAME

echo "Setup complete! LocalStack running with bucket '$BUCKET_NAME'."
export PYTHONPATH=.
fastapi dev main.py
