#a-O(n3)
#b-O(n3)
#c-O(n!)
#d-O(nlogn)
#e-O(n)
#f-O(n2)
#g-O(n2)
#h-O(n!)
def sum_tuples(tup1, tup2):
    """Sum the corresponding elements of two tuples and return the resulting tuple."""
    somme = []
    if len(tup1) != len(tup2):
        return -1  
    else:
        for i in range(len(tup1)):
            somme.append(tup1[i] + tup2[i])
    return tuple(somme)

def dict_to_json_manual(dictionary, filename):
    """Convert a dictionary to JSON format and write it to a file manually."""
    def to_json_value(value):
        if isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, bool):
            return 'true' if value else 'false'
        elif value is None:
            return 'null'
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, dict):
            return dict_to_json_string(value)
        elif isinstance(value, list):
            return "[" + ", ".join([to_json_value(item) for item in value]) + "]"
        else:
            raise TypeError(f"Unsupported data type: {type(value)}")

    def dict_to_json_string(dictionary):
        items = []
        for key, value in dictionary.items():
            json_key = f'"{key}"'
            json_value = to_json_value(value)
            items.append(f'{json_key}: {json_value}')
        return "{" + ", ".join(items) + "}"

    with open(filename, 'w') as file:
        json_content = dict_to_json_string(dictionary)
        file.write(json_content)

def json_to_dict_manual(filename):
    """Read a JSON file and convert each object into a dictionary manually."""
    with open(filename, 'r') as file:
        data = file.read().strip()

    def parse_json_value(value_str):
        if value_str.startswith('"') and value_str.endswith('"'):
            return value_str[1:-1]
        elif value_str == "true":
            return True
        elif value_str == "false":
            return False
        elif value_str == "null":
            return None
        elif value_str.isdigit():
            return int(value_str)
        try:
            return float(value_str)
        except ValueError:
            raise ValueError(f"Invalid JSON value: {value_str}")

    def parse_json_object(json_str):
        obj = {}
        json_str = json_str[1:-1].strip()
        items = json_str.split(', ')
        for item in items:
            key, value = item.split(": ")
            key = key[1:-1]
            obj[key] = parse_json_value(value)
        return obj

    return [parse_json_object(data)]  

def menu():
    while True:
        print("1. Sum Tuples")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")
        print("-" * 30)
        choice = input("Enter a choice: ")

        if choice == "1":
            try:
                tup1 = tuple(map(int, input("Enter the first tuple (comma-separated): ").split(',')))
                tup2 = tuple(map(int, input("Enter the second tuple (comma-separated): ").split(',')))
                result = sum_tuples(tup1, tup2)
                if result == -1:
                    print("Error: Tuples must be of the same length.")
                else:
                    print(f"Resulting tuple: {result}")
            except ValueError:
                print("Invalid input. Please enter valid integers for the tuples.")
        elif choice == "2":
            data = {
                "name": "John",
                "age": 30,
                "is_student": False,
                "courses": ["Math", "Science"],
                "details": {"university": "XYZ", "year": 4}
            }
            filename = input("Enter the filename to export JSON: ")
            dict_to_json_manual(data, filename)
            print(f"Data exported to {filename}")
        elif choice == "3":
            filename = input("Enter the filename to import JSON: ")
            try:
                result = json_to_dict_manual(filename)
                print(f"Data imported: {result}")
            except Exception as e:
                print(f"Error importing JSON: {e}")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()

menu()
