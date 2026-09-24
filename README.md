# ops-hub-platform

### Monorepo
https://medium.com/@life-is-short-so-enjoy-it/python-monorepo-with-uv-f4ced6f1f425
https://dev.to/ctrix/mastering-python-monorepos-a-practical-guide-2b4

### gRPC
https://medium.com/mitb-for-all/a-very-simple-introduction-to-grpc-6a666a039c03

### uv
https://hub.asimov.academy/blog/uv-python/

### add service
uv init services/auth-service

### add library
uv init packages/shares-proto --lib

### Generate the gRPC Code

# Run from the root or inside packages/shared_proto
 uv add --dev grpcio-tools

uv run --package shared_proto python -m grpc_tools.protoc \
  -Ipackages/shared_proto/proto \
  --python_out=packages/shared_proto/src/shared_proto \
  --grpc_python_out=packages/shared_proto/src/shared_proto \
  packages/shared_proto/proto/*.proto

uv run python packages/shared_proto/scripts/compile_proto.py