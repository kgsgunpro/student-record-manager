# Student Record Manager

A simple Python console application to manage student records.

## Features

- Add a student
- Automatically assign a unique ID
- Search student details by ID
- Handle invalid menu input
- Handle non-existing student IDs

## Project Structure

```
main.py
```

## How It Works

Students are stored in a dictionary:

```python
{
    1: {"name": "Ravi", "grade": "10"},
    2: {"name": "Ram", "grade": "9"}
}
```

Each new student receives an auto-incremented ID.

## Running the Project

Make sure Python is installed.

Run:

```bash
python main.py
```

## Menu

```text
Main menu
1. Add student
2. Fetch student details
Any other number -> Exit
```

## Example

```text
Main menu
1.press 1 to add student
2.press 2 to fetch details of student
press any number to exit

1

Enter student name : Ravi
Enter grade : 10

the following details added to database
id: 1 , name: Ravi , grade :10
```

Search by ID:

```text
2

Enter student id : 1

id: 1 , name: Ravi , grade :10
```

## Error Handling

### Invalid menu input

```text
abc

please enter integer
```

### Student ID not found

```text
Enter student id : 100

id doesn't exist
```

## Current Version

### v1
- Student manager class created
- Add student functionality

### v2
- Search student by ID
- Improved input validation
- Better exception handling

## Future Improvements

- Update student details
- Delete student
- Display all students
- Save records to a file
- Load records from a file
- Store data using JSON
