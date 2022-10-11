package DesignPatterns.AbstractFactory;

interface Factory {
    public Button createButton();

    public TextBox createTextBox();
}

class MacFactory implements Factory {
    public MacButton createButton() {
        return new MacButton();
    }

    public MacTextBox createTextBox() {
        return new MacTextBox();
    }
}

class WinFactory implements Factory {
    public WinButton createButton() {
        return new WinButton();
    }

    public WinTextBox createTextBox() {
        return new WinTextBox();
    }
}
