import hashlib 

while True:
    string = str(input('Digite sua string: '))
    hash = hashlib.sha1(string.encode()).hexdigest()
    print(hash)