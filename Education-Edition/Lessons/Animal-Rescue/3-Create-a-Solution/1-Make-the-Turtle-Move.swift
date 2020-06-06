func moveTurtle() {
    ev3.move(forSeconds: 10, leftPort: .b, rightPort: .c, leftPower: -100, rightPower: -100)
}

moveTurtle()
