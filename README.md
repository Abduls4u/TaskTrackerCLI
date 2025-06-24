
# 📝 Task Tracker CLI

A simple, Python-based command-line task tracker that allows you to add, list, update, delete, and manage the status of your tasks. Tasks are stored in a local JSON file, making the app lightweight and easy to use offline.

---

## 🚀 Features

- Add new tasks with descriptions
- View all tasks or filter by status (`todo`, `inprogress`, `done`)
- Update task descriptions
- Mark tasks as in-progress or done
- Delete tasks by ID
- All task data stored locally in `tasks.json`
- Timestamps for creation and last update

---

## 🛠️ Technologies Used

- Python 3
- Standard libraries: `os`, `sys`, `json`, `datetime`

---

## 📂 Project Structure

```

taskTracker.py
tasks.json         # Created after first task is added
README.md

````

---

## 📦 Installation

1. Make sure you have Python 3 installed:
   ```bash
   python3 --version
````

2. Clone this repository or download the `taskTracker.py` script:

   ```bash
   git clone https://github.com/Abduls4u/TaskTrackerCLI.git
   cd TaskTrackerCLI
   ```

3. Make the script executable (optional):

   ```bash
   chmod +x taskTracker.py
   ```

4. Run the script using:

   ```bash
   ./taskTracker.py <command>
   # or
   python3 taskTracker.py <command>
   ```

---

## 🧑‍💻 Usage

### ➕ Add a Task

```bash
python3 taskTracker.py Add "Buy groceries"
```

### 📋 List All Tasks

```bash
python3 taskTracker.py List
```

### ✅ Mark a Task as Done

```bash
python3 taskTracker.py Mark-done <task_id>
```

### 🔄 Mark a Task as In Progress

```bash
python3 taskTracker.py Mark-in-progress <task_id>
```

### ✏️ Update Task Description

```bash
python3 taskTracker.py Update <task_id> "New description here"
```

### ❌ Delete a Task

```bash
python3 taskTracker.py Delete <task_id>
```

### 🧾 Filtered Views

```bash
python3 taskTracker.py List-todo
python3 taskTracker.py List-inprogress
python3 taskTracker.py List-done
```

---

## 📝 Task Structure

Each task is stored in `tasks.json` as:

```json
{
  "id": 1,
  "description": "Sample task",
  "status": "todo",
  "createdAt": "2024-06-24 15:42",
  "updatedAt": "2024-06-24 15:42"
}
```

---

## ⚠️ Known Limitations

* No command-line argument parser (like `argparse` or `click`) used yet.
* The app does not support multi-user or concurrent editing.
* Basic error handling — could be expanded.
* Status must be one of: `todo`, `inprogress`, `done`.

---

## 🧪 Future Improvements

* Use `argparse` for cleaner argument handling
* Add support for task priorities and deadlines
* Include color-coded output for better readability
* Add unit tests
* Export tasks to CSV or Markdown

---

## 👨‍💻 Author

**Abdulsomad Abdulsalam**

Feel free to contribute, fork, or suggest improvements!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## Project Link From Roadmap.sh
This is the projects link on roadmap.sh (https://roadmap.sh/projects/task-tracker)

```
