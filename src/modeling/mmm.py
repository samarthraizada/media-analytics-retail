import argparse, pandas as pd, json
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

def main(feat_csv, out_json):
    df = pd.read_csv(feat_csv)
    X = df[['spend_ctv_adstock','spend_yt_adstock','spend_meta_adstock',
            'spend_search_adstock','spend_display_adstock',
            'google_trends_norm','temp_avg_f','promo_intensity_idx',
            'inventory_cap_idx','season_sin','season_cos']]
    y = df['units_sold']
    Xtr, Xte, ytr, yte = train_test_split(X,y,test_size=0.34, random_state=42)
    model = Ridge(alpha=1.0).fit(Xtr,ytr)
    mape = float(mean_absolute_percentage_error(yte, model.predict(Xte)))
    coefs = dict(zip(X.columns.tolist(), model.coef_.tolist()))
    out = {'mape': mape, 'intercept': float(model.intercept_), 'coefs': coefs}
    with open(out_json, 'w') as f:
        json.dump(out, f, indent=2)
    print('Wrote', out_json, 'MAPE=', mape)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--features', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    main(args.features, args.out)
