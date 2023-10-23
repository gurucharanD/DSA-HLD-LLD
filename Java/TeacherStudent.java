class WhiteBoard {
    String text;
    int noOfStudents = 0;
    int count = 0;

    public void attendance() {
        noOfStudents++;
    }

    synchronized public void write(String t) {
        System.out.println("Teacher is writing " + t);
        // if count != 0 teacher will wait and then write the
        // text on the white board
        while (count != 0) {
            try {
                wait();
            } catch (Exception e) {
            }
        }
        text = t;
        count = noOfStudents;
        notifyAll();
    }

    synchronized public String read() {
        // student thread will wait while the count is 0
        // because when count is 0 teacher thread is writing
        while (count == 0) {
            try {
                wait();
            } catch (Exception e) {
            }
        }
        String t = text;
        count--;
        if (count == 0) {
            notify();
        }
        return t;
    }

}

class Teacher extends Thread {
    WhiteBoard wb;
    String notes[] = {
            "text 1",
            "text 2",
            "text 3",
            "text 4",
            "text 5",
            "end"
    };

    Teacher(WhiteBoard wb) {
        this.wb = wb;
    }

    public void run() {
        for (int i = 0; i < notes.length; i++) {
            wb.write(notes[i]);
        }
    }
}

class Student extends Thread {
    WhiteBoard wb;
    String name;

    Student(WhiteBoard wb, String name) {
        this.wb = wb;
        this.name = name;
    }

    public void run() {
        this.wb.attendance();
        String text;

        do {
            text = wb.read();
            System.out.println(name + " reading " + text);
            System.out.flush();
        } while (!text.equals("end"));
    }
}

public class TeacherStudent {
    public static void main(String[] args) {
        WhiteBoard wb = new WhiteBoard();
        Teacher t = new Teacher(wb);
        Student s1 = new Student(wb, "s1");
        Student s2 = new Student(wb, "s2");
        Student s3 = new Student(wb, "s3");
        Student s4 = new Student(wb, "s4");
        t.start();
        s1.start();
        s2.start();
        s3.start();
        s4.start();
    }
}
