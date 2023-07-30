class CrimeRecord:
    def __init__(self, crime_id, date, location, description):
        self.crime_id = crime_id
        self.date = date
        self.location = location
        self.description = description

class CriminalRecord:
    def __init__(self, criminal_id, name, age, address):
        self.criminal_id = criminal_id
        self.name = name
        self.age = age
        self.address = address

class CrimeRecordSystem:
    def __init__(self):
        self.crime_records = []
        self.criminal_records = []
        self.logged_in_user = None

    def add_crime_record(self, crime_id, date, location, description):
        if self.logged_in_user:
            crime_record = CrimeRecord(crime_id, date, location, description)
            self.crime_records.append(crime_record)
            print("Crime record added successfully.")
        else:
            print("Please log in to add a crime record.")

    def add_criminal_record(self, criminal_id, name, age, address):
        if self.logged_in_user:
            criminal_record = CriminalRecord(criminal_id, name, age, address)
            self.criminal_records.append(criminal_record)
            print("Criminal record added successfully.")
        else:
            print("Please log in to add a criminal record.")

    def update_criminal_record(self, criminal_id, name, age, address):
        if self.logged_in_user:
            for criminal_record in self.criminal_records:
                if criminal_record.criminal_id == criminal_id:
                    criminal_record.name = name
                    criminal_record.age = age
                    criminal_record.address = address
                    print("Criminal record updated successfully.")
                    break
            else:
                print("Criminal record not found.")
        else:
            print("Please log in to update a criminal record.")

    def login(self):
        username = input('ENTER USERNAME: ').lower()
        password = input('ENTER PASSWORD: ').lower()
        logins = {'username1':'password1', 'username2':'password2','username3':'password3'}
        if logins[username]== password:
            self.logged_in_user = username
            print("Login successful.")
        else:
            print("Invalid username or password.")

    def logout(self):
        self.logged_in_user = None
        print("Logged out successfully.")

    def check_criminal_records(self):
        if self.logged_in_user:
            print("Criminal Records:")
            for criminal_record in self.criminal_records:
                print(f"Criminal ID: {criminal_record.criminal_id}")
                print(f"Name: {criminal_record.name}")
                print(f"Age: {criminal_record.age}")
                print(f"Address: {criminal_record.address}")
                print()
        else:
            print("Please log in to check criminal records.")


crime_system = CrimeRecordSystem()

crime_system.login()

crime_system.add_crime_record(1, "2023-07-16", "Hogwarts", "Burglary")

crime_system.add_criminal_record(1, "harry potter", 30, "cloudy highlands of Scotland")

crime_system.add_criminal_record(2, "hermoine", 35, "Hampstead Garden Suburb")

crime_system.update_criminal_record(2, "hermoine granger", 35, "Hampstead Garden Suburb")

crime_system.check_criminal_records()

crime_system.logout()
