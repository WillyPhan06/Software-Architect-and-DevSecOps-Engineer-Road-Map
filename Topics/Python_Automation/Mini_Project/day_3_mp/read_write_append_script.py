# Playing around with a sample .txt file using read append, write

file_1 = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_3_mp\for_read.txt"

with open(file_1, "r") as f:
    text = f.read()
print(text)

with open(file_1, "a") as f_2:
    f_2.write("\n")
    f_2.write("Yo another fourth line just got appended!!")

#Overwriting it with nothing to delete it when i haven't know how to delete all yet
with open(file_1, "w") as f_3:
    f_3.write("")

#Now separate each word with a space
with open(file_1, "a") as f_4:
    for word in text:
        f_4.write(f"{word} ")


