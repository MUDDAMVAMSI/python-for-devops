import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path) #imports all files in directory os.listdir()
        return files, None
    except FileNotFoundError:  #why we used exceptional handling means to not get erros if no files are found
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()

#step 1: Read input from the user
#step 2: for loop , folder -->list files
#step 3: Identify module
#step 4: print file
#step 5: Handle any known errors