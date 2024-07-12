#!/usr/bin/env python3
import asyncio
from 2_measure_runtime import measure_runtime

async def main():
    print(await measure_runtime())

asyncio.run(main())

