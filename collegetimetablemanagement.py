import pymongo

class TimeTableManager:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["college_timetable"]
        self.schedule_bca = self.db["bca_schedule"]
        self.schedule_mca = self.db["mca_schedule"]

    def add_subject(self, stream, subject, teacher, day, start_time, end_time):
        if stream.lower() == 'bca':
            self._add_subject_to_schedule(self.schedule_bca, subject, teacher, day, start_time, end_time)
        elif stream.lower() == 'mca':
            self._add_subject_to_schedule(self.schedule_mca, subject, teacher, day, start_time, end_time)
        else:
            print("Invalid stream. Please enter 'BCA' or 'MCA'.")

    def _add_subject_to_schedule(self, schedule, subject, teacher, day, start_time, end_time):
        data = {"subject": subject, "teacher": teacher, "day": day, "start_time": start_time, "end_time": end_time}
        schedule.insert_one(data)
        print(f"Subject '{subject}' with teacher '{teacher}' added successfully on {day} from {start_time} to {end_time}.")

    def compare_timetables(self):
        overlapping_subjects = set()
        for subject in self.schedule_bca.distinct("subject"):
            if self.schedule_mca.find_one({"subject": subject}):
                overlapping_subjects.add(subject)

        if overlapping_subjects:
            print("Warning: Overlapping subjects found:")
            for subject in overlapping_subjects:
                print(subject)
        else:
            print("No overlapping subjects found.")

    def view_schedule(self, stream):
        if stream.lower() == 'bca':
            self._view_schedule(self.schedule_bca)
        elif stream.lower() == 'mca':
            self._view_schedule(self.schedule_mca)
        else:
            print("Invalid stream. Please enter 'BCA' or 'MCA'.")

    def _view_schedule(self, schedule):
        print("Day\tSubject\t\tTeacher\t\tStart Time\tEnd Time")
        for doc in schedule.find():
            print(f"{doc['day']}\t{doc['subject']}\t\t{doc['teacher']}\t\t{doc['start_time']}\t\t{doc['end_time']}")

def main():
    timetable = TimeTableManager()

    while True:
        print("\nCollege Time Table Management Menu:")
        print("1. Add a subject to BCA schedule")
        print("2. Add a subject to MCA schedule")
        print("3. View BCA time schedule")
        print("4. View MCA time schedule")
        print("5. Compare BCA and MCA Timetables")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            timetable.add_subject('BCA', input("Enter subject: "), input("Enter teacher's name: "), input("Enter day: "), input("Enter start time: "), input("Enter end time: "))
        elif choice == '2':
            timetable.add_subject('MCA', input("Enter subject: "), input("Enter teacher's name: "), input("Enter day: "), input("Enter start time: "), input("Enter end time: "))
        elif choice == '3':
            timetable.view_schedule('BCA')
        elif choice == '4':
            timetable.view_schedule('MCA')
        elif choice == '5':
            timetable.compare_timetables()
        elif choice == '6':
            print("Exiting the Time Table Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
