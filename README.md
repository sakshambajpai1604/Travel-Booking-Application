# Travel Booking Application

## Local Setup Instructions

### Prerequisites
- Python 3.10+
- MySQL Server
- pip (Python package manager)

### 1. Clone the repository
```bash
git clone https://github.com/sakshambajpai1604/Travel-Booking-Application.git
cd Travel-Booking-Application
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# Or
source venv/bin/activate   # On Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL
- Create a MySQL database named `travel_booking_db`.
- Create a `.env` file in the project root with your DB credentials:
  ```
  SECRET_KEY=your-django-secret-key
  DB_NAME=travel_booking_db
  DB_USER=your_mysql_user
  DB_PASSWORD=your_mysql_password
  DB_HOST=localhost
  DB_PORT=3306
  ```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

### 8. Access the app
- Open [http://localhost:8000](http://localhost:8000) in your browser.

---

**Note:**  
- To run tests: `python manage.py test core`
- To access the admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)
