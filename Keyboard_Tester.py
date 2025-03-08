import keyboard

def test_keys():
    print("Press any key to test (press 'esc' to exit):")
    print("esc key will be tested when exiting.")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f'Key "{event.name}" pressed.')
        if event.name == 'esc':
            print("Exiting key tester.")
            break

if __name__ == "__main__":
    test_keys()
