#!/usr/bin/env python3
"""Vertiv RPP Simulator.

The setup configuration is below.
"""
import asyncio
import logging

from pymodbus import pymodbus_apply_logging_config
from pymodbus.server.simulator.http_server import ModbusSimulatorServer


_logger = logging.getLogger()


if __name__ == "__main__":
    pymodbus_apply_logging_config("DEBUG")
    _logger.info("### start Vertiv RPP simulator")
    task = ModbusSimulatorServer(
        modbus_server="vertiv",
        modbus_device="vertiv",
        http_port=6081,
        # json_file="/home/simulator/umg804/setup.json"
        json_file="./setup.json"
    )
    asyncio.run(task.run_forever(), debug=True)
    _logger.info("### stop Vertiv RPP simulator")
