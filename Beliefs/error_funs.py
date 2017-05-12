

def App1Page2_error_message(page, values):
    print('we are in error fun for {}, with values {} now...'.format(type(page), values))
    if values['FieldForA1P2'] % 2 == 0:
        return 'You must insert an odd number'
