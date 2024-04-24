from STT import listen
import threading
from main import *

def main():
    output_text = ""
    while True:
        try :
            while True:
                with open("web/input.txt","r") as input_cmd:
                    input_txt = input_cmd.read().strip()

                if input_txt != output_text:
                    output_text = input_txt
                    cmd = output_text.lower()
                    if cmd.startswith("friday"):
                        chat(cmd)
                    elif "friday" in cmd:
                        chat(cmd)
                    else:
                        pass
        except:
            pass



def friday_brain():
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=main)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

