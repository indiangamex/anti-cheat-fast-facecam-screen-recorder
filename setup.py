import threading
import subprocess
def gui():
    subprocess.run("python3 gui_recorder.py", shell = True)
def design():
    subprocess.run("python3 design.py", shell = True)

if __name__ == "__main__":

    # creating threads
    t1 = threading.Thread(target=design, name='t1')
    t2 = threading.Thread(target=gui, name='t2')

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()



