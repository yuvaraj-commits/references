#%%
import pickle


data = {
    'hash_key':'5200881839:AAGSwS9zgeRjVw1F5CKCVcfls1cppZn3FDo'
    }

with open('support_lib.serialized', 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


#%%
import pickle
with open('support_lib.serialized', 'rb') as handle:
    b = pickle.load(handle)

print(b['hash_key'])
