import random, string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

n_char = 8
n_type = 2

all_c = lowercase + uppercase + uppercase + digits + punctuation

rand_lower = random.sample(lowercase, n_type)
rand_upper = random.sample(uppercase, n_type)
rand_digit = random.sample(digits, n_type)
rand_punctuation = random.sample(punctuation, n_type)

rand_all = rand_lower + rand_upper + rand_digit + rand_punctuation 
passwd = ''.join(rand_all)

print()
print(passwd)
print()







