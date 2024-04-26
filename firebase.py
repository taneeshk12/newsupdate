
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import os

firebase_credentials = credentials.Certificate({
    "type": os.environ["service_account"],
    "project_id": os.environ["ideaism-blog"],
    "private_key_id": os.environ["f03ffb0eb89a99cc50cc0645915e10ab175e8377"],
    "private_key": os.environ["-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC8VM1ibTVeOzGR\n2b8KW+v96/DXDbP5JmZLEnqKjFxwCiaW+YTnEYJZ8WdErdnrzdXBKqgHZ/j3Fo+Z\n+YKbFFTQdVT6OMyFjrNSPmle2Xkhd8mV1mhGTvE0ytZrwpzDDEQA44Z+QVisP9Wv\n33DCkPPNLzKqSCGSq6mgXWjqds55uy1TRb8zLI/QzriDii71TR1seSOuLCxwd2mE\nj/fq8TaK8PxyVW0EWp/X0FjkYfqiFUgDMCKCfBW5eNZDGIcZT6KTfAwwzhwVPh/u\nXbIopQzIj5GacFBndFToRmUkRkVpzK2hI1eTcSKiSXlSWioBgFBgQHnMBDAA62r0\nn9ZXy459AgMBAAECggEAUHsy6/F8gYDtTYVOgRhIMNJvsQ8/jmUNCN7kNCoIZK7J\nz/HgjDhsypABkBV1T7I+OxbGCKgzejAPfP7mA+y70/uYLXgxWo/hbO+T6v8npxhA\nMsKV/BnHNUbLO/DGOgoXU4Pn2TOGt9FtuYNUdikortIRJji99CZczlWsvKm50cXh\n70FvtQFEDb5dYv9o34CrABRYvkjALthW08C6njTWPEmVCDHextP4MzmyO1RYRSQ8\ncODfsN3jPHQ34qStJv+Upo5sU27YRKdOyjTZ9SHeB03sshO4bGD4BjM8Abdt+h3j\nfxFYERkDUJudnN0Zfy6Bhv+GxJbMdUXUTh7wT6+ORwKBgQDpvmzWcUsiqCJq3eD2\nzPU/zfTXTCvQIpb0JLAgHKf0YcjScTRju8iX383IMr7vlH6vbGAow9/LU7uzlZYp\n9zJzHdLCpmohXkVrFEB9Cc3RzaIVU19q8nTe7KB5BYmahIHBlpcnigbbAoY4imxV\nT0UF1o8ZcMeiNs7l10tCu1qy8wKBgQDOQ26Ud3Kj4TrVZulm99U9cHQVlmVqkBi9\nsfZVv1iWhigJqqGT/zRje+qVuu6sNqhUDQNQWdCdpeqUgQjP6pv9Jv7U+Fjy//3Y\nFIytYXXEDZbDQo0ecIBrU/Mo39lsK+kf0JHDI6Afw8l3e+BMnGdMHVaOYi2mQ16p\nYFbAsla0zwKBgQC1N/e1whxYgDY+2ErjzT+O+iSLDvkg4tBZ9F/AZbcpVu6ViULu\n19XLOa6XOhCiOmSFqOZcdI/7Wa26q4zCeG5apZKTauX5fNchD5B34LP7pwu0sPDX\nP6awdpBrg4mNjJH0/sWt1+s8vRZGm7sl4NFIl3JWbQO5lfiOZX5p/EtzVQKBgBjm\nuyrhYM24G0o4KmVr9ip8sQcKKSQ8UUBVg8/GUgOaHqtMFkWvwbtg8mkxMC9KSfgb\nuhKxRSZDKZbUHSQ8xqhBVPKRKOvtS9ASawljgrwwh8r69d5+5oIOmISOwcj1ZCeb\nHn3YhzROhrwOEH4vQ6lEwXZfE/PGnl8EanTJEv6xAoGBAJzVpP5wBV7Na87Btkte\nfkCJnhgym+AC89TgH/Gb89STDPGauxTV9fBwb9DxzNYp4rlJE+F8gh9WcN/AO8wk\nhEQQyJ+/ypXq/BrVveCOX3BmBJUjZkRoyFGsVOWaxAC81QZaSNB2VrR3pmTND5QJ\njbpAllgAZVKFJjqVCO+4MoHS\n-----END PRIVATE KEY-----\n"].replace("\\n", "\n"),
    "client_email": os.environ["firebase-adminsdk-zeusk@ideaism-blog.iam.gserviceaccount.com"],
    "client_id": os.environ["111195026095062633402"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ["https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zeusk%40ideaism-blog.iam.gserviceaccount.com"]
})



# cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(firebase_credentials)

store = firestore.client()
doc_ref = store.collection('mail').limit(2)
mail_ids = []
try:
    docs = doc_ref.get()
    for doc in docs:
        mail_id = doc.to_dict().get('text')
        if mail_id:
            mail_ids.append(mail_id)
        print(u'Doc Data:{}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')

# print("Mail IDs:", mail_ids)