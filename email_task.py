

class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        '''
        class constructor is created with argumets email_address, 
        subject_line and email_content
        four instance methods has been created to do different functionality
        an instance variable has_been_read is created and initiazed to False
        '''

    def mark_as_read(self):
        self.has_been_read = True

email_box = []

def populate_inbox():
    email_box.append(Email("david@gmail.com", "Welcome to HyperionDev!", "This is your first welcome email."))
    email_box.append(Email("smith_123@gmail.com", "Project Update", "Here's an update on the ongoing project."))
    email_box.append(Email("john14@hotmail.com", "Meeting Reminder", "Reminder about tomorrow's meeting."))
    email_box.append(Email("jack_98@yahoo.com","gym closure", "Good morning John,The gym will remain closed this weekend!"))
    email_box.append(Email("rachel10@gmail.com","NHS-appo", "Hello Rachel,Gentle reminder that your appointment is tomorrow!"))
    email_box.append(Email("mark_ab@yahoo.com","work related", "Hi Mark, Please come to work today!"))

def list_emails():
    print("\nListing all emails:")
    print("-------------------")
    for index, email in enumerate(email_box):
        status = 'Read' if email.has_been_read else 'Unread'
        print(f"{index}: {email.subject_line} ({status})")

def read_email(index):
    if 0 <= index < len(email_box):
        email = email_box[index]
        print(f"\nReading email {index}:")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}\n")
        email.mark_as_read()
        print("Email marked as read.\n")
    else:
        print("Invalid email index. Please try again.")

def email_simulator_menu():
    populate_inbox()  # Initially populate the inbox with emails

    while True:
        print("\nEmail Simulator Menu:")
        print("----------------------")
        print("1. List all emails")
        print("2. Read an email")
        print("3. Quit")
        
        choice = input("Please choose an option: ")
        if choice == "1":
            list_emails()
        elif choice == "2":
            index = int(input("Enter the index of the email to read: "))
            read_email(index)
        elif choice == "3":
            print("Exiting the Email Simulator.")
            break
        else:
            print("Invalid choice, please try again.")
email_simulator_menu()
