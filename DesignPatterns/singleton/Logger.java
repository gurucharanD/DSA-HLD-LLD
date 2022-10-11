package DesignPatterns.singleton;

class Logger {
    private static Logger loggerInstance = null;

    private Logger() {
    }

    static Logger getLoggerInstance() {
        if (loggerInstance == null) {
            // synchronized block
            // to allow only thread to access
            // the instance creation at any point of time
            synchronized (Logger.class) {
                if (loggerInstance == null) {
                    loggerInstance = new Logger();
                }
            }
        }
        return loggerInstance;
    }

    public void print(String msg) {
        System.out.println("new msg:" + msg + loggerInstance);
    }
}
