# 🏋️‍♂️ Workout Bot

A Telegram bot for workout assistance. Built with Aiogram 3 and SQLite. The bot includes a multi-step user registration, personalized greetings, and a foundation for exercise selection with proper technique guides.

## 🛠 Tech Stack
* **Python 3**
* **Aiogram 3** — an asynchronous framework for Telegram bots
* **SQLite3** — a built-in database with a table for users

## ✨ Features
* **Multi-step User Registration:** Collects first name, surname, and group/faculty using a Finite State Machine (FSM).
* **Data Confirmation:** Asks the user to confirm their entered data using inline Yes/No buttons before saving to the database.
* **Database Protection:** Uses `PRIMARY KEY` on `user_id` to prevent duplicate registrations and database errors.
* **Dynamic Routing on `/start`:** Shows the registration menu for new users and the main menu for already registered users.
* **Personalized Greeting:** Addresses the user by the name they provided during registration.
* **Exercise Selection:** The main menu contains a button to go to exercise selection (feature in development).

## 📁 Project Structure
* `main.py` — Entry point, bot startup, and database initialization.
* `app/handlers.py` — Handlers for commands, messages, and callback queries.
* `app/database.py` — Database functions (SQL queries for the `users` table).
* `app/keyboards.py` — Reply and inline keyboards.
* `app/states.py` — FSM states for the registration process.
* `config.py` — Configuration file with the bot token and database path.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install aiogram
