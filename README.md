# ops-hub-platform

### Monorepo
https://medium.com/@life-is-short-so-enjoy-it/python-monorepo-with-uv-f4ced6f1f425
https://dev.to/ctrix/mastering-python-monorepos-a-practical-guide-2b4

### gRPC
https://medium.com/mitb-for-all/a-very-simple-introduction-to-grpc-6a666a039c03

### uv
https://hub.asimov.academy/blog/uv-python/

### Generate the gRPC Code

# Run from the root or inside packages/shared-proto
 uv add --dev grpcio-tools

uv run --package shared-proto python -m grpc_tools.protoc \
  -Ipackages/shared-proto/proto \
  --python_out=packages/shared-proto/src/shared_proto \
  --grpc_python_out=packages/shared-proto/src/shared_proto \
  packages/shared-proto/proto/*.proto

uv run python packages/shared-proto/scripts/compile_proto.py