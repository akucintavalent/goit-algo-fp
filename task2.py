import turtle


def draw_pitagorean_tree(t, depth, size):
    if depth == 0:
        return

    # Draw the current branch
    t.forward(size)
    t.left(45)

    # Draw the left subtree
    draw_pitagorean_tree(t, depth - 1, size / 2)

    t.right(90)

    # Draw the right subtree
    draw_pitagorean_tree(t, depth - 1, size / 2)

    t.left(45)
    t.backward(size)


def main():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Start pointing upwards
    t.penup()
    t.goto(0, -300)  # Move to the starting position
    t.pendown()

    depth = int(input("Enter the depth of the Pythagorean tree (up to 10): "))

    if depth < 1 or depth > 10:
        print("Please enter a depth between 1 and 10.")
        return

    size = 300  # Initial size of the branches

    draw_pitagorean_tree(t, depth, size)

    turtle.done()


if __name__ == "__main__":
    main()
