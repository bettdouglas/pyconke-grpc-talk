# bin/sh

echo "Generating python stubs"

python -m grpc_tools.protoc --proto_path=protos/ --python_betterproto_out=protos/python_out/ --grpc_python_out=protos/python_out/ event_service.proto domain.proto

echo "Finished generating python stubs"
