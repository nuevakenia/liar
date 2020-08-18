# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import gym

environment = gym.make("MountainCar-v0")
environment.reset()
for _ in range(2000):
    environment.render()
    environment.step(environment.action_space.sample())
