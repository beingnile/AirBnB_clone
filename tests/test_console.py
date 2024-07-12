#!/usr/bin/python3
"""Defines testcases for console.py"""
import json
import os
import unittest
from console import HBNBCommand
from models import storage
from io import StringIO
from unittest.mock import patch


classes = ['BaseModel', 'User', 'Amenity', 'City', 'Place', 'Review', 'State']


class TestHBNBCommand(unittest.TestCase):
    """Testcases for the HBNBCommand class"""
    def setUp(self):
        """Sets up test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.all().clear()

    def tearDown(self):
        """Tears down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.all().clear()

    def test_quit(self):
        """Tests quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Tests EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """Tests empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue().strip(), '')

    def test_help(self):
        """Tests help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            test_str = (
                "Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  create  destroy  help  quit  show  update"
            )
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue().strip(), test_str)

    def test_create_missing_class(self):
        """Tests create command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Tests create command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """Tests create command with valid class"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                self.assertTrue(len(mod_id) > 0)
                key = f"{model}.{mod_id}"
                self.assertIn(key, storage.all())

    def test_show_missing_class(self):
        """Tests show command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Tests show command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show InvalidClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Tests show command with missing id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show {model}")
                self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        """Tests show command with invalid id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show {model} 1234")
                self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_valid(self):
        """Tests show command with valid class and id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"show {model} {mod_id}")
                    self.assertIn(f"[{model}] ({mod_id})", f.getvalue().strip())

    def test_destroy_missing_class(self):
        """Tests destroy command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Tests destroy command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Tests destroy command with missing id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"destroy {model}")
                self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Tests destroy command with invalid id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"destroy {model} 1234")
                self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_valid(self):
        """Tests destroy command with valid class and id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"destroy {model} {mod_id}")
                    self.assertEqual(f.getvalue().strip(), "")
                    self.assertNotIn(f"{model}.{mod_id}", storage.all())

    def test_all_no_class(self):
        """Tests all command with no class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertIn("User", output)

    def test_all_valid_class(self):
        """Tests all command with valid class"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                HBNBCommand().onecmd(f"all {model}")
                output = f.getvalue().strip()
                self.assertIn(f"{model}", output)

    def test_all_invalid_class(self):
        """Tests all command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_class(self):
        """Tests update command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        """Tests update command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update InvalidClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Tests update command with missing id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"update {model}")
                self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        """Tests update command with invalid id"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"update {model} 1234")
                self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute(self):
        """Tests update command with missing attribute"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"update {model} {mod_id}")
                    f_str = "** attribute name missing **"
                    self.assertEqual(f.getvalue().strip(), f_str)

    def test_update_missing_value(self):
        """Tests update command with missing value"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"update {model} {mod_id} attr")
                    self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_valid(self):
        """Tests update command with valid class, id, attribute and value"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"update {model} {mod_id} attr test")
                    self.assertEqual(f.getvalue().strip(), "")
                    mod = storage.all()[f"{model}.{mod_id}"]
                    self.assertEqual(mod.attr, "test")

    def test_count_command(self):
        """Tests count command for a valid class"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"{model}.count()")
                    output = f.getvalue().strip()
                    self.assertEqual(output, "1")

    def test_show_command_with_dot_notation(self):
        """Tests show command with dot notation"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f'{model}.show("{mod_id}")')
                    self.assertIn(f"[{model}] ({mod_id})", f.getvalue().strip())

    def test_destroy_command_with_dot_notation(self):
        """Tests destroy command with dot notation"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f'{model}.destroy("{mod_id}")')
                    self.assertEqual(f.getvalue().strip(), "")
                    self.assertNotIn(f"{model}.{mod_id}", storage.all())

    def test_all_command_with_dot_notation(self):
        """Tests all command with dot notation"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"{model}.all()")
                    self.assertIn(f"{model}", f.getvalue().strip())

    def test_update_command_with_dot_notation(self):
        """Tests update command with dot notation"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    f_str = f'{model}.update("{mod_id}", "attr", "test")'
                    HBNBCommand().onecmd(f_str)
                    self.assertEqual(f.getvalue().strip(), "")
                    mod = storage.all()[f"{model}.{mod_id}"]
                    self.assertEqual(mod.attr, "test")

    def test_update_command_with_dict_dot_notation(self):
        """Tests update command with dictionary and dot notation"""
        for model in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {model}")
                mod_id = f.getvalue().strip()
                with patch('sys.stdout', new=StringIO()) as f:
                    s = f'{model}.update("{mod_id}", {{"attr1": "test", "attr": "t2"}})'
                    HBNBCommand().onecmd(s)
                    self.assertEqual(f.getvalue().strip(), "")
                    mod = storage.all()[f"{model}.{mod_id}"]
                    self.assertEqual(mod.attr1, "test")
                    self.assertEqual(mod.attr, "t2")


if __name__ == '__main__':
    unittest.main()
