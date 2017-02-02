# replace this with your stuff

# depends on address of server
# FHIR fhirgenomics.ieadworkd
#API_BASE = 'http://fhirgenomics.ideaworld.org//api'
#AUTH_BASE = 'http://fhirgenomics.ideaworld.org//auth'
#API_BASE = 'http://genomics-advisor.smartplatforms.org:3000/api'
#AUTH_BASE = 'http://genomics-advisor.smartplatforms.org:3000/auth'
API_BASE = 'http://localhost:2048/api'
AUTH_BASE = 'http://localhost:2048/auth'
# http://localhost:2048/auth/authorize is used for authorization page
# http://localhost:2048/auth/token is used for exchange access taken
# see details in auth.py

# FHIR fhirgenomics.ieadworkd
#CLIENT_ID = 'b8731f83-0979-472a-8197-c103b0b471b9'
CLIENT_ID='56019b7e-6745-45f8-ae9e-7ada69c9995c'
REDIRECT_URI = 'http://localhost:8000/recv_redirect'

SCOPES = ['user/Sequence.read','user/Sequence.write',
        'user/observationforgenetics.read',
        'user/reportforgenetics.read',
        'user/Patient.read',
        'user/Condition.read',
        'user/Observation.read',
        'user/DiagnosticReport.read'
]
