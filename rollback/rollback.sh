#!/bin/bash
echo "❌ Deployment failed. Rolling back to the last working version..."
docker tag my-app:previous my-app:latest
docker-compose up -d