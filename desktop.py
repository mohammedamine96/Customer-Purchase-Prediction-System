import eel
import threading
import time
from app import app

def start_server():
    app.run(port=5000)

if __name__ == '__main__':
    # Start the Flask server in a separate thread
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    # Give the server a moment to start
    time.sleep(1)

    # Initialize Eel (pointing to static folder, though we use a URL)
    eel.init('static')
    
    # Start Eel window pointing to the loader page which redirects to Flask
    try:
        # Try to open in an app-like window (Chrome/Edge)
        eel.start('loader.html', size=(1000, 800), port=0)
    except EnvironmentError:
        # If Chrome/Edge is not found, fallback to default browser
        print("Chrome/Edge not found, falling back to default browser...")
        eel.start('loader.html', size=(1000, 800), mode='default', port=0)

