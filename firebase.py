
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

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