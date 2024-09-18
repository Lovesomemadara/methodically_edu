import string
import random

N: int = 10
CHARS: str = string.ascii_letters + string.digits

# №1
rand_letters: list[str] = random.choices(CHARS, k=N)

# №2
rand_letters: list[str] = random.sample(CHARS, k=N)

# №3
result: list[str] = []
for _ in range(N):
    result.append(random.choice(CHARS))

print(result)
