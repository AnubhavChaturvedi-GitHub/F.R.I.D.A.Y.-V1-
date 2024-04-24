import threading
import time
import eel

from logic_brain import friday_brain

eel.init("web")
@eel.expose
def display_response(element_id):
    while True:
        try:
            response_file = "output.txt"
            input_file = "input.txt"
            # Read data from input file
            with open(input_file, 'r') as f:
                input_data = f.read().strip()
            # Read data from response file
            with open(response_file, 'r') as f:
                response_data = f.read().strip()
            # Update the content of the element using JavaScript
            js_script = f"document.getElementById('{element_id}').innerText = 'Input: {input_data}\nResponse: {response_data}';"
            eel.js(js_script)()
        except Exception as e:
            print("Error:", e)
        time.sleep(1)  # Adjust the interval according to your needs

def ui():
    eel.start("index.html",mode='chrome', port=8080, cmdline_args=['--start-fullscreen'])

def friday():
    t1 = threading.Thread(target=friday_brain)
    t2 = threading.Thread(target=ui)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

friday()