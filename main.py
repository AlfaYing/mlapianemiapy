from pydantic import BaseModel
from fastapi import FastAPI
import pickle
import json
import pandas as pd

app = FastAPI(title='Api Anemia predictora de tratamiento anemi',
                describe='Primera version del API',
                version='1.01')

class model_input(BaseModel):
        N_1 : int
        N_2 : int
        N_3: int
        N_4: int
        N_5: int
        N_6: int
        N_7: int
        N_LEV: int
        N_MOD: int
        N_P01: int
        N_P02: int
        N_P03: int
        N_P04: int
        N_P05: int
        N_P06: int
        N_PD: int
        N_PE: int
        N_RD: int
        N_SF1: int
        N_SF2: int
        N_SF3: int
        N_SF4: int
        N_SF5: int
        N_SF6: int
        N_TA: int
# loading the save model
# with open('LogisticRegressionV4.sav','rb') as f:
# anemia_model = pickle.load(f)
anemia_model = pickle.load(open('LogisticRegressionV8.sav','rb'))

@app.post('/anemia_predicction')
async def anemia_pred(item:model_input):
        input_data = item.json()
        input_data_for_model_request =  json.loads(input_data)

        input_1 =input_data_for_model_request['N_1'],
        input_2 =input_data_for_model_request['N_2'], 
        input_3 = input_data_for_model_request['N_3'],
        input_4 = input_data_for_model_request['N_4'],
        input_5 = input_data_for_model_request['N_5'],
        input_6 = input_data_for_model_request['N_6'],
        input_7 = input_data_for_model_request['N_7'],
        input_LEV = input_data_for_model_request['N_LEV'],
        input_MOD = input_data_for_model_request['N_MOD'],
        input_P01 = input_data_for_model_request['N_P01'],
        input_P02 = input_data_for_model_request['N_P02'],
        input_P03 = input_data_for_model_request['N_P03'],
        input_P04 = input_data_for_model_request['N_P04'],
        input_P05 = input_data_for_model_request['N_P05'],
        input_P06 = input_data_for_model_request['N_P06'],
        input_PD = input_data_for_model_request['N_PD'],
        input_PE = input_data_for_model_request['N_PE'],
        input_RD = input_data_for_model_request['N_RD'],
        input_SF1 = input_data_for_model_request['N_SF1'], 
        input_SF2 = input_data_for_model_request['N_SF2'],
        input_SF3 = input_data_for_model_request['N_SF3'],
        input_SF4 = input_data_for_model_request['N_SF4'],
        input_SF5 = input_data_for_model_request['N_SF5'],
        input_SF6 = input_data_for_model_request['N_SF6'],
        input_TA = input_data_for_model_request['N_TA']
        df = pd.DataFrame([item.dict().values()],columns=item.dict().keys())
        predicction = anemia_model.predict(df)
        if predicction[0] == 0:
                return "Pronostico: En paciente probablemente no recibirá un tratamiento completo."
        else:
                return "Pronostico: En paciente probablemente recibirá un tratamiento completo."