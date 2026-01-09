# 🚀 FastAPI – SQLAlchemy Revision

A complete **revision-focused backend project** built using **FastAPI** and **SQLAlchemy**, demonstrating a **clean, modular, and scalable REST API architecture**.

This repository is intended to practice and showcase **industry-level backend structure**, proper separation of concerns, and RESTful API development using Python.

---

## 📌 Project Description

This project implements a **User-based REST API** with a well-structured backend architecture.  
The application is organized into separate modules for database handling, models, schemas, services, routers, and configuration.

> ⚠️ This project does **not include authentication**.  
> The main focus is on **application structure, database integration, and clean code practices**.

---

## 🧠 Concepts & Learnings

- FastAPI application structure
- Modular backend architecture
- SQLAlchemy ORM usage
- SQLite database integration
- Pydantic models for data validation
- API Routers for clean endpoint separation
- Service layer for business logic
- RESTful API design principles

---

## 🗂️ Folder Structure
```bash
app/
│
├── database/
│ └── database.py # Database connection & session management
│
├── models/
│ └── user.py # SQLAlchemy ORM models
│
├── schemas/
│ └── user.py # Pydantic request/response schemas
│
├── services/
│ └── user_service.py # Business logic layer
│
├── routers/
│ └── user.py # User API routes
│
├── config/
│ └── config.py # Application configuration
│
├── main.py # FastAPI application entry point
```


---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **Uvicorn**
- **API Routers**

---

## 🔁 API Functionality

This REST API supports standard CRUD operations for users:

- Create user
- Fetch user details
- Update user information
- Delete user
- Input & output validation using Pydantic
- Clean separation between routes, services, and database logic

---

## ▶️ Running the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nevin100/FastAPI-SQLAlchemy-Revision.git
cd FastAPI-SQLAlchemy-Revision
```
### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### 4️⃣ Start the Development Server
```bash
uvicorn app.main:app --reload
```

## Open API Docs

Swagger UI:
```bash
http://127.0.0.1:8000/docs
```

ReDoc:
```bash
http://127.0.0.1:8000/redoc
```
