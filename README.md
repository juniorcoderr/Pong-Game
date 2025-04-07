# 🕹️ Python Pong Game

Welcome to a simple and fun version of the classic **Pong game**, built using **Python** and the **Turtle graphics module**. This project is designed for **beginners** who are learning **object-oriented programming (OOP)** and want to see how classes and game logic come together in a real project.

---

## 🌟 What You Will Learn

By going through this project, you will learn:

- How to use the `turtle` module to draw graphics and create animations.
- How to structure a Python project using **multiple files and classes**.
- How to use **OOP concepts** like inheritance and methods.
- How to detect **collisions** between game objects.
- How to control game flow using a **main game loop**.
- How to handle **keyboard input** for real-time controls.

---

## 📂 Project Structure

Here’s a quick overview of all the files:

```
pong-game/
├── main.py          # Main game loop and logic
├── paddle.py        # Code for the player paddles
├── ball.py          # Code for the moving ball
└── scoreboard.py    # Code for tracking and showing the score
```

---

## 🧠 Detailed Concepts Used

### ✅ 1. `main.py` - The Game Engine

This is the central part of the game. It does the following:

#### 📺 Screen Setup
```python
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
```
- Creates a screen window of size 800x600 pixels.
- Sets background color to black and title to “Pong”.
- `screen.tracer(0)` turns off automatic animation so we can manually update the screen for smooth gameplay.

#### 🕹️ Paddle & Ball Setup
```python
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
```
- Initializes 2 paddles on each side and places them at fixed X coordinates.
- Also creates a `Ball` object and a `Scoreboard`.

#### 🎮 Keyboard Controls
```python
screen.onkeypress(right_paddle.start_moving_up, "Up")
screen.onkeyrelease(right_paddle.stop_moving_up, "Up")
...
```
- Uses `onkeypress()` and `onkeyrelease()` to detect when a key is pressed or released.
- Allows **smooth movement** when keys are held down.

#### 🔁 Game Loop
```python
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
```
- The game runs in an infinite loop.
- `time.sleep()` controls the speed of the game.
- Every loop updates the screen, checks for collisions, and moves the ball and paddles.

---

### ✅ 2. `paddle.py` - Paddle Class

This file defines a **Paddle** object. It inherits from `Turtle`, so it can move and be displayed on the screen.

#### 🛠️ Setup
```python
self.shape("square")
self.shapesize(stretch_wid=5, stretch_len=1)
```
- Makes a tall, thin rectangle by stretching the default square turtle shape.
- Each paddle is placed at a given X,Y coordinate.

#### 🔼 Movement Handling
```python
def go_up(self): ...
def go_down(self): ...
```
- Moves the paddle up/down by changing its Y-coordinate.
- Prevents it from going off-screen using boundary checks.

#### ⏫ Continuous Movement
```python
def start_moving_up(self): self.moving_up = True
def stop_moving_up(self): self.moving_up = False
```
- Uses boolean flags to track key holding for continuous paddle movement.

---

### ✅ 3. `ball.py` - Ball Class

The ball moves around the screen and interacts with the paddles and screen borders.

#### ➕ Initialization
```python
self.shape("circle")
self.x_move = 10
self.y_move = 10
self.move_speed = 0.1
```
- The ball moves 10 pixels per update in both X and Y directions.
- `move_speed` controls how fast the ball moves (used in `time.sleep()`).

#### 🎯 Ball Movement
```python
def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)
```
- Moves the ball by adding values to its current X and Y positions.

#### 🔄 Bouncing Logic
```python
def bounce_y(self): self.y_move *= -1
def bounce_x(self): self.x_move *= -1
```
- Reverses direction to simulate bouncing off walls or paddles.
- `bounce_x()` also increases speed a bit to make the game harder.

#### 🧹 Reset Position
```python
def reset_position(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.bounce_x()
```
- Called when a player misses the ball.
- Resets ball to center and flips its direction.

---

### ✅ 4. `scoreboard.py` - Score Tracker

This class is used to display and update the score.

#### 🧾 Initialization
```python
self.left_score = 0
self.right_score = 0
```
- Keeps track of both players' scores.
- Uses Turtle’s `write()` method to display scores on screen.

#### 🔢 Updating Score
```python
def left_point(self): self.left_score += 1
def right_point(self): self.right_score += 1
```
- These methods increase the score and refresh the scoreboard.

---

## 🎮 Controls

| Player | Key to Move Up | Key to Move Down |
|--------|----------------|------------------|
| Left   | W              | S                |
| Right  | Up Arrow       | Down Arrow       |

**Hold the key** to move the paddle continuously.

---

## 🔧 How to Run the Game

1. Make sure you have Python installed.
2. Clone or download this repository.
3. Run the game using this command:

```bash
python main.py
```

A game window will open. Play and have fun!

---

## 🏁 Goals for Improvement

- Add a start screen
- Add sound effects
- Add a single-player mode with AI
- Keep high scores
- Add difficulty levels

---

## 💡 Final Thoughts

This Pong game is a great **beginner-friendly project** that teaches you how to:

- Use the turtle module for animation
- Break code into different classes and files
- Control object movement and detect collisions
- Build interactive apps with keyboard input

---

## 🙋 Need Help?

If you get stuck, feel free to [open an issue](https://github.com/juniorcoderr/Pong-Game/issues) or message me. Happy coding!
