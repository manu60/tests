import sys
import pandas as pd
import math

def get_thetas(reset=False):
    if reset:
        thetas = pd.DataFrame({'t0': [0], 't1': [0]})
        thetas.to_csv('thetas.csv', mode='w', header=['t0', 't1'], index=False)

    try:
        thetas = pd.read_csv('thetas.csv')
    except:
        thetas = pd.DataFrame({'t0': [0], 't1': [0]})
        thetas.to_csv('thetas.csv', mode='w', header=['t0', 't1'], index=False)
    t0 = thetas.iloc[-1]['t0']
    t1 = thetas.iloc[-1]['t1']
    if math.isnan(t0):
        t0 = 0
    if math.isnan(t1):
        t1 = 0
    return t0, t1

if __name__ == '__main__':
    txt_input = input('Please input a car mileage: ')
    try:
        mileage = float(txt_input)
        if math.isinf(mileage) or mileage < 0:
            raise ValueError
    except ValueError:
        sys.exit('Wrong input provided')

    t0, t1 = get_thetas()

    price_prediction = t0 + (t1 * mileage)
    print('Estimated price for this mileage: {}'.format(int(price_prediction)))