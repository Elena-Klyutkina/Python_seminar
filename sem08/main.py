# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from new_person import writing_down as wd
import view
import json_module as jm

employee_catalog = wd()
view.export_catalog(employee_catalog)
jm.exp_json(employee_catalog, filename = 'Employee_database')