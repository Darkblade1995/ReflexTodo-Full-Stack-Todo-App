# 📝 ReflexTodo – Full-Stack Todo App

**Author:** Luis Fernando Agamez Atehortua  
**Role:** Software Engineer  

---

## 🧠 Description

**ReflexTodo** is a full-stack task management application built with **Reflex (Python)** that demonstrates clean state management, database interaction, and reactive UI updates.

The app allows users to create, complete, and delete tasks in real time, with persistent storage and robust error handling to prevent server crashes.

---

## ✨ Features

- Create tasks with title and optional description
- Mark tasks as completed / uncompleted
- Delete tasks
- Persistent database storage
- Automatic UI refresh after every action
- Dark mode UI
- Defensive error handling to avoid server failures

---

## 🏗 Architecture Overview

### State Management
- Centralized state using `rx.State`
- Reactive updates across the UI
- Controlled inputs for form handling

### Backend
- Database session management with `rx.session()`
- ORM-based `Todo` model
- Safe transactions with exception handling

### Frontend
- Component-based UI
- Conditional rendering
- Responsive layout with clean spacing

---

## 📂 Project Structure

/app
│── models.py # Todo ORM model
│── state.py # TodoState logic
│── pages.py # UI components
│── app.py # App initialization

yaml
Copy code

---

## 🧩 Technologies Used

- Python
- Reflex (Full-stack reactive framework)
- SQLAlchemy (via Reflex ORM)
- Type hints (`typing`)
- Dark UI theme

---

## ▶️ How It Works

1. Tasks are loaded from the database on page load.
2. New tasks are validated before being saved.
3. Each interaction:
   - Updates the database
   - Refreshes the state
   - Automatically re-renders the UI
4. Errors are handled gracefully with alerts instead of crashes.

---

## 🚀 How to Run

```bash
reflex run
Then open your browser at:

arduino
Copy code
http://localhost:3000
⚠️ Notes
Title field is required

Description is optional

Designed to be easily extendable

Safe for production-style patterns

🔮 Possible Improvements
Edit task functionality

Task filtering (completed / pending)

Authentication

API integration

Deployment (Vercel / Fly.io)

📜 License
Free to use, modify, and distribute.

A clean, reactive, full-stack task manager built entirely in Python.



