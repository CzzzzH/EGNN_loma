import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current))

import loma

loma_sqrt_ = loma.Sqrt()
loma_sum_ = loma.Sum()
loma_sum_aggr_ = loma.SumAggr()
loma_relu_ = loma.ReLU()
loma_silu_ = loma.SiLU()
loma_sigmoid_ = loma.Sigmoid()
loma_add_ = loma.Add()
loma_add_broadcast_ = loma.AddBroadcast()
loma_sub_ = loma.Sub()
loma_mul_ = loma.Mul()
loma_mul_broadcast_ = loma.MulBroadcast()
loma_div_ = loma.Div()
loma_linear_ = loma.Linear()
loma_mse_ = loma.MSELoss() 
loma_mae_ = loma.MAELoss()