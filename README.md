# 🏋️‍♂️ Workout Bot (Gym Helper)

A Telegram bot for workout assistance. Built with Aiogram 3 and SQLite. The bot features a multi-step user registration, user settings, and an interactive exercise guide with proper technique descriptions for different muscle groups.

## 🛠 Tech Stack
* **Python 3**
* **Aiogram 3** — an asynchronous framework for Telegram bots
* **SQLite3** — a built-in database for storing user profiles

## ✨ Features
* **Multi-step User Registration:** Collects first name, surname, and study group using a Finite State Machine (FSM) with a data confirmation step (Yes/No inline buttons).
* **User Settings & Privacy:** Users can completely delete their profile from the database via the settings menu (with a confirmation step) to start fresh.
* **Interactive Exercise Guide:** 
  * Browse exercises by muscle groups (Arms, Legs, Back, Chest) using inline buttons.
  * View detailed technique descriptions for the 5 most popular exercises per muscle group.
  * Formatted with HTML for better readability.
  * Includes a "Return" button to easily navigate back to the muscle group selection.
* **Database Protection:** Uses `PRIMARY KEY` on `user_id` to prevent duplicate registrations.
* **Dynamic Routing:** Smart `/start` command that shows the registration menu for new users and the main menu for returning users.

## 📁 Project Structure
* `main.py` — Entry point, bot startup, and database initialization.
* `app/handlers.py` — Handlers for commands, messages, and callback queries.
* `app/database.py` — Database functions (SQL queries for user management).
* `app/keyboards.py` — Reply and inline keyboards.
* `app/states.py` — FSM states for the registration and deletion processes.
* `assets/exercise_data.py` — Dictionary containing all exercise texts and techniques.
* `assets/config.py` — Configuration file with the bot token and database path.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install aiogram
