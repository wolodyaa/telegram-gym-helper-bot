# 🏋️‍♂️ Workout Bot

A Telegram bot for workout assistance. Bot, built with Aiogram 3 and SQLite. The bot includes user registration, personalized greetings, and a foundation for exercise selection with proper technique guides.

## 🛠 Tech Stack

* **Python 3**
* **Aiogram 3** — an asynchronous framework for Telegram bots
* **SQLite3** — a built-in database with a table for users

## ✨ Features

* **User registration** — saves users to the `users` table for personalized greetings and tracking registration status.
* **Dynamic routing on `/start`** — shows the registration menu for new users and the main menu for already registered users.
* **Personalized greeting** — addresses the user by the name they provided during registration.
* **Exercise selection** — the main menu contains a button to go to exercise selection (feature in development).
* **Protection against duplicate registration** — the bot prevents the same user from registering twice.

## 📁 Project Structure

* `main.py` — entry point, bot startup, and database initialization.
* `app/handlers.py` — handlers for commands, messages, and callback queries.
* `app/database.py` — database functions (SQL queries for the `users` table).
* `app/keyboards.py` — reply keyboards.
* `app/states.py` — FSM states for registration.
* `config.py` — configuration file with the bot token and database path.

## ⚙️ How to Run Locally

1. Clone the repository.

2. Install dependencies:

   ```bash
   pip install aiogram
