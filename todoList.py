import os 
import datetime
import sqlite3

class taskInfo:
    def __init__(self):
        self.tasks = []
        self.current_date = datetime.date.today()
        try:
            self.con = sqlite3.connect("/home/r00t/Documents/SqliteDB/todoList.db")
            self.curr = self.con.cursor()
        except Exception as e:
            print(f"Error in Connection {e}")

    def storeValues(self):
        try:
            message = input("Enter your note: ")
            date = self.current_date
            self.tasks.append((message, date))
            self.curr.executemany('INSERT INTO todo(message, date) VALUES (?, ?)', self.tasks)
            self.con.commit()
        except Exception as e:
            print(f"Error! {e}")

    def viewValues(self):
        message_values = self.curr.execute('SELECT id, message, date FROM todo')
        print("=====================================================")   
        print("|| ID  ||         LIST           ||      DATE      ||")
        print("=====================================================")
        print("\n")

        for id, message, date in message_values:
            print(f"{id}. Message-> {message}. Date-> {date} ")
        
        print("\n\n")

    def updateValues(self):
        try:
            choice = int(input("Enter the id: "))
            new_message = input("Enter new message: ")
            proceed = input("Do you want to edit the Date?: ")
            if(proceed == 'Y' or proceed == 'y'):
                print("Date format: YYYY-DD-MM")
                new_date = input("Enter the date: ")
                self.curr.execute('UPDATE todo SET message = (?), date = (?) WHERE id = (?)', (new_message, new_date, choice))    
            else:
                self.curr.execute('UPDATE todo SET message = (?) WHERE id = (?)', (new_message, choice))
        except Exception as e:
            print(f"Error! {e}")


    def deleteValues(self):
        try:
            choice = int(input("Enter the id: "))
            confirmation = input(f"Are you sure you want to delete? id {choice}: ")
            if(confirmation == 'Y' or confirmation == 'y'):
                self.curr.execute('DELETE FROM todo WHERE id = ?', (choice,))
            else:
                return 'Okay!';
        except Exception as e:
            print(f"Error! {e}")
        self.con.commit()

    def clearScreen(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def closeConnection(self):
        self.con.close()

if __name__ == "__main__":
   taskObj = taskInfo()
try:
       while True:
        print("=========Todo List by Jorge==========\n")
        print("1. Add Task")
        print("2. View Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("q. Quit")
        choice = input("Enter your choice:").strip()

        match choice:
            case '1':
                taskObj.clearScreen()
                taskObj.storeValues()
            case '2':
                taskObj.clearScreen()
                taskObj.viewValues()
            case '3':
                taskObj.clearScreen()
                taskObj.viewValues()
                taskObj.updateValues()
            case '4':
                taskObj.clearScreen()
                taskObj.viewValues()
                taskObj.deleteValues()
            case 'q':
                taskObj.clearScreen()
                print("Thank you for using my todo list!")
                break
finally:
    taskObj.closeConnection()
