import pandas as pan

excel_data_df = pandas.read_excel('UpiSprint1_860061256806_14-02-2020_22_00_29-02-2020_22_00_tags_ALL.xlsx', sheet_name='Data Dump')

json_str = excel_data_df.to_json()

print('Excel Sheet to JSON:\n', json_str)