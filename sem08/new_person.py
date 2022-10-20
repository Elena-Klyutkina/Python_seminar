import employee_database as ed
import view


def writing_down():
    name = view.get_name()
    post = view.get_position()
    action = view. what_to_do()
    if action == 'add_new_employee':
        if name[0] not in ed.employee_catalog:
            ed.create_new_list(name, ed.employee_catalog)
        ed.create_new_catalog(name, ed.employee_catalog, post)
    elif action == 'change_position':
        ed.update_catalog(name, ed.employee_catalog, post)
    elif action == 'delete_employee':
        ed.delete_catalog(name, ed.employee_catalog)
    return ed.employee_catalog