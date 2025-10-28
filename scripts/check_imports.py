modules = [
    'pyspark',
    'pyarrow',
    'numpy',
    'pandas',
    'sqlalchemy',
    'snowflake.connector'
]

import importlib, sys

errors = []
for m in modules:
    try:
        importlib.import_module(m)
    except Exception as e:
        errors.append((m, str(e)))

if errors:
    print('=== IMPORT ERRORS ===')
    for mod, err in errors:
        print(f'{mod}: {err}')
    sys.exit(1)

print('All imports succeeded')
