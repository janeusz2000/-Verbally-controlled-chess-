#!/bin/bash
# coding=utf-8

virtualenv -p python3 proto_env
# shellcheck disable=SC1091
source proto_env/bin/activate
pip install grpcio-tools==1.7.0

function cleanup() {
    # shellcheck disable=SC1091
    rm -rf proto_env
}
trap cleanup EXIT

echo "Generating tribune Python protobuf/grpc sources."
path_i="../proto"
path_o="."
python3 -m grpc_tools.protoc \
	        -I${path_i} \
            --python_out=${path_o} \
            --grpc_python_out=${path_o} \
            ${path_i}/tribune_tts.proto

# Fix buggy autogenerated GRPC import
#sed -i 's/import tribune_tts_pb2 as tribune__tts__pb2/from . import tribune_tts_pb2 as tribune__tts__pb2/' ${path_o}/tribune_tts_pb2_grpc.py
