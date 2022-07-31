#!/bin/bash
BOOKDIR="$1"
python3 check_parity.py "$BOOKDIR""/he.json" "$BOOKDIR""/cs.json"