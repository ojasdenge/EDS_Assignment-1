import pandas as pd

# Load the student ID and name from the "Stud.txt" file
stud_data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Assignment-1/Student.csv")

# Load the placement data from the "Placement.csv" file
placement_data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Assignment-1/Placement.csv")

# Load the result data from the "Result.csv" file
result_data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Assignment-1/Result.csv")

# Merge the data into a single DataFrame using the student ID as the key
student_details = pd.merge(stud_data, placement_data, on="ID")
student_details = pd.merge(student_details, result_data, on="ID")

# Save the combined data to a CSV file
student_details.to_csv("/content/drive/MyDrive/Colab Notebooks/Assignment-1/StudentDetails.csv", index=False)

# Display Student Details
df1 = pd.read_csv(r'/content/drive/MyDrive/Colab Notebooks/Assignment-1/StudentDetails.csv')
display(df1)

# Load the combined data from the "StudentDetails.csv" file
student_details = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Assignment-1/StudentDetails.csv")

# Calculate the average CGPA
avg_cgpa = student_details["CGPA"].mean()

# Calculate the maximum CGPA
max_cgpa = student_details["CGPA"].max()

# Calculate the minimum CGPA
min_cgpa = student_details["CGPA"].min()

# Count the number of students
count = student_details["ID"].count()

# Calculate the percentage of students who are placed
placed_students = student_details[student_details["Placement Status"] == 1]
placed_percentage = (len(placed_students) / count) * 100

# Print the results
print("Average CGPA: {:.2f}".format(avg_cgpa))
print("Maximum CGPA: {:.2f}".format(max_cgpa))
print("Minimum CGPA: {:.2f}".format(min_cgpa))
print("Number of students: {:.2f}".format(count))
print("Placed Students: {}".format(placed_students))
print("Placed Percentage: {:.2f}".format(placed_percentage))