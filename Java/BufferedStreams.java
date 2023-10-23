

public class BufferedStreams<T> {

    T data[] = (T[]) new Object[3];
    public static void main(String[] args) throws Exception{
        BufferedStreams<String> bs = new BufferedStreams<String>();
        bs.data[0] = new String("test3");
        bs.data[1] = new String("test1");
        bs.data[2] = new String("test2");        
    }
}
