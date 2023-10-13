# Banking Software Lifecycle

Welcome to the repository for the IE Bank Corp's bank account management system. This project was developed as a part of the 'Software Development and DevOps' class. It showcases the development and deployment of a bank account management system with new features and addresses the technical debt present in the initial version.

## Note on Documentation

This README provides an overview of the project, its components, and setup instructions. For a detailed Software Requirements Specification (SRS), please refer to the [GitHub Wiki](https://github.com/gabrieldeolaguibel/Banking-Software-Lifecycle/wiki).

## Project Overview

The bank account management system consists of four main components:
1. **IE Bank Website (Frontend)**: Provides the user interface for bank account management.
2. **IE Bank API (Backend)**: Handles the business logic and interacts with the database.
3. **PostgreSQL Database**: Stores bank account data.
4. **Infrastructure Code**: Contains the configurations and scripts to set up and manage the cloud resources required for the application.

### Interactions

#### Frontend to Backend
- `/accounts` (HTTP_GET) -> `/accounts, GET`
- `/accounts` (HTTP_GET) -> `/accounts/[account_id], GET`
- `/accounts` (HTTP_DELETE) -> `/accounts/[account_id], PUT`

#### Backend to Database
- `/accounts, GET` -> `db_read` -> PostgreSQL
- `/accounts, POST` -> `db_add` -> PostgreSQL
- `/accounts/[account_id], GET` -> `db_read` -> PostgreSQL
- `/accounts/[account_id], PUT` -> `db_update` -> PostgreSQL
- `/accounts/[account_id], DELETE` -> `db_Delete` -> PostgreSQL

## Getting Started

### Prerequisites

Ensure you have the following installed and set up:
- Git
- Node.js
- Python
- Flask
- SQLAlchemy
- SQLite
- Visual Studio Code
- GitHub
- Azure subscription
- Azure Service Principal

### Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/gabrieldeolaguibel/Banking-Software-Lifecycle.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Banking-Software-Lifecycle
   ```

3. **Set Up the Backend**:
   - Navigate to the backend directory: `cd ie-bank-be`
   - Install the required Python packages: `pip install -r requirements.txt`
   - Run the Flask application: `flask run`

4. **Set Up the Frontend**:
   - Navigate to the frontend directory: `cd ie-bank-fe`
   - Install the required Node packages: `npm install`
   - Start the frontend application: `npm start`

5. **Deploy the Infrastructure**:
   - Navigate to the infrastructure directory: `cd ie-bank-infra`
   - Deploy the infrastructure using the provided scripts.

6. **Access the Application**: Open a web browser and navigate to `http://localhost:8080` to access the IE Bank website.

## Features and Enhancements

- **Homepage**: A new homepage has been added to the web application.
- **Country Field for Accounts**: Users can now submit the account country when creating a new account.
- **Unit and Functional Tests**: Tests have been written for the backend API to ensure its functionality.
- **GitHub Flow**: A branch-based workflow strategy has been implemented.
- **Azure Application Insights**: Monitoring capabilities have been added to the application.
- **UAT Environment**: A User Acceptance Testing environment has been set up to test the application before production release.

## Contributors

- Gabriel De Olaguibel

## License

This project is licensed under the MIT License.

