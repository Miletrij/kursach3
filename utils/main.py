from utils.utils_code import *

values = get_executed_operations(load_json_file())
operations = sort_data_operations(values)
data = format_date(operations)
card_mask = card_number_mask(operations)
amount_mask = amount_number_mask(operations)


for operation in range(len(operations)):
    print(f"{data[operation]} {operations[operation]['description']}\n"
          f"{card_mask[operation]} -> Счет: {amount_mask[operation]}\n"
          f"{operations[operation]['operationAmount']['amount']}"
          f"{operations[operation]['operationAmount']['currency']['name']}\n")
