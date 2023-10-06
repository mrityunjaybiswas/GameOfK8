import requests

userDataURL = "https://dummyjson.com/users"

def get_employee_data(userData, emp_id):
    for user in userData['users']:
        if user.get('id') == emp_id:
            return user
    return None

def emp_input(employee_data):
    if employee_data:
        print("User ID:", employee_data['id'])
        print("First Name:", employee_data['firstName'])
        print("Last Name:", employee_data['lastName'])
        print("Maiden Name:", employee_data['maidenName'])
        print("Age:", employee_data['age'])
        print("Gender:", employee_data['gender'])
        print("Email:", employee_data['email'])
        print("Phone:", employee_data['phone'])
        print("Username:", employee_data['username'])
        print("Password:", employee_data['password'])
        print("Birth Date:", employee_data['birthDate'])
    else:
        print("User not found.")

def get_data(user_data_url):
    response = requests.get(user_data_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch user data.")
        return None

if __name__ == "__main__":
    userData = get_data(userDataURL)
    if userData:
        while True:
            user_input = input("Enter User ID (or type exit to exit): ")
            if user_input.lower().strip() == 'exit':
                break
            try:
                emp_id = int(user_input)
                employee_data = get_employee_data(userData, emp_id)
                if employee_data:
                    emp_input(employee_data)
                else:
                    print("User not found.")
            except ValueError:
                print("Please enter a valid integer for User ID or exit to exit.")
