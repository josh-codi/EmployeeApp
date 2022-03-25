import random 

def generate_code():
    code = ''.join(random.choice('0123456789') for i in range(3))
    return code