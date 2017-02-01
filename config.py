# replace this with your stuff

# depends on address of server
# FHIR fhirgenomics.ieadworkd
API_BASE = 'http://fhirgenomics.ideaworld.org//api'
AUTH_BASE = 'http://fhirgenomics.ideaworld.org//auth'

#API_BASE = 'http://localhost:2048/api'
#AUTH_BASE = 'http://localhost:2048/auth'
# http://localhost:2048/auth/authorize is used for authorization page
# http://localhost:2048/auth/token is used for exchange access taken
# see details in auth.py

# FHIR fhirgenomics.ieadworkd
CLIENT_ID = 'b8731f83-0979-472a-8197-c103b0b471b9'
#CLIENT_ID='2a6c8196-a55b-42d5-a1a2-8948bc0265b5'
REDIRECT_URI = 'http://localhost:8000/recv_redirect'

SCOPES = ['user/Sequence.read','user/Sequence.write',
        'user/observationforgenetics.read',
        'user/reportforgenetics.read',
        'user/Patient.read',
        'user/Condition.read',
        'user/Observation.read',
        'user/DiagnosticReport.read'
]
