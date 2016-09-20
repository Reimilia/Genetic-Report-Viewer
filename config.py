# replace this with your stuff

# depends on address of server
API_BASE = 'http://localhost:2048/api'
AUTH_BASE = 'http://localhost:2048/auth'
# http://localhost:2048/auth/authorize is used for authorization page
# http://localhost:2048/auth/token is used for exchange access taken
# see details in auth.py
CLIENT_ID = 'c3425824-351f-4b54-b607-2ec0640dbecc'
REDIRECT_URI = 'http://localhost:8000/recv_redirect'

SCOPES = ['user/Sequence.read','user/Sequence.write',
        'user/observationforgenetics.read',
        'user/reportforgenetics.read',
        'user/Patient.read',
        'user/Condition.read'
]
