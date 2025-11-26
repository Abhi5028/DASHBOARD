#!/usr/bin/env python3

"""Preprocess BlinkIT Grocery Data XLSX -> CSV/Parquet"""
import pandas as pd
from pathlib import Path

def convert_xlsx(input_path, out_dir='data', sheet_name=0):
    p = Path(input_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    df = pd.read_excel(p, sheet_name=sheet_name)
    csv_path = out_dir / (p.stem + '.csv')
    parquet_path = out_dir / (p.stem + '.parquet')
    df.to_csv(csv_path, index=False)
    try:
        df.to_parquet(parquet_path, index=False)
    except Exception:
        # parquet optional
        pass
    print(f"Wrote {csv_path} and {parquet_path}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Path to input XLSX file')
    parser.add_argument('--out', default='data', help='Output directory')
    parser.add_argument('--sheet', default=0, help='Sheet name or index')
    args = parser.parse_args()
    convert_xlsx(args.input, args.out, args.sheet)