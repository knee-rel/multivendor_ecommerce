# Django Project Setup

## Overview

This repository contains a Django project that serves as a template for building web applications. Follow the instructions below to set up the project on your local machine.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python** (version 3.6 or higher)
- **pip** (Python package installer)
- **virtualenv** (optional but recommended)

You can check if Python and pip are installed by running:

```bash
python --version
pip --version
```

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create a Virtual Environment

It’s recommended to create a virtual environment to manage dependencies:

```bash
python -m venv env  # Replace 'env' with your preferred environment name
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

- On macOS and Linux:
  ```bash
  source env/bin/activate
  ```

- On Windows:
  ```bash
  .\env\Scripts\activate
  ```

### 4. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root of your project and add your environment variables. Here’s an example of what you might include:

```
DEBUG=True
SECRET_KEY='your_secret_key'
DATABASE_URL='sqlite:///db.sqlite3'  # Adjust based on your database configuration
```

### 6. Apply Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

If you want to access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser credentials.

### 8. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You can now access your application at `http://127.0.0.1:8000/`.
