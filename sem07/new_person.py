import telephone_book as tb
import view


def writing_down():
    name = view.get_name()
    phone = view.get_number()
    action = view. what_to_do()
    if action == 'add_new_contact':
        if name[0] not in tb.t_book:
            tb.create_new_list(name, tb.t_book)
        tb.create_new_note(name, tb.t_book, phone)
    elif action == 'change_number':
        tb.update_note(name, tb.t_book, phone)
    elif action == 'add_new_number':
        tb.append_number(name, phone, tb.t_book)
    elif action == 'delete_number':
        tb.delete_note(name, tb.t_book)
    return tb.t_book