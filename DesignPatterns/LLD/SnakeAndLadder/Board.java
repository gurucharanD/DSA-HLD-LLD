package DesignPatterns.LLD.SnakeAndLadder;

import java.util.concurrent.ThreadLocalRandom;

// this class is responsible for 
// creating the board
// initialsing the players
// adding snakes and laders to the game

public class Board {

    Cell[][] cells;

    Board(int boardSize, int noOfSnakes, int noOfLadders) {
        this.initialiseCells(boardSize);
        this.addSnakesAndLadders(cells, noOfSnakes, noOfLadders);
    }

    private void initialiseCells(int boardSize) {
        cells = new Cell[boardSize][boardSize];

        for (int i = 0; i < boardSize; i++) {
            for (int j = 0; j < boardSize; j++) {
                Cell cellObj = new Cell();
                cells[i][j] = cellObj;
            }
        }
    }

    private void addSnakesAndLadders(Cell[][] cells2, int noOfSnakes, int noOfLadders) {
        while (noOfSnakes > 0) {
            int snakeHead = ThreadLocalRandom.current().nextInt(1, cells.length * cells.length - 1);
            int snakeTail = ThreadLocalRandom.current().nextInt(1, cells.length * cells.length - 1);

            if (snakeHead <= snakeTail) {
                continue;
            }

            Jump snakeObj = new Jump();
            snakeObj.start = snakeHead;
            snakeObj.end = snakeTail;

            Cell cell = getCell(snakeHead);
            cell.jump = snakeObj;

            noOfSnakes--;
        }

        while (noOfLadders > 0) {
            int ladderHead = ThreadLocalRandom.current().nextInt(1, cells.length * cells.length - 1);
            int ladderTail = ThreadLocalRandom.current().nextInt(1, cells.length * cells.length - 1);

            if (ladderHead >= ladderTail) {
                continue;
            }

            Jump ladderObj = new Jump();
            ladderObj.start = ladderHead;
            ladderObj.end = ladderTail;

            Cell cell = getCell(ladderHead);
            cell.jump = ladderObj;

            noOfLadders--;
        }
    }

    Cell getCell(int playerPosition) {
        int row = playerPosition / cells.length;
        int col = playerPosition % cells.length;
        return this.cells[row][col];
    }

}
