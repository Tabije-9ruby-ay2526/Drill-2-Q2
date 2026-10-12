from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ''

    math_club_members = ['CEAN ALAGAR', 'MOHAMMAD CALACA', 'POCH OLO COMANDA', 'JM PIANSAY', 'BELA ALLAS', 'DAPHNE MARIANO']
    f_name = ['CEAN', 'MOHAMMAD', 'POCH OLO', 'JM', 'BELA', 'DAPHNE']
    l_name = ['ALAGAR', 'CALACA', 'COMANDA', 'PIANSAY', 'ALLAS', 'MARIANO']

    f_name = document.getElementById('fname').value.upper().strip()
    l_name = document.getElementById('lname').value.upper().strip()

    full_name = f_name + ' ' + l_name
    name_checker = full_name in math_club_members

    display_message = (f'Sorry, {full_name} is not in the list.', f'{full_name} is in the list!') #true(1) false(0)

    display(display_message[name_checker], target='div1')
