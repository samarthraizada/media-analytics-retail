setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

demo:
	python src/ingest/load_sample.py
	python src/attribution/mta.py --paths data/sample/paths_sample.csv --out data/sample/attribution_out.csv
	python src/modeling/mmm.py --features data/sample/mmm_features_sample.csv --out data/sample/mmm_outputs.json
	python src/forecast/forecast.py --hist data/sample/pos_sales_sample.csv --out data/sample/forecast_out.csv
