import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
PROTO_DIR = ROOT_DIR / "proto"
OUT_DIR = ROOT_DIR / "src" / "shared_proto"

def compile_protos():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    
    proto_files = list(PROTO_DIR.glob("*.proto"))
    if not proto_files:
        print("No proto files found.")
        return

    cmd = [
        "python", "-m", "grpc_tools.protoc",
        f"-I{PROTO_DIR}",
        f"--python_out={OUT_DIR}",
        f"--grpc_python_out={OUT_DIR}",
        *[str(p) for p in proto_files]
    ]
    
    subprocess.run(cmd, check=True)
    
    for grpc_file in OUT_DIR.glob("*_pb2_grpc.py"):
        content = grpc_file.read_text()
        for proto in proto_files:
            base_name = proto.stem
            content = content.replace(f"import {base_name}_pb2", f"from . import {base_name}_pb2")
        grpc_file.write_text(content)

    print(f"Successfully compiled {len(proto_files)} proto files to {OUT_DIR}")

if __name__ == "__main__":
    compile_protos()
