# replace this with your stuff

# depends on address of server
API_BASE = 'http://localhost:2048/api'
AUTH_BASE = 'http://localhost:2048/auth'
# http://localhost:2048/auth/authorize is used for authorization page
# http://localhost:2048/auth/token is used for exchange access taken
# see details in auth.py
CLIENT_ID = 'da49d2ac-5c2f-4d7f-b1cb-2acc79cf3809'
REDIRECT_URI = 'http://localhost:8000/recv_redirect'

SCOPES = ['user/Sequence.read','user/Sequence.write',
        'user/observationforgenetics.read',
        'user/reportforgenetics.read',
        'user/Patient.read',
        'user/Condition.read'
]
