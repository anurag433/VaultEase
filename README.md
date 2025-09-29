# 🏦 Bank Management System API

A comprehensive Bank Management System API built with **Django REST Framework (DRF)** that allows users to register as customers, manage their accounts, and perform transactions securely using **JWT authentication**.

---

## ✨ Features

### 🔐 **Authentication**
- **JWT-based Authentication** using `djangorestframework-simplejwt`
- Customer Registration and Login
- Secure token-based API access

### 💳 **Account Management**
- ✅ **Create Accounts**: Customers can create multiple bank accounts
- 👁️ **View Accounts**: Customers can view their own accounts
- 💰 **Balance Tracking**: Monitor account balances

### 💸 **Transactions**
- 📥 **Deposit Funds**: Add money to your account
- 📤 **Withdraw Funds**: Withdraw money from your account
- 🔄 **Transfer Funds**: Transfer money between your accounts
---

## Tech Stack

![Django](https://img.shields.io/badge/DJANGO-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/DJANGO%20REST-FF0000?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jwt&logoColor=white)

---

## Tools Used

![Postman](https://img.shields.io/badge/POSTMAN-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![VS Code](https://img.shields.io/badge/VISUAL%20STUDIO%20CODE-0078d7?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## 🚀 Setup and Installation Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bank-management-api.git
cd bank-management-api
```
### **2. Create Virtual Environment**
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Database Setup**
```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### **5. Create Superuser (Admin)**
```bash
python manage.py createsuperuser
```

### **6. Run Development Server**
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📖 API Documentation

### **Base URL**
```
http://127.0.0.1:8000/
```

### **Authentication Endpoints**

#### **User Registration**
```http
POST /register/
Content-Type: application/json

{
    "username": "This field is required.",
    "first_name": "This field is required.",
    "last_name": "This field is required.",
    "email": "This field is required.",
    "password": "This field is required."
}

```

**Response:**
```json
{
    "message": "Account Created Successfully",
    "Your Account No.": "<Account No.>" ,
    "access": "<access_token>",
    "refresh": "<refresh_token>"
}
```

### **Bank Management Endpoints**

#### **Customer Login**
```http
POST /api/token/
Content-Type: application/json
{
    "username": "your_username",
    "password": "your_password"
}

```

**Response:**
```json
{
    "access": "<access_token>",
    "refresh": "<refresh_token>"
}
```

#### **User Dashboard**
```http
GET /dashboard/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "account_id": 9,
    "username": "<username>",
    "first_name": "<first_name>",
    "last_name": "<last_name>",
    "email": "<email>",
    "current_balance": "<amount>"
}

```

#### **Deposit**
```http
POST /deposit/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "amount": 500
}

```
#### **Withdrawl**
```http
POST /withdrawl/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "amount": 500
}

```

#### **Transfer**
```http
POST /transfer/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "from_account": "<your account no.>",
    "to_account": "<other account no.>",
    "amount": 300
}

```
### **HTTP Status Codes**
- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error



## 🔮 Future Enhancements

- Multi-currency accounts
- Email/SMS transaction notifications
- Mobile/web frontend integration
- Account statements & reporting

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Anurag Singh**
- GitHub: [@anurag433](https://github.com/anurag433)
- Project Link: [VaultEase](https://github.com/anurag433/VaultEase)



⭐ **Star this repository if you found it helpful!**



