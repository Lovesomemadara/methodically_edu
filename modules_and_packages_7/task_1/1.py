import string
import random

letters: str = string.ascii_letters + string.digits
# rand_letters: list[str] = random.choices(letters, k=10)
# rand_letters: list[str] = random.sample(letters, k=10)

result: list[str] = []
for _ in range(10):
    result.append(random.choice(letters))

print(result)
