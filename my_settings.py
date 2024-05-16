DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'button',
        'USER' : 'button_dev3',
        'PASSWORD' : 'qing1105!', # 설정한 비밀번호로 적어주면 된다.
        'HOST' : '118.44.218.236',
        'PORT' : '6000',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'djangoConnectTest',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://<username>:<password>@<cluster-address>/<dbname>?retryWrites=true&w=majority'
        }
    }
}
