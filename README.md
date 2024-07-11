# AirBnB Clone

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting started](#getting-started)
  - [File Structure](#file-structure)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Available Commands](#available-commands)
    - [Example Usage](#example-usage)
- [Authors](#authors)

## Introduction
This project is a simplified version of the AirBnB web application. Some features are not included.  
However, the basic functionalities are implemented.The project includes a command interpreter for managing the application data, a storage system to persist the data, and various models representing the data structures used in the application.

## Features
- Create, retrieve, update, and delete operations on app data through a console.
- Storage system to persist data using JSON files.
- Models representing Users, Places, Cities, States, Amenities, and Reviews.
- Automated unittests for various components of the application.

## Getting started
For this project, you'll need the following dependencies
- git
- python3

### File Structure
```md
.
├── AUTHORS
├── README.md
├── console.py
├── hack
│   └── generate-authors.sh
├── models
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── tests
    ├── __init__.py
    ├── test_console.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/beingnile/AirBnB_clone.git
```
2. Navigate to the project directory:
```bash
cd AirBnB_clone
```

### Usage
The console can be used to interact with the application data.  
Start the console with:

```bash
./console.py
```
You should see a prompt screen:
```
(hbnb) 
```

#### Available Commands
- `create <classname>`: Creates a new instance of the specified class.  
- `show <classname> <id>` or `<classname>.show(<id>)`: Prints the string representation of an instance based on the class name and id.  
- `destroy <classname> <id>` or `<classname>.destroy(<id>)`: Deletes an instance based on the class name and id.  
- `all <classname>` or `<classname>.all()`: Shows all instances of the specified class. If no class is specified, shows all instances.  
- `update <classname> <id> <attribute_name> <attribute_value>` or `<classname>.update(<id>, <attribute_name>, <attribute_value>)`: Updates an instance based on the class name and id by adding or updating an attribute.  
For the dot notation in `update`, You can have a dictionary of `{<attribute_name>: <attribute_value>}`.  
- `<classname>.count()`: Prints the number of instances of the specified class.  
- `quit` or `EOF`(CTRL+D): Exits the command interpreter.  


#### Example Usage
```bash
beingnile@Beingnile:~/AirBnB_clone$ ./console.py
(hbnb) all
[]
(hbnb) create User
0e5a91f8-cb08-4525-94ac-5b76a9c2862c
(hbnb) all
["[User] (0e5a91f8-cb08-4525-94ac-5b76a9c2862c) {'id': '0e5a91f8-cb08-4525-94ac-5b76a9c2862c', 'created_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457057), 'updated_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457082)}"]
(hbnb) create Amenity
476b7c08-5b03-4c2c-98ed-9628ab6ae07a
(hbnb) all
["[User] (0e5a91f8-cb08-4525-94ac-5b76a9c2862c) {'id': '0e5a91f8-cb08-4525-94ac-5b76a9c2862c', 'created_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457057), 'updated_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457082)}", "[Amenity] (476b7c08-5b03-4c2c-98ed-9628ab6ae07a) {'id': '476b7c08-5b03-4c2c-98ed-9628ab6ae07a', 'created_at': datetime.datetime(2024, 7, 11, 23, 53, 57, 516192), 'updated_at': datetime.datetime(2024, 7, 11, 23, 53, 57, 516213)}"]
(hbnb) all User
["[User] (0e5a91f8-cb08-4525-94ac-5b76a9c2862c) {'id': '0e5a91f8-cb08-4525-94ac-5b76a9c2862c', 'created_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457057), 'updated_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457082)}"]
(hbnb) all Amenity
["[Amenity] (476b7c08-5b03-4c2c-98ed-9628ab6ae07a) {'id': '476b7c08-5b03-4c2c-98ed-9628ab6ae07a', 'created_at': datetime.datetime(2024, 7, 11, 23, 53, 57, 516192), 'updated_at': datetime.datetime(2024, 7, 11, 23, 53, 57, 516213)}"]
(hbnb) User.update("0e5a91f8-cb08-4525-94ac-5b76a9c2862c", "password", "root")
(hbnb) User.show("0e5a91f8-cb08-4525-94ac-5b76a9c2862c")
[User] (0e5a91f8-cb08-4525-94ac-5b76a9c2862c) {'id': '0e5a91f8-cb08-4525-94ac-5b76a9c2862c', 'created_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457057), 'updated_at': datetime.datetime(2024, 7, 11, 23, 55, 20, 157956), 'password': 'root'}
(hbnb) User.count()
1
(hbnb) create User
062a755b-e93b-4696-8d45-c588a300ed54
(hbnb) User.count()
2
(hbnb) User.all()
["[User] (0e5a91f8-cb08-4525-94ac-5b76a9c2862c) {'id': '0e5a91f8-cb08-4525-94ac-5b76a9c2862c', 'created_at': datetime.datetime(2024, 7, 11, 23, 53, 35, 457057), 'updated_at': datetime.datetime(2024, 7, 11, 23, 55, 20, 157956), 'password': 'root'}", "[User] (062a755b-e93b-4696-8d45-c588a300ed54) {'id': '062a755b-e93b-4696-8d45-c588a300ed54', 'created_at': datetime.datetime(2024, 7, 11, 23, 56, 4, 959335), 'updated_at': datetime.datetime(2024, 7, 11, 23, 56, 4, 959352)}"]
(hbnb) Amenity.destroy("476b7c08-5b03-4c2c-98ed-9628ab6ae07a")
(hbnb) Amenity.all()
[]
(hbnb) quit
beingnile@Beingnile:~/AirBnB_clone$
```

## Authors

Nile Okomo - [beingnile](https://github.com/beingnile) 
