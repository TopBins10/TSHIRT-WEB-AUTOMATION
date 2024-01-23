import os
import pandas as pd

def extract_names_from_filename(filename):
    # Remove the file extension first
    filename_without_extension = os.path.splitext(filename)[0]

    # Replace all underscores with spaces, then split by space
    parts = filename_without_extension.replace('_', ' ').split()

    # Assuming the first two words are the first and last names
    first_name = parts[0]
    last_name = parts[1]
    
    return first_name, last_name

def rename_files_face(directory, df):
    df['First Name'] = df['First Name'].str.strip()
    df['Last Name'] = df['Last Name'].str.strip()

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            first_name, last_name = extract_names_from_filename(filename)
            matching_rows = df[(df['First Name'] == first_name) & (df['Last Name'] == last_name)]
            if not matching_rows.empty:
                
                row = matching_rows.iloc[0]
                
                _, ext = os.path.splitext(filename)
                new_filename = f"{row['First Name']}_{row['Last Name']}{ext}"
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)

                try:
                    os.rename(old_file, new_file)
                    print(first_name + ' ' + last_name + ':' + '. . . . DONE . . . .')
                except OSError as e:
                    print(f"Error renaming file {filename}: {e}")
            else:
                print(f"No DataFrame match found for file: {filename}")

def rename_files_sign(directory, df):
    df['First Name'] = df['First Name'].str.strip()
    df['Last Name'] = df['Last Name'].str.strip()

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            first_name, last_name = extract_names_from_filename(filename)
            matching_rows = df[(df['First Name'] == first_name) & (df['Last Name'] == last_name)]
            if not matching_rows.empty:
                
                row = matching_rows.iloc[0]
                
                new_filename = f"{row['First Name']}_{row['Last Name']}.png"
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)

                try:
                    os.rename(old_file, new_file)
                    print(first_name + ' ' + last_name + ':' + '. . . . DONE . . . .')
                except OSError as e:
                    print(f"Error renaming file {filename}: {e}")
            else:
                print(f"No DataFrame match found for file: {filename}")

file_path = '/Users/visvamurali/Downloads/Contact Information ~ MAGIC (File responses)/Contact Information (Responses).xlsx'
df = pd.read_excel(file_path)


faceDirectory = '/Users/visvamurali/Downloads/Contact Information ~ MAGIC (File responses)/PICTURE OF FACE! - White background please (File responses)'
signDirectory = '/Users/visvamurali/Downloads/Contact Information ~ MAGIC (File responses)/SIGNATURE! - black pen white paper - only pictures accepted_ (File responses)'
rename_files_face(faceDirectory, df)
print("Faces done!")
print( )
rename_files_sign(signDirectory, df)
print("Signatures done!")