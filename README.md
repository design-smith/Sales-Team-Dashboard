---

# Sales Monitoring System

## Overview
This Sales Monitoring System is a comprehensive web application designed to help businesses monitor and manage sales data efficiently. It allows sales managers to track team performance, manage customer relationships, handle invoices, and analyze sales through various data visualizations.

## Features
- **Dashboard**: Provides a summary of key sales metrics and performance indicators.
- **Team Management**: Manage sales team members, including adding new members, editing profiles, and assigning roles.
- **Customer Management**: Keep track of customer information and manage customer relationships.
- **Invoices**: Generate and review invoices for transactions.
- **Sales Analytics**: Visualize sales data through bar charts, pie charts, and line graphs.
- **Secure Authentication**: Login and registration system to ensure secure access to the application.
- **Responsive Design**: The interface is fully responsive and supports various devices and screen sizes.

## Technologies
- **Frontend**: React.js, Material-UI, Nivo for data visualization.
- **Backend**: Django REST Framework for handling API services.
- **Database**: PostgreSQL.
- **Authentication**: JWT (JSON Web Tokens) for secure authentication and session management.

## Installation

### Prerequisites
- Node.js
- Python 3.8 or higher
- PostgreSQL

### Setting Up the Project

1. **Clone the repository**
   ```bash
   git clone {link}
   cd your-project-repo
   ```

2. **Setup the backend**

   Navigate to the backend directory:
   ```bash
   cd backend
   ```

   Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Set up the database:
   ```bash
   createdb sales_tool
   psql -U postgres -d sales_tool -f path/to/SalesTool.sql
   ```

   Start the Django server:
   ```bash
   python manage.py runserver
   ```

3. **Setup the frontend**

   Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

   Install dependencies:
   ```bash
   npm install
   ```

   Start the React development server:
   ```bash
   npm start
   ```

   This will run the frontend on `http://localhost:3000`.

## Usage
After starting both the backend and frontend servers, navigate to `http://localhost:3000` in your browser to access the application. Log in or register a new account to begin managing your sales data.

## Database Installation
To set up the PostgreSQL database:
- Ensure PostgreSQL is installed and running.
- Use the `createdb` command to create a new database named `sales_tool`.
- Import the database schema and data from the `SalesTool.sql` file using the `psql` command.

---
