print("Welcome to the Student App Access Manager")

name = input("Let's start by getting to know you. What's your name? ")
age = int(input("How old are you? "))

print("\nHere is a summary of your information:")
print(f"Your name is {name},")
print(f"and you are {age} years old.")

print("\nData Types")
print(type(name))
print(type(age))

approved_apps = ["Google Classroom", "Python", "Khan Academy"]
restricted_apps = ["Instagram", "TikTok", "Games"]

app = input("\nWhat app are you planning to use on the school Wi-Fi? ")

if app in approved_apps:
    print("You're all good to use this app.")
elif app in restricted_apps:
    print("You can't use this app in school.")
else:
    print("This app is not identified by the Wi-Fi. It is being sent to the admin.")

READ = 0b001
WRITE = 0b010
EXECUTE = 0b100

permissions = READ | WRITE

print("\nPermissions:", bin(permissions))

if permissions and READ:
    print("You are given permission to read.")
else:
    print("Writing permissions are not granted")

if permissions and WRITE:
    print("You are given permission to write.")
else:
    print("Writing permissions are not granted")

if permissions and EXECUTE:
    print("You are given permission to execute.")
else:
    print("Execution permissions are not granted")

number = 5

print("\nThe original number is", number)
print("The number left shifted is", number << 1)
print("The number right shifted is", number >> 1)