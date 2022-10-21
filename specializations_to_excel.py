import requests
import pandas as pd
from env import *


def main():
  try:
    df = pd.DataFrame()
    response = requests.get(SERVER_ADDRESS+ENDPOINT_SPECIALIZATIONS)
    if(response.status_code == 200):
      listDict = response.json()

      df = pd.concat([df, pd.DataFrame.from_records([listDict[i] for i in range(0, len(listDict))])])
      df = df.drop(['id'], axis=1)
      df.to_excel('especializaciones.xlsx', index=False, sheet_name='Especialidades')
  except ValueError:
    print('An unexpected error has occurred')
  except EnvironmentError:
    print('An environment error has occurred')
  except ConnectionError:
    print('An connection error has occurred')
  except TimeoutError:
    print('A timeout error has ocurred')


if __name__ == '__main__':
  main()