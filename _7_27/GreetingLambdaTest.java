package _7_27;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class GreetingLambdaTest {

    @Test
    void testHandleRequest() {
        GreetingLambda lambda = new GreetingLambda();
        String response = lambda.handleRequest("So-Yeon");
        assertEquals("Hello, So-Yeon", response);
    }
}
