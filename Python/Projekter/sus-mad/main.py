import csv
#with open("madplan.csv", newline="") as csv:
    
class FoodRecon:

  
    def WriteFood():
        filename = "madplan.csv"
        fields = ['Name', 'Branch', 'Year', 'CGPA']
        # data rows of csv file
        rows = [['Nikhil', 'COE', '2', '9.0'],
                ['Sanchit', 'COE', '2', '9.1'],
                ['Aditya', 'IT', '2', '9.3'],
                ['Sagar', 'SE', '1', '9.5'],
                ['Prateek', 'MCE', '3', '7.8'],
                ['Sahil', 'EP', '2', '9.1']]

        with open(filename, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)

FoodRecon.WriteFood()