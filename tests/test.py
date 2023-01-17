import sys, os
import pytest
import requests

sys.path.append(os.getcwd())

from YaDisk import YaUploader

def test_create_folder():
    host = YaUploader.HOST
    token = YaUploader.token
    
    url = f'{host}/v1/disk/resources/'
    
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }
    
    params = {'path': 'disk:/ДляПроверки'}
    response = requests.get(url, params=params, headers=headers)
    print(response.status_code)
    assert response.json()['name'] == 'ДляПроверки'
    assert response.status_code == 200
    
    
    

if __name__ == '__main__':
    pytest.main(['tests/test.py'])