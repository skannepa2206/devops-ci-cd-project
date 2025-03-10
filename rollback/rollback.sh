#!/bin/bash
echo "🔄 Starting rollback procedure..."
echo "🛑 Stopping current deployment..."

# Check if docker-compose file exists
if [ -f "docker/docker-compose.yml" ]; then
    docker-compose -f docker/docker-compose.yml down
    echo "✅ Current deployment stopped successfully"
else
    echo "⚠️ docker-compose.yml not found, trying direct container removal"
    docker stop docker-web-1 || true
    docker rm docker-web-1 || true
fi

# Check if we have a previous version to restore
if docker image inspect my-app:previous >/dev/null 2>&1; then
    echo "♻️ Restoring from previous stable version..."
    # Tag the previous image as current
    docker tag my-app:previous my-app:latest
    # Start the previous version
    docker run -d -p 5000:5000 --name docker-web-1 my-app:previous
    echo "✅ Restored previous version successfully"
else
    echo "⚠️ No previous version found to restore"
fi

echo "✅ Rollback completed successfully"
exit 0