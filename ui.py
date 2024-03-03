from logger import*

def interface():

    user_input = None
    while user_input != '6':
        print(
        'Available actions:\n'
        '1. Create note\n'
        '2. Edit note\n'
        '3. Remove note\n'
        '4. Show all notes\n'
        '5. Search note by date\n'
        '6. Exit\n'
        )

        user_input = input('Enter number of action: ')

        while user_input not in ('1', '2', '3', '4', '5', '6'):
            print('Wrong input! Try again.')
            user_input = input('Enter number of action: ')

        print()

        match user_input:
            case '1':
                create_note()
            case '2':
                edit_note()
            case '3':
                remove_note()
            case '4':
                print_all_notes()
            case '5':
                search_note()