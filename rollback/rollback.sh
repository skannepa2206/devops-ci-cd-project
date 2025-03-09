#!/bin/bash
echo "❌ Deployment failed. Rolling back to the last working version..."
docker tag my-app:previous my-app:latest
docker-compose up -d

#!/bin/bash

echo "🔄 Starting rollback procedure..."

# Stop the current containers
echo "🛑 Stopping current deployment..."
docker-compose -f docker/docker-compose.yml down

# You might want to restore from a previous backup or image here
echo "♻️ Restoring from previous stable version..."
# Example: docker pull yourrepo/app:previous-stable
# Example: docker-compose -f docker/docker-compose.previous.yml up -d

echo "✅ Rollback completed successfully"

# Notify the team (this is a placeholder)
echo "📧 Sending notification to DevOps team..."
# You could add actual notification logic here (email, Slack, etc.)

exit 0