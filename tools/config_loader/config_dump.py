#!/usr/bin/env python3

from __future__ import print_function

import logging
import random
import json

import grpc
import katran_pb2_grpc
import katran_pb2

lb_config = []

if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = katran_pb2_grpc.KatranServiceStub(channel)
    for vip in stub.getAllVips(katran_pb2.Empty()).vips:
        v_reals = []
        v_flags = stub.getVipFlags(vip)
        v_config = { 'address' : vip.address, 'port': vip.port, 'protocol': vip.protocol, 'flags': v_flags.flags }
        lb_config.append(v_config)
    print (json.dumps(lb_config))
