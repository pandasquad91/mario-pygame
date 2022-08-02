#!/bin/bash
eval "$(pyenv init -)"
pyenv activate mario-pygame
pylint src/ 