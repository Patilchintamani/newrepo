def compare_timetables(timetable1, timetable2):
    common_slots = set(timetable1) & set(timetable2)
    if not common_slots:
        return "No common slots found."
    
    common_slots = sorted(common_slots, key=lambda x: (x[0], int(x[1].split(':')[0])))
    comparison_result = "Common slots:\n"
    for slot in common_slots:
        comparison_result += f"{slot[0]} - {slot[1]}\n"
    
    return comparison_result

# Example timetables for two students
student1_timetable = [("Monday", "08:00"), ("Wednesday", "10:00"), ("Friday", "13:00")]
student2_timetable = [("Monday", "08:00"), ("Tuesday", "11:00"), ("Friday", "13:00")]

# Compare the timetables
comparison_result = compare_timetables(student1_timetable, student2_timetable)
print(comparison_result)
