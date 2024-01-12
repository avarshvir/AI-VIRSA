import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()

        # Check if the Person table exists
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Person';")
        table_exists = self.cursor.fetchone()

        # If the table doesn't exist, create it
        if not table_exists:
            table_creation_query = '''
            CREATE TABLE IF NOT EXISTS Person (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                dob TEXT,
                father_name TEXT,
                mother_name TEXT,
                education TEXT,
                health_info TEXT,
                personal_info TEXT,
                social_media_accounts TEXT
            );
            '''
            self.cursor.execute(table_creation_query)
            self.conn.commit()

    def insert_person(self, name, dob, father_name, mother_name, education, health_info, personal_info,
                      social_media_accounts):
        insert_query = '''
        INSERT INTO Person (name, dob, father_name, mother_name, education, health_info, personal_info, social_media_accounts)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        '''
        self.cursor.execute(insert_query, (
            name, dob, father_name, mother_name, education, health_info, personal_info, social_media_accounts))
        self.conn.commit()
        messagebox.showinfo("Success", "Person added successfully!")

    def update_person(self, person_id, name, dob, father_name, mother_name, education, health_info, personal_info,
                      social_media_accounts):
        update_query = '''
        UPDATE Person SET
        name=?, dob=?, father_name=?, mother_name=?, education=?, health_info=?, personal_info=?, social_media_accounts=?
        WHERE id=?;
        '''
        self.cursor.execute(update_query, (
            name, dob, father_name, mother_name, education, health_info, personal_info, social_media_accounts, person_id))
        self.conn.commit()
        messagebox.showinfo("Success", "Person updated successfully!")

    def delete_person(self, person_id):
        delete_query = "DELETE FROM Person WHERE id=?;"
        self.cursor.execute(delete_query, (person_id,))
        self.conn.commit()
        messagebox.showinfo("Success", "Person deleted successfully!")

    def fetch_all_persons(self):
        fetch_query = "SELECT * FROM Person;"
        self.cursor.execute(fetch_query)
        return self.cursor.fetchall()

class ExcelLikeGUI(tk.Tk):
    def __init__(self, database_manager):
        super().__init__()
        self.title("Database Management of VIRSA")
        self.geometry("800x600")

        self.database_manager = database_manager
        self.data_entries = []
        self.persons_added = False  # Initialize to False

        self.create_widgets()

    def create_widgets(self):
        # Labels for column headers
        columns = ["ID", "Name", "Date of Birth", "Father's Name", "Mother's Name", "Education", "Health Info",
                   "Personal Info", "Social Media Accounts"]
        for col_index, col_name in enumerate(columns):
            tk.Label(self, text=col_name, relief=tk.GROOVE, width=15).grid(row=0, column=col_index, sticky=tk.W)

        # Entry widgets for data input
        for row_index in range(1, 11):
            row_entries = []
            for col_index in range(len(columns)):
                entry = tk.Entry(self, width=15)
                entry.grid(row=row_index, column=col_index)
                row_entries.append(entry)

            # Bind right-click event to the entire row
            self.bind_row_context_menu(row_entries)

            self.data_entries.append(row_entries)

        # Buttons for actions
        tk.Button(self, text="Add Person", command=self.add_person).grid(row=11, column=0, pady=10)
        tk.Button(self, text="Fetch All Persons", command=self.fetch_all_persons).grid(row=11, column=1, pady=10)

        # Search entry and button
        self.search_entry = tk.Entry(self, width=15)
        self.search_entry.grid(row=11, column=2)
        tk.Button(self, text="Search", command=self.search_person).grid(row=11, column=3, pady=10)

        # Treeview for displaying existing data
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=5)
        for col_name in columns:
            self.tree.heading(col_name, text=col_name)
            self.tree.column(col_name, width=80)
        self.tree.grid(row=12, column=0, columnspan=9, pady=10)

        # Bind double-click event to update a person
        self.tree.bind("<Double-1>", self.update_person_from_treeview)

        # Bind right-click event to show context menu
        self.tree.bind("<Button-3>", self.show_context_menu_from_treeview)

        # Fetch all persons initially
        self.fetch_all_persons()

    def bind_row_context_menu(self, row_entries):
        for entry in row_entries:
            entry.bind("<Button-3>", lambda event: self.show_context_menu(event, row_entries))

    def show_context_menu(self, event, row_entries):
        row_context_menu = tk.Menu(self, tearoff=0)
        row_context_menu.add_command(label="Update Person", command=lambda: self.update_person(row_entries))
        row_context_menu.add_command(label="Delete Person", command=lambda: self.delete_person(row_entries))
        row_context_menu.post(event.x_root, event.y_root)

    def add_person(self):
        confirm = messagebox.askyesno("Confirmation", "Do you want to add the persons?")

        if confirm:
            for row_entries in self.data_entries[:-1]:  # Skip the last row
                data_to_add = [entry.get() for entry in row_entries[1:]]  # Exclude the first entry (ID)
                if any(data_to_add):  # Check if at least one field is filled
                    self.database_manager.insert_person(*data_to_add)
            messagebox.showinfo("Success", "Persons added successfully!")
            self.persons_added = True  # Set to True after adding persons

            # Fetch all persons after adding
            self.fetch_all_persons()

    def update_person(self, row_entries):
        if not self.persons_added:
            messagebox.showinfo("Info", "Please add persons first.")
            return

        person_id = simpledialog.askinteger("Update Person", "Enter Person ID:")
        if person_id is not None:
            data = [entry.get() for entry in row_entries[1:]]  # Exclude the first entry (ID)
            self.database_manager.update_person(person_id, *data)

            # Fetch all persons after updating
            self.fetch_all_persons()

    def delete_person(self, row_entries):
        if not self.persons_added:
            messagebox.showinfo("Info", "Please add persons first.")
            return

        person_id = simpledialog.askinteger("Delete Person", "Enter Person ID:")
        if person_id is not None:
            self.database_manager.delete_person(person_id)

            # Fetch all persons after deleting
            self.fetch_all_persons()

    def update_person_from_treeview(self, event):
        item = self.tree.selection()
        if item:
            person_id = self.tree.item(item, "values")[0]
            data = self.tree.item(item, "values")[1:]
            data_entries = self.data_entries[0][1:]  # Exclude the first entry (ID)

            for entry, value in zip(data_entries, data):
                entry.delete(0, tk.END)
                entry.insert(0, value)

            self.update_person(self.data_entries[0])

    def show_context_menu_from_treeview(self, event):
        item = self.tree.selection()
        if item:
            row_context_menu = tk.Menu(self, tearoff=0)
            row_context_menu.add_command(label="Update Person", command=lambda: self.update_person_from_treeview(event))
            row_context_menu.add_command(label="Delete Person", command=lambda: self.delete_person_from_treeview(event))
            row_context_menu.post(event.x_root, event.y_root)

    def delete_person_from_treeview(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            person_id = self.tree.item(selected_item, "values")[0]
            self.delete_person(person_id)

    def fetch_all_persons(self):
        persons = self.database_manager.fetch_all_persons()

        # Clear existing data in treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new data into treeview
        for person in persons:
            self.tree.insert("", "end", values=person)

    def search_person(self):
        search_text = self.search_entry.get()
        if search_text:
            search_query = f"SELECT * FROM Person WHERE name LIKE '%{search_text}%' OR " \
                           f"father_name LIKE '%{search_text}%' OR mother_name LIKE '%{search_text}%';"
            self.database_manager.cursor.execute(search_query)
            search_results = self.database_manager.cursor.fetchall()

            # Clear existing data in treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert new data into treeview
            for result in search_results:
                self.tree.insert("", "end", values=result)

if __name__ == "__main__":
    db_manager = DatabaseManager()
    gui = ExcelLikeGUI(db_manager)
    gui.mainloop()
