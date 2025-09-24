import argparse, pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def main(hist_csv, out_csv):
    df = pd.read_csv(hist_csv).sort_values(['week_id'])
    # aggregate to series (toy)
    s = df.groupby('week_id')['units_sold'].sum().astype('float')
    model = SARIMAX(s, order=(1,1,1), seasonal_order=(0,0,0,0), enforce_stationarity=False, enforce_invertibility=False)
    res = model.fit(disp=False)
    pred = res.get_forecast(steps=4)
    out = pred.summary_frame()[['mean','mean_ci_lower','mean_ci_upper']].reset_index().rename(columns={'index':'week_id'})
    out.to_csv(out_csv, index=False)
    print('Forecast saved to', out_csv)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--hist', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    main(args.hist, args.out)
