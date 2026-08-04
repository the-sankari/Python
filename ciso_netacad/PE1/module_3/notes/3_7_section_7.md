## 3.7 Section 7 - Lists in advanced applications

> Nested lists are the Python way to model tables, grids, and layered data.

## At a glance

| Concept            | Simple meaning                   | Example                       |
| ------------------ | -------------------------------- | ----------------------------- |
| List comprehension | A short way to build a list      | `[x ** 2 for x in range(10)]` |
| Nested list        | A list that contains other lists | `board[row][column]`          |
| Matrix             | A 2D list                        | chessboard, weather table     |
| 3D list            | A list with three levels         | building, floor, room         |

## 1) Lists inside lists

A list does not have to hold only numbers or text. It can hold other lists.

Think of a chessboard:

- rows go across
- columns go down
- each square has one position

If each row is a list, then the whole board becomes a list of rows.

```python
row = []

for i in range(8):
    row.append(WHITE_PAWN)
```

That code creates one row with 8 pawns.

The same idea can be written more neatly with a list comprehension:

```python
row = [WHITE_PAWN for i in range(8)]
```

### Mental model

- left side: the value you want to repeat
- right side: how many times to repeat it

## 2) List comprehensions

A list comprehension is a compact way to create a list.

General pattern:

```python
[expression for item in iterable if condition]
```

Examples:

```python
squares = [x ** 2 for x in range(10)]
twos = [2 ** i for i in range(8)]
odds = [x for x in squares if x % 2 != 0]
```

What each one does:

| Example   | Result                         |
| --------- | ------------------------------ |
| `squares` | numbers squared from 0 to 9    |
| `twos`    | powers of 2                    |
| `odds`    | only odd values from `squares` |

## 3) Two-dimensional lists

When a list contains rows, it becomes a 2D list, also called a matrix.

For an 8 x 8 chessboard:

```python
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
```

You can also build it with one nested comprehension:

```python
board = [[EMPTY for i in range(8)] for j in range(8)]
```

### How to read it

- the inner list builds one row
- the outer list repeats that row 8 times

### How to access a cell

Use two indexes:

```python
board[row][column]
```

Examples:

```python
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[4][2] = KNIGHT
board[3][4] = PAWN
```

### Quick rule

- first index = row
- second index = column

## 4) Real-world example: weather data

The weather station stores temperatures for:

- 31 days
- 24 hours per day
- one float value per reading

That gives us a table with 31 rows and 24 columns.

```python
temps = [[0.0 for h in range(24)] for d in range(31)]
```

### Average temperature at noon

Midnight is hour 0, so noon is hour 11.

```python
total = 0.0

for day in temps:
    total += day[11]

average = total / 31
print("Average temperature at noon:", average)
```

### Highest temperature in the month

```python
highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)
```

### Count hot days

```python
hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print("Number of hot days:", hot_days)
```

## 5) Three-dimensional lists

Lists can go deeper than two levels.

Example:

```python
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
```

This can represent:

- 3 buildings
- 15 floors per building
- 20 rooms per floor

Access pattern:

```python
rooms[building][floor][room]
```

Examples:

```python
rooms[1][9][13] = True
rooms[0][4][1] = False
```

Count free rooms on one floor:

```python
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
```

## Key takeaways

- A list can contain other lists.
- Nested lists are useful for tables, grids, and layered structures.
- List comprehensions are the shortest clean way to create many lists.
- A 2D list uses two indexes: row and column.
- A 3D list adds another level, such as building, floor, and room.

## Short summary

Use a normal list when data is simple.
Use a nested list when data has structure.
Use a list comprehension when you want to build that structure clearly and quickly.
