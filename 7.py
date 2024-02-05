name = input("Enter your name: ")
email = input("Enter your email address: ")
inquiry = input("Enter your inquiry: ")
form_data = {"Name": name, "Email": email, "Inquiry": inquiry}

with open("formdata.txt", 'a') as file:
    for key, value in form_data.items():
        file.write(f"{key}: {value}\n")
    file.write("\n")

