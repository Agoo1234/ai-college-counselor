# Setup Tutorial for the Application

This tutorial will guide you through setting up the environment and configurations needed to run the application.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- MySQL server

## Steps

1. **Set up MySQL Server**
   - Install MySQL Server if you haven't already.
   - Create a new database for the application:
     ```sql
     CREATE DATABASE your_database_name;
     ```
   - Create a new user and grant privileges:
     ```sql
     CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
     GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
     FLUSH PRIVILEGES;
     ```

2. **Clone the Repository**
   - Clone the application repository to your local machine.

3. **Set Up Python Virtual Environment**
   - Navigate to the project directory.
   - Create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS and Linux: `source venv/bin/activate`

4. **Install Dependencies**
   - Install the required Python packages:
     ```
     pip install -r backend/requirements.txt
     ```

5. **Configure Environment Variables**
   - Copy the `.env.example` file to `.env` (if it doesn't exist already).
   - Update the `.env` file with your MySQL credentials:
     ```
     SECRET_KEY=your_secret_key
     MYSQL_DATABASE_URI=mysql+pymysql://your_username:your_password@localhost/your_database_name
     JWT_SECRET_KEY=your_jwt_secret_key
     ```

6. **Initialize the Database**
   - Run the Flask application once to create the database tables:
     ```
     python backend/app.py
     ```
   - You should see output indicating that the tables were created.

7. **Run the Application**
   - Start the backend server:
     ```
     python backend/app.py
     ```
   - The server should now be running on `http://localho.st:5000`.

8. **Set Up the Frontend (if applicable)**
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```
   - Start the frontend development server:
     ```
     npm start
     ```
   - The frontend should now be accessible at `http://localhost:3000`.

## Troubleshooting

- If you encounter any database connection issues, double-check your MySQL credentials in the `.env` file.
- Make sure all required ports (5000 for backend, 3000 for frontend) are available and not being used by other applications.
- If you face any package-related issues, ensure that you're using the correct versions as specified in `requirements.txt`.
