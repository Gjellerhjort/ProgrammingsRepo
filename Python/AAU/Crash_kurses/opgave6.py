school = 'Aalborg University'
classroom = "Programering for matematikere"
number_of_lectures = 12
minutes_per_lecture = 130
total_minutes = number_of_lectures * minutes_per_lecture #Compute total minutes for entire class
total_hours = total_minutes / 60
remaining_minutes = total_minutes % 60
# fejl her at bruge " istedet for ' og ingen () og mangler f foran string
print(f'The class {classroom} is held at {school} over {number_of_lectures} lectures for at total of {total_hours} hours and {remaining_minutes} minutes') 