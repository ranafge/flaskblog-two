from app import app
from time import time
import jwt


def get_reset_password_token(expires_in=600):
    return jwt.encode({'reset_password': 2, 'exp': time() + expires_in},
                      app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')


@staticmethod
def verify_reset_password_token(token):
    id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
    print('ID IS', id)



if __name__ == "__main__":
    print(get_reset_password_token())