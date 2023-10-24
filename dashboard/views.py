import os

import pandas as pd
import numpy as np
from django.shortcuts import render


def index(request):
    module_dir = os.path.dirname(__file__)
    data = pd.read_csv(
        os.path.join(module_dir, 'fan.csv'),
        usecols=[
            'timestamp',
            'U3_HNC10CT111',
            'U3_HNC10CT121',
            'U3_HNC10CT131',
            'U3_HNC10AA101XQ01',
            'U3_HNC10CG101XQ01'
        ],
        index_col='timestamp'
    )
    data = data[1000: 1020]

    data['U3_HNC10CT111'].values[2] -= 2.356
    data['U3_HNC10CT111'].values[3] -= 2.21

    data['U3_HNC10CT121'].values[3] += 1.1
    data['U3_HNC10CT121'].values[4] += 1.1
    data['U3_HNC10CT121'].values[5] += 1.1

    data['U3_HNC10CT131'].values[12] += 1.9

    xaxis = [i for i in range(1, 21)]
    U3_HNC10CT111 = data['U3_HNC10CT111'].values.tolist()
    U3_HNC10CT121 = data['U3_HNC10CT121'].values.tolist()
    U3_HNC10CT131 = data['U3_HNC10CT131'].values.tolist()
    U3_HNC10AA101XQ01 = data['U3_HNC10AA101XQ01'].values.tolist()
    U3_HNC10CG101XQ01 = data['U3_HNC10CG101XQ01'].values.tolist()

    context = {
        'xaxis': xaxis,
        'U3_HNC10CT111': U3_HNC10CT111,
        'U3_HNC10CT121': U3_HNC10CT121,
        'U3_HNC10CT131': U3_HNC10CT131,
        'U3_HNC10AA101XQ01': U3_HNC10AA101XQ01,
        'U3_HNC10CG101XQ01': U3_HNC10CG101XQ01,
    }

    return render(request, "dashboard/index.html", context)
