package DesignPatterns.LLD.SnakeAndLadder;

import java.util.Deque;
import java.util.LinkedList;

public class Game {
    Board board;
    Dice dice;
    Deque<User> playerList = new LinkedList<>();
    User winner;

    Game() {
        this.intilaiseGame();
    }

    private void intilaiseGame() {
        this.board = new Board(10, 5, 4);
        this.dice = new Dice(1);
        this.winner = null;
        this.addPlayers();
    }

    private void addPlayers() {
        User p1 = new User("p1", 0);
        User p2 = new User("p2", 0);

        this.playerList.add(p2);
        this.playerList.add(p1);
    }

    public void startGame() {

        while (winner == null) {

            // check whose turn now
            User playerTurn = findPlayerTurn();
            System.out.println("player turn is:" + playerTurn.id + " current position is: " + playerTurn.position);

            // roll the dice
            int diceNumbers = dice.rollDice();

            // get the new position
            int playerNewPosition = playerTurn.position + diceNumbers;
            playerNewPosition = jumpCheck(playerNewPosition);
            playerTurn.position = playerNewPosition;

            System.out.println("player turn is:" + playerTurn.id + " new Position is: " + playerNewPosition);
            // check for winning condition
            if (playerNewPosition >= board.cells.length * board.cells.length - 1) {

                winner = playerTurn;
            }

        }

        System.out.println("WINNER IS:" + winner.id);
    }

    private User findPlayerTurn() {

        User playerTurns = playerList.removeFirst();
        playerList.addLast(playerTurns);
        return playerTurns;
    }

    private int jumpCheck(int playerNewPosition) {

        if (playerNewPosition > board.cells.length * board.cells.length - 1) {
            return playerNewPosition;
        }

        Cell cell = board.getCell(playerNewPosition);
        if (cell.jump != null && cell.jump.start == playerNewPosition) {
            String jumpBy = (cell.jump.start < cell.jump.end) ? "ladder" : "snake";
            System.out.println("jump done by: " + jumpBy);
            return cell.jump.end;
        }
        return playerNewPosition;
    }

}
