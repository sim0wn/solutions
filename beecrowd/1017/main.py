# -*- coding: utf-8 -*-

duration, speed = [int(input()) for _ in range(2)]
distance = duration * speed
fuel = distance / 12

print(f"{fuel:.3f}")
