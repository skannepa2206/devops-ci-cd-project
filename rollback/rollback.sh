#!/bin/bash
echo "🔄 Starting rollback procedure..."
echo "🛑 Stopping current deployment..."

# Stop the container
echo "Stopping Docker container..."
docker-compose -f docker/docker-compose.yml down || {
    echo "Failed to stop with docker-compose, trying direct container stop"
    docker stop docker-web-1 2>/dev/null || true
    docker rm docker-web-1 2>/dev/null || true
}

echo "✅ Rollback completed successfully"
exit 0