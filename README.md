# ping-pong-game

A simple Ping Pong game implemented using Python's `turtle` module. This is a two-player game where each player controls a paddle, and the goal is to score points by getting the ball past the opponent.

## Table of Contents
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Controls](#controls)
- [Acknowledgment](#acknowledgment)

## Installation

1. Make sure you have Python installed. You can download it [here](https://www.python.org/downloads/).
2. Install the `turtle` module if not already available. The `turtle` module is included with Python, but if needed, you can run:
   ```bash
   pip install PythonTurtle
Clone this repository or copy the Python script into a file named `ping_pong.py`.

## How to Play

- The game is played between two players.
- Each player controls a paddle and tries to prevent the ball from passing their paddle to score points.
- The first player to reach a certain score wins.

## Game Objective

- Player 1 (left) and Player 2 (right) use their paddles to bounce the ball back to the opponent.
- If the ball passes one player's paddle, the other player scores a point.
- The ball bounces off the top and bottom borders, and paddles change its direction when hit.

## Features

- **Player 1 (Blue)** and **Player 2 (Red)** paddles.
- A **center dividing line**.
- Simple ball and paddle mechanics.
- Real-time score display for both players.
- Keyboard controls for moving the paddles.

## Controls

- **Player 1 (Left Paddle)**:
  - Move up: `W`
  - Move down: `S`
  
- **Player 2 (Right Paddle)**:
  - Move up: `Up Arrow`
  - Move down: `Down Arrow`

## Code Overview

- The game uses the `turtle` module for graphics and object handling.
- The ball and paddle objects are instances of `turtle.Turtle()`.
- A simple game loop handles the ball movement, collision detection, and scoring.

## Acknowledgment

This game is not fully inspired by me. It was built with reference to similar classic Ping Pong game implementations and online resources.
