def save_inquiry_form():
    try:        
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        inquiry = input("Enter your inquiry: ")
        form_data = {
            "Name": name,
            "Email": email,
            "Inquiry": inquiry
        }

        with open("formdata.txt", 'a') as file:
            file.write("===== Inquiry Form Data =====\n")
            for key, value in form_data.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")

        print("Inquiry form data has been successfully saved to formdata.txt.")

    except Exception as e:
        print(f"Error: {e}")

save_inquiry_form()
