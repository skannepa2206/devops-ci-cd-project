# devops-ci-cd-project
Introduction:
AI-Driven CI/CD Release Automation automates deployments using GitHub Actions, Docker, and AI-powered log analysis. It detects errors with spaCy NLP and auto-rolls back failed releases, ensuring reliability. This project showcases DevOps automation, CI/CD expertise, and AI-driven monitoring for seamless software delivery.

# DevOps CI/CD Pipeline with AI Features

This project demonstrates a modern continuous integration and continuous deployment (CI/CD) pipeline with AI-powered log analysis and automatic rollback mechanisms. It is built with Python, Docker, and GitHub Actions, showcasing a reliable and automated deployment workflow.

## 🌟 Features

- **Automated CI/CD Pipeline**: Continuous integration and deployment using GitHub Actions
- **AI-Powered Log Analysis**: Intelligent analysis of deployment logs to identify issues
- **Automatic Rollback**: Self-healing system that rolls back to previous stable versions on failure
- **Containerized Application**: Flask web application running in Docker containers
- **Test-Driven Deployment**: Automated testing at each stage of the deployment

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Testing**: Pytest
- **Monitoring**: Custom AI log analysis

## 📋 Prerequisites

To run this project, you need:

- Python 3.8 or higher
- Docker and Docker Compose
- Git

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/devops-ci-cd-project.git
cd devops-ci-cd-project
```

### Local Development

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   cd app
   python main.py
   ```

4. Access the application at http://localhost:5000

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t my-app -f docker/Dockerfile .
   ```

2. Run the container:
   ```bash
   docker run -d -p 5000:5000 --name docker-web-1 my-app
   ```

3. Access the application at http://localhost:5000

### Using Docker Compose

1. Start the application:
   ```bash
   docker-compose -f docker/docker-compose.yml up -d
   ```

2. Stop the application:
   ```bash
   docker-compose -f docker/docker-compose.yml down
   ```

## 📊 CI/CD Pipeline

This project uses GitHub Actions for CI/CD. The workflow includes:

1. **Build**: Checkout code, set up Python and Docker, build the Docker image
2. **Test**: Run tests to verify the application works correctly
3. **Deploy**: Deploy the application to the target environment
4. **Monitor**: Analyze logs for potential issues
5. **Rollback**: Automatically roll back to the previous version if issues are detected

## 🧠 AI Log Analysis

The AI log analysis component (`ai_log_analysis/analyze_logs.py`) scans deployment logs to detect issues. It uses regex pattern matching to:

- Extract error and warning messages
- Generate summaries of detected issues
- Provide actionable insights for troubleshooting

## 🔄 Auto-Rollback Mechanism

The rollback script (`rollback/rollback.sh`) automatically:

1. Stops the current deployment
2. Restores the previous stable version
3. Verifies the restored version is functioning correctly

## 📁 Project Structure

```
devops-ci-cd-project/
├── .github/
│   └── workflows/
│       └── release.yml     # GitHub Actions workflow
├── ai_log_analysis/
│   ├── analyze_logs.py     # AI log analysis script
│   └── deployment_logs.txt # Sample logs
├── app/
│   └── main.py             # Flask application
├── docker/
│   ├── Dockerfile          # Docker configuration
│   └── docker-compose.yml  # Docker Compose configuration
├── rollback/
│   └── rollback.sh         # Rollback script
├── tests/
│   └── test_app.py         # Application tests
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 🔧 Troubleshooting

### Common Issues

1. **Flask application isn't accessible:**
   - Make sure Flask is binding to `0.0.0.0` and not `127.0.0.1`
   - Verify the port mapping in Docker (`-p 5000:5000`)

2. **Dependency errors:**
   - Ensure compatible versions in requirements.txt
   - Flask 2.2.3 requires Werkzeug 2.2.3

3. **Docker build fails:**
   - Check if all necessary files are being copied to the container
   - Ensure build dependencies are installed

### Running Tests Manually

```bash
pip install pytest
pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Flask web framework
- Docker containerization
- GitHub Actions for CI/CD
- All open-source contributors who made this project possible

---

Made with ❤️ by Sriram Kannepalli
