package org.calc.server;

import io.grpc.stub.StreamObserver;
import org.calc.gen.*;

public class CalculatorImpl extends CalculatorGrpc.CalculatorImplBase {

    @Override
    public void add(ArithmeticOpArguments request, StreamObserver<ArithmeticOpResult> responseObserver) {
        int result = request.getArg1() + request.getArg2();
        ArithmeticOpResult response = ArithmeticOpResult.newBuilder().setRes(result).build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    @Override
    public void subtract(ArithmeticOpArguments request, StreamObserver<ArithmeticOpResult> responseObserver) {
        int result = request.getArg1() - request.getArg2();
        ArithmeticOpResult response = ArithmeticOpResult.newBuilder().setRes(result).build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    // tried to implement ComplexOperation (SUM, AVG, MIN, MAX),
    // but reflection implementation for Java does not support describing enums in grpcurl
    @Override
    public void avg(AvgArithmeticOpArguments request, StreamObserver<AvgArithmeticOpResult> responseObserver) {
        int argsSize = request.getArgsList().size();
        double result = argsSize != 0 ? request.getArgsList().stream().reduce(Double::sum).orElse(0d) / argsSize : 0d;
        AvgArithmeticOpResult response = AvgArithmeticOpResult.newBuilder().setRes(result).build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
