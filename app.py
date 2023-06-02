started = False

while True:
    text_input = input('>')
    if text_input.lower() == 'help':
        print('''you have three options you can either 
enter "stop" for car to stop
enter "start" for car to start
enter "exit" to exit the game''')
    elif text_input.lower() == 'start':
        if started:
            print('the car is already started')
        else:
            started = True
            print('the car is started')

    elif text_input.lower() == 'stop':
        if not started:
            print('the car is already stopped')
        else:
            started = False
            print('the car is stopped')



    elif text_input.lower() == 'exit':
        break
    else:
        print("i don't recognize this shit")
