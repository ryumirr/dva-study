package _7_27;

public class GreetingLambda {

    private final GreetingService service;

    public GreetingLambda() {
        this.service = new GreetingService(); // 직접 주입 (단순 예시)
    }

    public String handleRequest(String name) {
        return service.greet(name);
    }
}
