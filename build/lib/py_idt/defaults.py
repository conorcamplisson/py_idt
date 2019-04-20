
DEFAULT_PARAMS = {
    'scale': '25nm',
    'purification': 'STD',
    'output_dir': 'IDT_xlsx_output'
}

# IDT reference data acquired 2019-04-19 from: https://www.idtdna.com/site/order/oligoentry
SCALE_DICT = {
    '25nm':	'25 nmole',
    '100nm': '100 nmole',
    '250nm': '250 nmole',
    '1um': '1 µmole',
    '5um': '5 µmole',
    '10um': '10 µmole',
    '4nmU': '4 nmole Ultramer',
    '20nmU': '20 nmole Ultramer',
    'PU': 'PAGE Ultramer',
    '25nmS': '25 nmole Sameday'
}
PURIFICATION_DICT = {
    'STD': 'Standard Desalting',
    'PAGE': 'PAGE',
    'HPLC': 'HPLC',
    'IEHPLC': 'IE HPLC',
    'RNASE': 'RNase Free HPLC',
    'DUALHPLC': 'Dual HPLC',
    'PAGEHPLC': 'Dual PAGE & HPLC'
}
