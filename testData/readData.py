import subprocess
import os

# Define the path to the JSON file
#a= runJson("C:\\disk\\PyRestAPI\\pythonProject1\\testData\\student.json")


    # Ensure the file exists
import subprocess
import os

# Define the path to the JSON file
json_file_path = 'C:\\disk\\PyRestAPI\\pythonProject1\\testData\\student.json'

# Ensure the file exists
if not os.path.isfile(json_file_path):
    raise FileNotFoundError(f"{json_file_path} not found!")

# Command to run the JSON server
command = f'json-server --watch {json_file_path}'

# Run the command
process = subprocess.Popen(command, shell=True)
print(f"Started JSON server with PID: {process.pid}")

# Keep the script running to keep the server alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Terminating JSON server...")
    process.terminate()
