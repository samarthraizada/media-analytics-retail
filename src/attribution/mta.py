import argparse, pandas as pd, numpy as np

def position_time_decay_weight(row, half_life_days=3):
    # Simplified: 0.4 first, 0.4 last, 0.2 assists; boost if qualified view
    base = 0.0
    if row.get('first_touch', 0) == 1: base += 0.4
    if row.get('last_touch', 0) == 1: base += 0.4
    if row.get('assist_touches', 0) > 0: base += 0.2
    if row.get('qualified_view', 0) == 1: base *= 1.1
    return base

def main(paths_csv, out_csv):
    df = pd.read_csv(paths_csv)
    df['credit'] = df.apply(position_time_decay_weight, axis=1)
    # Aggregate to weekly DMA x channel credit value
    agg = df.groupby(['week_id','dma_id','channel_id'], as_index=False).agg(
        credited_value_usd=('conv_value','sum'),
        credit=('credit','sum')
    )
    agg.to_csv(out_csv, index=False)
    print('Wrote', out_csv, 'rows=', len(agg))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--paths', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    main(args.paths, args.out)
