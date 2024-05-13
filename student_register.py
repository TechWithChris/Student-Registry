# Requesting user input for no. of student registering and storing it in a variable
num_of_student= int(input("How many student are you registering: "))

 # Assigning the loop of the ID inputed into an empty variable
id_numbers= ""
# Iterate in the range of the number the user inputed
for i in range (num_of_student):
    student_id=input("Enter the student ID:  ")  # Requesting user's input of the first student ID
    id_numbers += student_id + "\n"
    print ("Please enter the next student ID")  # Prompt user's input for the next student ID
print ("Thank You, that would be all for now")
print ("Student ID:")
print (id_numbers)

# Writing the ID numbers into a text file   
with open("reg_form.txt","w") as student_id_no:
    for i in id_numbers.split(): # Iterating through the stored ID number and using .split to convert the string to list 
        student_id_no.write(i+".........."+"\n") 