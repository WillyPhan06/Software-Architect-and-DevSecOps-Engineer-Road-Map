import pandas as pd

def read_row(df, index):
    try:
        row = df.iloc[index]
        print("\nRow at index", index, ":\n", row)
    except IndexError:
        print("Error: Index out of range.")

def add_row(df, file_path):
    new_data = {}
    for col in df.columns:
        value = input(f"Enter value for {col}: ")
        new_data[col] = value
    new_row = pd.DataFrame([new_data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)
    print("Row added successfully.")
    return df

def update_row(df, file_path, index):
    try:
        print("\nCurrent row at index", index, ":\n", df.iloc[index])
        new_data = {}
        for col in df.columns:
            value = input(f"Enter new value for {col} (press Enter to keep '{df.iloc[index][col]}'): ")
            new_data[col] = value if value else df.iloc[index][col]
        df.iloc[index] = new_data
        df.to_csv(file_path, index=False)
        print("Row updated successfully.")
    except IndexError:
        print("Error: Index out of range.")
    return df

def delete_row(df, file_path, index):
    try:
        df = df.drop(index)
        df.to_csv(file_path, index=False)
        print("Row deleted successfully.")
    except IndexError:
        print("Error: Index out of range.")
    return df.reset_index(drop=True)

def display_csv(df):
    print("\nCurrent CSV content:\n", df)

def main():
    file_path = input("Enter the path to your CSV file: ")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    while True:
        print("\nCSV Manipulator Menu:")
        print("1. Read a row by index")
        print("2. Add a new row")
        print("3. Update a row")
        print("4. Delete a row")
        print("5. Display entire CSV")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                index = int(input("Enter row index to read: "))
                read_row(df, index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '2':
            df = add_row(df, file_path)
        elif choice == '3':
            try:
                index = int(input("Enter row index to update: "))
                df = update_row(df, file_path, index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter row index to delete: "))
                df = delete_row(df, file_path, index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '5':
            display_csv(df)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()