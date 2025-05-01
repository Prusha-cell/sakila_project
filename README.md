# 🎮 Console-Based Movie Search Application (Powered by Sakila Database)

## 📌 Project Description

This is a console-based Python application for interactive movie search using the **Sakila** database. It supports searching by keywords, genre, and release year, while also storing search history and displaying the most popular search queries.

The database is deployed on the following server:  
`group_111124_fp_{Vadym_Prudnikov}`

---

## 📚 Table of Contents

1. [Project Description](#-project-description)  
2. [Stage 1 — Studying the Database Structure](#stage-1--studying-the-database-structure)  
3. [Stage 2 — Developing SQL Queries](#stage-2--developing-sql-queries)  
4. [Stage 3 — Building the Console Application](#stage-3--building-the-console-application)  
5. [Installation and Launch](#-installation-and-launch)  
6. [Available Commands](#-available-commands)  
7. [Code Quality and Testing](#-code-quality-and-testing)  
8. [Author](#-author)  

---

## Stage 1 — Studying the Database Structure

- Established a connection to the Sakila database.  
- Analyzed key tables: `film`, `category`, `language`, `film_category`, `inventory`, `rental`, and their relationships.  
- Gained an understanding of how to retrieve movie titles, genres, release dates, and related metadata.

---

## Stage 2 — Developing SQL Queries

- Implemented SQL queries for:
  - Searching for movies by keyword in the title.
  - Searching by genre and release year.
  - Logging each search query to the `popular_queries` table with type, parameters, and timestamp.
  - Retrieving the most frequent query types:

```sql
SELECT search_type, COUNT(*) AS cnt
FROM popular_queries
GROUP BY search_type
ORDER BY cnt DESC;
```

- All queries include filtering and result limits (10+ items).  
- Handles cases where no results are found (returns an empty list without errors).

---

## Stage 3 — Building the Console Application

- The application is launched via the `main.py` file and operates in interactive mode.
- Supported commands:

  1. **Search by keyword:**
     - Input: `search keyword <your_keyword>`
     - Searches for movies where the keyword appears in the title (case-insensitive).
     - Returns at least 10 relevant results.

  2. **Search by genre and year:**
     - Input: `search genre <genre> <year>`
     - Finds movies of a specified genre released in the given year.

  3. **Show popular queries:**
     - Input: `popular`
     - Displays the most frequently used search types.

  4. **Exit the program:**
     - Input: `exit`

- Includes error handling for database connection loss, invalid input, and empty search results.
- The app remains active after each command, waiting for the next user input.

---

## ⚙️ Installation and Launch

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/sakila_project.git
cd sakila_project
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure database connection

Create a `.env` file or define the parameters in `config.py`:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=sakila
DB_USER=your_user
DB_PASSWORD=your_password
```

### 4. Run the application:

```bash
python main.py
```

---

## 💻 Available Commands

| Command                          | Description                                                 |
|----------------------------------|-------------------------------------------------------------|
| `search keyword <word>`          | Searches for movies with the given keyword in the title.    |
| `search genre <genre> <year>`    | Searches for movies by genre and release year.              |
| `popular`                        | Displays the most popular search query types.               |
| `exit`                           | Exits the application.                                      |

---

## 🧹 Code Quality and Testing

- The code adheres to [PEP 8](https://peps.python.org/pep-0008/) standards.
- Key functions are well-commented.
- All edge cases are handled, including invalid input and no results.
- This README includes full documentation on setup, usage, and functionality.

---

## 📝 Author

**Vadym Prudnikov**  
An educational project developed as part of learning SQL, Python, and the fundamentals of manual/automated testing.

