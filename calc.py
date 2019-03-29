import pandas as pd
from history import hist
import json
hist = hist()

df = pd.DataFrame(hist['aapl'])

with open('aapl.json', 'w') as fp:
    json.dump(hist,fp)
    #doesnt work
