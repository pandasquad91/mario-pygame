#!/bin/bash
eval "$(pyenv init -)"
pyenv activate mario-pygame
pytest tests/