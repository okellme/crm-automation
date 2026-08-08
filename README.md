# CRM Automation Tool

A lightweight, terminal-based CRM automation tool built in Python. Designed to reduce manual, repetitive admin work for freelancers and small businesses — automatically tracking leads, flagging overdue follow-ups, and sending automated email reminders.

## Features

- Add and store leads in a persistent SQLite database
- View all saved leads at any time
- Automatically flags leads that haven't been followed up on in 7+ days
- Sends automated follow-up email reminders via Gmail
- Simple menu-driven interface — no need to edit code to use it
- Input validation to prevent bad/empty data
- Graceful error handling for email sending failures

## Tech Stack

- Python 3
- SQLite (built-in `sqlite3` module)
- Gmail SMTP (`smtplib`) for email automation
- `python-dotenv` for secure credential management

## Setup

1. Clone this repository
2. Install dependencies:
